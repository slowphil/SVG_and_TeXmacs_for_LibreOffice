#!/usr/bin/env python
"""
*******************************************************************************
* Texmacs extension for LibreOffice/openOffice
* COPYRIGHT  : (C) 2017 Philippe JOYEZ and the TeXmacs team
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

"""
#------------------------------------------------------------------------------

import os, glob, platform, time
import tempfile, subprocess
from xml.etree import ElementTree as etree

import socket

IS_WINDOWS = (platform.system() == "Windows")
#IS_MACOS= sys.platform.startswith('darwin')

if IS_WINDOWS :
    def Is64Windows():
        return 'PROGRAMFILES(X86)' in os.environ

    def GetProgramFiles32():
        if Is64Windows():
            return os.environ['PROGRAMFILES(X86)']
        else:
            return os.environ['PROGRAMFILES']

    texmacs_path = os.path.join(GetProgramFiles32(), 'TeXmacs','bin', 'texmacs.exe')
    if not(os.path.isfile(texmacs_path)):
        print("TeXmacs not found in the usual location:\n"+texmacs_path+"\nCannot continue, sorry.")
        raise SystemExit()

else : texmacs_path ='texmacs' #texmacs needs to be in the path!

import codecs        
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
TEXMACS_NS = u"http://www.texmacs.org/"
SVG_NS = u"http://www.w3.org/2000/svg"


tm_file="<TeXmacs|1.99.5>\n\n<style|generic>\n\n<\\body>\n %s \n\n</body>\n\n<\\initial>\n %s \n\n</initial>"
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


def tm_equation(latex_code, svg_file, tm_equation, tm_style):
    """Perform the effect: create/modify embedded equation"""
    latex_code = latex_code.replace("\\","\\\\")
    if svg_file != '' :
        # Find equation and how to modify it
        latex_code, tm_equation, tm_style = get_equation_code(svg_file)
        scheme_cmd = tm_scheme_cmd_line_args % ''
    elif tm_equation != "" :
        tm_equation = string_unescape(tm_equation)
        tm_style = string_unescape(tm_style)
        scheme_cmd = tm_scheme_cmd_line_args % ''
    elif latex_code == '' :
        tm_equation, tm_style = (tm_dummy_equation, tm_no_style)
        scheme_cmd = tm_scheme_cmd_line_args % ''
    else :
        tm_equation, tm_style = (tm_no_equation, tm_no_style)
        # build full scheme command line command
        scheme_cmd = tm_scheme_cmd_line_args % (tm_extra_latex_cmd_line_args % latex_code)
       
    # call texmacs for editing
    svg_name = tmp_name + ".svg" #if successful texmacs creates that svg file
    try_remove(svg_name)
    call_texmacs(scheme_cmd, tm_equation, tm_style, latex_code)
    try_remove(tmp_name)
    if os.path.isfile(svg_name):
        return svg_name
    else :
        return ""

def get_equation_code(svg_name):
    """retrieve texmacs code for embedded equation"""
    f = open(svg_name, 'r')
    tree = etree.parse(f)
    f.close()
    #inkex.debug("file read  "+svg_name)
    root = tree.getroot()
    node = root.find('{%s}g' % SVG_NS) #by construction the equation is in the first group 
    if node is None :
        return ('', tm_dummy_equation, tm_no_style)
    elif '{%s}texmacscode'%TEXMACS_NS in node.attrib: # that group contains texmacs data
        
        tm_equation = string_unescape(node.attrib.get('{%s}texmacscode' % TEXMACS_NS, ''))
        if '{%s}texmacsstyle'%TEXMACS_NS in node.attrib: #further contains styling info
            tm_style = string_unescape(node.attrib.get('{%s}texmacsstyle' % TEXMACS_NS, ''))
        else:
            tm_style =''
        return ('', tm_equation, tm_style)

    elif '{%s}text'%TEXTEXT_NS in node.attrib:  #implements Textext conversion to TeXmacs
        latex_code = node.attrib.get('{%s}text' % TEXTEXT_NS, '')
        return (latex_code, tm_no_equation, tm_no_style)


def call_texmacs(scheme_cmd, equ, styl, latex):
    f_tmp = open(tmp_name, 'wb') # create a temporaty tm file that texmacs will edit
    try:
        f_tmp.write((tm_file %( equ, styl)).encode("iso-8859-1")) #insert equation to be edited in file (blank in textext case)
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
#            inkex.debug("recvd: " + str(len(data)) + " bytes")
#            inkex.debug("recvd:" + data)
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
                print("Error in creating Named Pipe")
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
                print("Could not connect with "+texmacs_path+"\n using named pipe")
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
                    print("error reading from named pipe")
                    break
                
            ctypes.windll.kernel32.FlushFileBuffers(hPipe)
            ctypes.windll.kernel32.DisconnectNamedPipe(hPipe)
            ctypes.windll.kernel32.CloseHandle(hPipe)

        else : # Linux, MacOS: so much simpler!
            cmd = [texmacs_path,"-x",scheme_cmd , tmp_name]
        #try:
            p = subprocess.Popen(cmd, 
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
            while p.poll() is None:
                output = p.stdout.readline()
                if ((b"done" in output) or (b"cancel" in output) ):
                    break
        #except OSError as e:
        #    raise RuntimeError("Command %s failed: %s" % (' '.join(cmd), e))
        #except :
            #inkex.debug("launching texmacs failed   ")
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

g_exportedScripts = tm_equation,

if __name__ == u'__main__':
    tm_equation("", "/tmp/test.svg", "", "")
    #tm_equation(r"\frac{a}{b}", "", "", "")
    

