#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
*******************************************************************************
* Texmacs extension for LibreOffice
* COPYRIGHT  : (C) 2017-2022 Philippe JOYEZ
*******************************************************************************
* This software falls under the GNU general public license version 3 or later.
* It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
* in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.
*******************************************************************************

This code is very similar to the original Texmacs-Inkscape extension
It was stripped of Inkscape specific code, and adapted for python 3

depending on what is provided it will either 
-extract the texmacs code that was embedded in an svg drawing,
-use a latex descrition of an equation
-provide a dummy equation

and start texmacs to edit that equation. Once finished, the name of the
newly created svg image is returned (if any).

Communication with texmacs is established either though a socket, or
using pipes.

*****************************

this code is known to run with LO versions > 5.3 (which use python 3)

Note that the extension also comprises a few star basic scripts which
complete its functionality : inserting images in documents, and extracting
them for re-edition, copy/paste, converting mathtype equations ...

"""
#------------------------------------------------------------------------------

import os, glob, platform, time, uno
import tempfile, subprocess
from xml.etree import ElementTree as etree

import socket, shutil

IS_WINDOWS = (platform.system() == "Windows")
#IS_MACOS= sys.platform.startswith('darwin')

CTX = uno.getComponentContext()
SM = CTX.getServiceManager()


def create_instance(name, with_context=False):
    if with_context:
        instance = SM.createInstanceWithContext(name, CTX)
    else:
        instance = SM.createInstance(name)
    return instance

from com.sun.star.awt import MessageBoxButtons as MSG_BUTTONS

def msgbox(message, title='TeXmacs equation editor', buttons=MSG_BUTTONS.BUTTONS_OK, type_msg='infobox'):
    """ Create message box
        type_msg: infobox, warningbox, errorbox, querybox, messbox
        https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html
    """
    toolkit = create_instance('com.sun.star.awt.Toolkit')
    parent = toolkit.getDesktopWindow()
    mb = toolkit.createMessageBox(parent, type_msg, buttons, title, str(message))
    return mb.execute()

#https://wiki.documentfoundation.org/Macros/Python_Guide/Useful_functions#Execute_in_other_thread 



def texmacs_exe_path() :
  ''' Find texmacs path, save config file to user profile if necessary'''

  #https://www.linux.com/news/openofficeorg-basic-crash-course-saving-user-settings/
  createUnoService = XSCRIPTCONTEXT.getComponentContext().getServiceManager().createInstance
  SubstService = createUnoService("com.sun.star.util.PathSubstitution")
  UserPath = uno.fileUrlToSystemPath(SubstService.substituteVariables("$(user)", True))
  #res = msgbox("UserPath: "+UserPath, title='Where is TeXmacs?')
  
  texmacs_path = shutil.which('texmacs') # looking in $PATH
  if texmacs_path == None :
    texmacs_path = ""
  
  if (texmacs_path == "" ) and os.path.isfile(UserPath+'/texmacs_path.conf'):
  # try to load from saved config file
    with open(UserPath+'/texmacs_path.conf', 'r') as f:
      texmacs_path = f.read()
      if not(os.path.isfile(texmacs_path)):
          texmacs_path = ""
  
  if (texmacs_path == "" ) and IS_WINDOWS :
  # try usual windows system path
        def Is64Windows():
            return 'PROGRAMFILES(X86)' in os.environ
    
        def GetProgramFiles32():
            if Is64Windows():
                return os.environ['PROGRAMFILES(X86)']
            else:
                return os.environ['PROGRAMFILES']
    
        texmacs_path = os.path.join(GetProgramFiles32(), 'TeXmacs','bin', 'texmacs.exe')
        if not(os.path.isfile(texmacs_path)):
          texmacs_path = ""
        
  if texmacs_path == "":
  # ask to point to executable (Windows or Appimage)
    res = msgbox("Cannot locate your TeXmacs executable\nPlease locate it in the next dialog", title='Where is TeXmacs?')
    # based on https://stackoverflow.com/a/30863692
    path=None
    mode=0
    """
        read:  `mode in (0, 6, 7, 8, 9)`
        write `mode in (1, 2, 3, 4, 5, 10)`
        see: ('''https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1TemplateDescription.html''' )
    """
    #filepicker = createUnoService( "com.sun.star.ui.dialogs.OfficeFilePicker" )
    filepicker = createUnoService( "com.sun.star.ui.dialogs.FilePicker" ) #this is Os's file picker
    #if path:
    #    filepicker.setDisplayDirectory(path )
    filepicker.initialize( ( mode,) )
    filepicker.setTitle("Please locate your TeXmacs executable")
    if filepicker.execute():
        texmacs_path = uno.fileUrlToSystemPath(filepicker.getFiles()[0])
        with open(UserPath+'/texmacs_path.conf', 'w') as f:
          f.write(texmacs_path)
  return texmacs_path

#import codecs        
def string_unescape(s):
    """
etree.parse uses the encoding specified in the xml file (UTF8)
However when the svg is created, texmacs uses Cork encoding and escapes
the characters above 128 (for instance é => \xe9 ) and some special characters (&,<,>...)
so that the texmacs code recorded by texmacs
and read back by this python code in LO are not immediatly consistent.
Here, we take care that these characters are properly translated back to texmacs
(note also the .encode when writing the file content)
    """
    #return str(codecs.escape_decode(bytes(s, "utf-8").decode("us-ascii"))[0],"iso-8859-1")
    return bytes(s, 'utf8').decode('unicode_escape')

TEXTEXT_NS = u"http://www.iki.fi/pav/software/textext/"
TEXMACS_NS = u"https://www.texmacs.org/"
TEXMACS_OLD_NS = u"http://www.texmacs.org/"
SVG_NS = u"http://www.w3.org/2000/svg"


tm_file="<TeXmacs|1.99.5>\n\n<style|%s>\n\n<\\body>\n %s \n\n</body>\n\n<\\initial>\n %s \n\n</initial>"
tm_dummy_equation="<\equation*>\n    1+1\n  </equation*>\n"
tm_no_equation="\\;\n"
tm_scheme_cmd_line_args =  '(begin (lazy-plugin-force) (equ-edit-cmdline) %s) '
if IS_WINDOWS :
    tm_extra_latex_cmd_line_args=  "(delayed (:idle 000)(insert (latex->texmacs (parse-latex \\\"\\\\[ %s \\\\]\\\"))))"
else :
    tm_extra_latex_cmd_line_args=  '(delayed (:idle 000)(insert (latex->texmacs (parse-latex \"\\\\[ %s \\\\]\"))))'
tm_no_style=""

#------------------------------------------------------------------------------
# Talking with the (unofficial yet) TeXmacs Equation-editor plugin 
#------------------------------------------------------------------------------

tmp_path = tempfile.mkdtemp()
tmp_base = 'LO_edit_tmp.tm'
tmp_name = os.path.join(tmp_path,tmp_base)


def tm_equation(latex_code="", svg_file="", base_font_size=""):
    """create the temporary tm file according to the data provided on input
       then call texmacs
       This function is called from Basic"""
    latex_code = latex_code.replace("\\","\\\\")
    if svg_file != '' :
        # Find equation and how to modify it
        latex_code, tm_equation, tm_style, tm_style2 = get_equation_code(svg_file)
        scheme_cmd = tm_scheme_cmd_line_args % ''
    elif latex_code == '' :
        tm_equation, tm_style = (tm_dummy_equation, tm_no_style)
        tm_style2 = 'generic'
        scheme_cmd = tm_scheme_cmd_line_args % ''
    else :
        tm_equation, tm_style = (tm_no_equation, tm_no_style)
        tm_style2 = 'generic'
        # build full scheme command line command
        scheme_cmd = tm_scheme_cmd_line_args % (tm_extra_latex_cmd_line_args % latex_code)

    if  base_font_size != '' :
        """calling from writer, we adapt the font size in TeXmacs"""
        pos = tm_style.find('font-base-size') 
        if pos == -1 :
            pos = tm_style.find('</collection>')
            if pos >= 0 :
                tm_style = tm_style[:pos] + '<associate|font-base-size|'+base_font_size+'>'+tm_style[pos:]
            else :
                tm_style = '<collection|<associate|font-base-size|'+base_font_size+'>>'
        else :
            pos2 = tm_style.find('|',pos) +1
            pos3 = tm_style.find('>',pos2)
            tm_style = tm_style[:pos2] +base_font_size+tm_style[pos3:] 
    # call texmacs for editing
    svg_name = tmp_name + ".svg" #if successful texmacs creates that svg file
    try_remove(svg_name)
    call_texmacs(scheme_cmd, tm_equation, tm_style, tm_style2, latex_code)
    try_remove(tmp_name)
    if os.path.isfile(svg_name):
        return svg_name
    else :
        return ""

def get_equation_code(svg_name):
    """retrieve texmacs code for embedded equation in svg file"""
    f = open(svg_name, 'r')
    tree = etree.parse(f)
    f.close()
    #inkex.debug("file read  "+svg_name)
    root = tree.getroot()
    node = root.find('.//{%s}g[@{%s}texmacscode]' % (SVG_NS, TEXMACS_NS)) 
    # https://www.reddit.com/r/learnpython/comments/gp3ph1/find_element_whose_attribute_contains_a_value_in/?utm_source=share&utm_medium=web2x&context=3
    if node is not None:
        tm_equation = string_unescape(node.attrib.get('{%s}texmacscode' % TEXMACS_NS, ''))
        if '{%s}texmacsstyle'%TEXMACS_NS in node.attrib: #contains styling info (fonts , font size...)
            tm_style = string_unescape(node.attrib.get('{%s}texmacsstyle' % TEXMACS_NS, ''))
        else:
            tm_style =''
        if '{%s}texmacsstyle2'%TEXMACS_NS in node.attrib: #further contains document style info
            tm_style2 = string_unescape(node.attrib.get('{%s}texmacsstyle2' % TEXMACS_NS, ''))
        else:
            tm_style2 ='generic'
        return ('', tm_equation, tm_style, tm_style2)

    else : 
        node = root.find('.//{%s}g[@{%s}texmacscode]' % (SVG_NS, TEXMACS_OLD_NS)) 
        if node is not None:
            tm_equation = string_unescape(node.attrib.get('{%s}texmacscode' % TEXMACS_OLD_NS, ''))
            if '{%s}texmacsstyle'%TEXMACS_OLD_NS in node.attrib: #further contains styling info
                tm_style = string_unescape(node.attrib.get('{%s}texmacsstyle' % TEXMACS_OLD_NS, ''))
            else:
                tm_style =''
            return ('', tm_equation, tm_style, 'generic')

        else :
            node = root.find('.//{%s}g[@{%s}text]' % (SVG_NS, TEXTEXT_NS)) 
            if node is not None: #implements Textext conversion to TeXmacs
                latex_code = node.attrib.get('{%s}text' % TEXTEXT_NS, '')
                return (latex_code, tm_no_equation, tm_no_style, 'generic')
            else :
                return ('', tm_dummy_equation, tm_no_style, 'generic')

def call_texmacs(scheme_cmd, equ, styl, styl2, latex):
    """" handle various ways of calling and communicating with texmacs """
    f_tmp = open(tmp_name, 'wb') # create a temporaty tm file that texmacs will edit
    try:
        f_tmp.write((tm_file %(styl2, equ, styl)).encode("iso-8859-1")) #insert equation to be edited in file (blank in textext case)
    finally:
        f_tmp.close()

#try connecting already running texmacs on socket (spares boot-up time)
    size = 1024
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientsocket.settimeout(1.25)
        clientsocket.connect(('localhost', 6561))
        time.sleep(.5)
        msg='(0 (remote-login "inkscape" "inkscape"))\n'
        clientsocket.sendall(bytes(str(len(bytes(msg,'utf8')))+ '\n'+msg,'utf8'))
        clientsocket.setblocking(1)
        time.sleep(.1)
        msg = clientsocket.recv(size)
    except : #any error : can't connect (texmacs not running or server not started), no answer,...
        use_socket = False
        print("use_socket = False")
    else:
        if msg.find(b"ready") : use_socket = True
    #login was accepted; continue with socket connection (assume tm-service remote-equ is properly setup)
        else : use_socket = False #login failed. user not defined?
    if use_socket :
        clientsocket.settimeout(None)
        clientsocket.setblocking(1)
        if IS_WINDOWS :
            aux = tmp_name.replace('\\','\\\\')
        else :
            aux = tmp_name
        msg = '(0 (remote-equ "%s" "%s"))\n' % (aux , latex)
        clientsocket.sendall(bytes(str(len(bytes(msg,'utf8')))+ '\n'+msg,'utf8'))
        time.sleep(.1)
        data = clientsocket.recv(size)
#            print("recvd: " + str(len(data)) + " bytes")
#            print("recvd:" + data)
        clientsocket.close()
    else :

# socket connection failed : texmacs not in server mode or not started.
#
# Then, use old method : launch it with proper args on the command line
# and communicate through pipes.
#
# In that case, if texmacs has server mode enabled we want it to
# keep running after this script quits, for subsequent connections.
# This is straightforward on Linux/MacOs.
#
# However on Windows this script would hang until texmacs quits, unless
# Texmacs runs as a completly independent process and not a subprocess of this script.
# The next problem is that, on Windows, launching and independent process is
# incompatible with using stdin/stdout pipes; we thus use a named pipe to know 
# when texmacs has finished editing our first equation (sending "done" or "cancel" on stdout)
# Since python shipped with (windows-)inkscape does not have packages for
# handling nicely such named pipes we need to perform low level calls.
#  
# http://code.activestate.com/lists/python-list/446422/
# https://mail.python.org/pipermail/python-list/2005-March/355623.html
        texmacs_path = texmacs_exe_path()
        if IS_WINDOWS :
            import ctypes
            PIPE_ACCESS_DUPLEX = 0x3
            PIPE_TYPE_MESSAGE = 0x4
            PIPE_READMODE_MESSAGE = 0x2
            PIPE_WAIT = 0
            PIPE_NOWAIT = 0x1
            PIPE_UNLIMITED_INSTANCES = 255
            BUFSIZE = 4096
            NMPWAIT_USE_DEFAULT_WAIT = 0
            INVALID_HANDLE_VALUE = -1
            ERROR_PIPE_CONNECTED = 535

            tmPipename = r"\\.\pipe\namedpipe1"

            hPipe = ctypes.windll.kernel32.CreateNamedPipeW(tmPipename,
                                             PIPE_ACCESS_DUPLEX,
                                             PIPE_TYPE_MESSAGE |
                                             PIPE_READMODE_MESSAGE |
                                             PIPE_WAIT, PIPE_UNLIMITED_INSTANCES,
                                             BUFSIZE, BUFSIZE, NMPWAIT_USE_DEFAULT_WAIT,
                                             None
                                            )
            if (hPipe == INVALID_HANDLE_VALUE):
                msgbox("Error in creating Named Pipe")
                return
            cmd = '"'+texmacs_path+'" -x "'+scheme_cmd+'" "'+tmp_name+'" > '+tmPipename

            print (cmd)
            DETACHED_PROCESS = 8
            CREATE_NEW_PROCESS_GROUP = 512 #required for win7
            p = subprocess.Popen(cmd, shell=True, creationflags=CREATE_NEW_PROCESS_GROUP, close_fds=True)
            time.sleep(1)
            fConnected = ctypes.windll.kernel32.ConnectNamedPipe(hPipe, None)
            if ((fConnected == 0) and (ctypes.windll.kernel32.GetLastError() == ERROR_PIPE_CONNECTED)):
                fConnected = 1
            if (fConnected != 1) :
                msgbox("Sorry, could not connect with\n "+texmacs_path+"\n using named pipe", title='TeXmacs equation editor')
                return
            ERROR_MORE_DATA = 234
            BUFSIZE = 512
            chBuf = ctypes.create_string_buffer(BUFSIZE)
            cbRead = ctypes.c_ulong(0)
            while 1 : # repeat loop if ERROR_MORE_DATA
                fSuccess = ctypes.windll.kernel32.ReadFile(hPipe, chBuf, BUFSIZE, ctypes.byref(cbRead), None)
                if (fSuccess == 1) :
                    #print ("Number of bytes read:", cbRead.value)
                    #print (chBuf.value)
                    if ((b"done" in chBuf.value) or (b"cancel" in chBuf.value) ):
                        break
                elif (ctypes.windll.kernel32.GetLastError() != ERROR_MORE_DATA):
                    msgbox("error reading from named pipe")
                    break
                
            ctypes.windll.kernel32.FlushFileBuffers(hPipe)
            ctypes.windll.kernel32.DisconnectNamedPipe(hPipe)
            ctypes.windll.kernel32.CloseHandle(hPipe)

        else : # Linux, MacOS: so much simpler!
            cmd = [texmacs_path,"-x",scheme_cmd , tmp_name]
            try:
                p = subprocess.Popen(cmd, 
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
                while p.poll() is None:
                    output = p.stdout.readline()
                    if ((b"done" in output) or (b"cancel" in output) ):
                        break
            #except OSError as e:
            #    raise RuntimeError("Command %s failed: %s" % (' '.join(cmd), e))
            except :
                msgbox("launching texmacs failed   ")
            #    print( "launching texmacs failed   ")


def remove_temp_files():
    """Remove temporary files"""
    base = os.path.join(tmp_path, tmp_base)
    for filename in glob.glob(base + '*'):
        try_remove(filename)
    try_remove(tmp_path)

def try_remove(filename):
    """Try to remove given file, skipping if not exists."""
    if os.path.isfile(filename):
        os.remove(filename)
    elif os.path.isdir(filename):
        os.rmdir(filename)

"""functions exposed to LO"""
g_exportedScripts = tm_equation,

if __name__ == u'__main__':
    """allow runing the script standalone for debugging"""
    #tm_equation("", "/tmp/test.svg", "", "")
    tm_equation(r"\frac{a}{b}", "", "", "")
    #print( get_equation_code("/tmp/sample.svg"))
        


