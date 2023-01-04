#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This code can put and get arbitrary content on windows clipboard.
It is used in particular to communicate svg drawings to and from 
LibreOffice.

************************************************
Why this code?

On windows, in LO 5 (but I suspect it has always been so), 
com.sun.star.datatransfer.clipboard.SystemClipboard 
only accepts standard (= windows predefined) datatypes.
Obviously, this is a bug.

The bad thing is that "image/svg+xml" is not considered a standard type,
so we cannot transfer svg over the clipboard using the standard LO API !

We work around this issue by accessing the clipboard through python,
talking directly with the OS. We need no module other than the standard
ones coming with LO's python.

**************************************************

The code is based on http://stackoverflow.com/a/25678113,

It is licensed under CC BY-SA 3.0

See the terms of this license at
https://creativecommons.org/licenses/by-sa/3.0/

'''
__author__ = "Philippe Joyez"
__credits__ = ["Mark Ransom"]
__license__ = "CC BY-SA 3.0"


import ctypes


from ctypes.wintypes import BOOL, HWND, HANDLE, HGLOBAL, UINT, LPVOID, LPSTR, LPCWSTR
from ctypes import c_int as int
from ctypes import c_size_t as SIZE_T

OpenClipboard = ctypes.windll.user32.OpenClipboard
OpenClipboard.argtypes = HWND,
OpenClipboard.restype = BOOL
EmptyClipboard = ctypes.windll.user32.EmptyClipboard
EmptyClipboard.restype = BOOL
GetClipboardData = ctypes.windll.user32.GetClipboardData
GetClipboardData.argtypes = UINT,
GetClipboardData.restype = HANDLE
SetClipboardData = ctypes.windll.user32.SetClipboardData
SetClipboardData.argtypes = UINT, HANDLE
SetClipboardData.restype = HANDLE
CloseClipboard = ctypes.windll.user32.CloseClipboard
CloseClipboard.restype = BOOL

CountClipboardFormats = ctypes.windll.user32.CountClipboardFormats
CountClipboardFormats.restype = int
EnumClipboardFormats = ctypes.windll.user32.EnumClipboardFormats
EnumClipboardFormats.argtypes = UINT,
EnumClipboardFormats.restype = UINT

GetClipboardFormatName = ctypes.windll.user32.GetClipboardFormatNameA
GetClipboardFormatName.argtypes = UINT, LPSTR, int
GetClipboardFormatName.restypes = int

RegisterClipboardFormat = ctypes.windll.user32.RegisterClipboardFormatW
RegisterClipboardFormat.argtypes = LPCWSTR, 
RegisterClipboardFormat.restypes = UINT
CF_UNICODETEXT = 13

GlobalAlloc = ctypes.windll.kernel32.GlobalAlloc
GlobalAlloc.argtypes = UINT, SIZE_T
GlobalAlloc.restype = HGLOBAL
GlobalLock = ctypes.windll.kernel32.GlobalLock
GlobalLock.argtypes = HGLOBAL,
GlobalLock.restype = LPVOID
GlobalUnlock = ctypes.windll.kernel32.GlobalUnlock
GlobalUnlock.argtypes = HGLOBAL,
GlobalSize = ctypes.windll.kernel32.GlobalSize
GlobalSize.argtypes = HGLOBAL,
GlobalSize.restype = SIZE_T

GMEM_MOVEABLE = 0x0002
GMEM_ZEROINIT = 0x0040

unicode_type = type(u'')

def get():
    text = None
    OpenClipboard(None)
    handle = GetClipboardData(CF_UNICODETEXT)
    pcontents = GlobalLock(handle)
    size = GlobalSize(handle)
    if pcontents and size:
        raw_data = ctypes.create_string_buffer(size)
        ctypes.memmove(raw_data, pcontents, size)
        text = raw_data.raw.decode('utf-16le').rstrip(u'\0')
    GlobalUnlock(handle)
    CloseClipboard()
    return text

def put(s):
    if not isinstance(s, unicode_type):
        s = s.decode('mbcs')
    data = s.encode('utf-16le')
    OpenClipboard(None)
    EmptyClipboard()
    handle = GlobalAlloc(GMEM_MOVEABLE | GMEM_ZEROINIT, len(data) + 2)
    pcontents = GlobalLock(handle)
    ctypes.memmove(pcontents, data, len(data))
    GlobalUnlock(handle)
    SetClipboardData(CF_UNICODETEXT, handle)
    CloseClipboard()

paste = get
copy = put
def getformatname(format):
    buffer = bytes(" "*100,"ascii")
    bufferSize = len(buffer)
    OpenClipboard(0)
    ret = GetClipboardFormatName(format, buffer, bufferSize)
    CloseClipboard()
    if ret == 0 : return "predefined"
    return buffer.decode('ascii').split("\0")[0]


def enum():
    OpenClipboard(0)
    print(CountClipboardFormats())
    q = EnumClipboardFormats(0)
    l = [q]    
    while q:
        q = EnumClipboardFormats(q)
        l.append(q)
    CloseClipboard()
    for q in l :
        print(q," ",getformatname(q))
        
def getclipboardtype(mimetypelist, outfile): 
#mimetypelist is a list where each element is EITHER a string defining the mimetype OR an int for predefined types in Windows
# sorted in order of preference (first is prefered)
    success = False
    OpenClipboard(0)
    if CountClipboardFormats() != 0 :
        datatype = EnumClipboardFormats(0)
        while datatype:
            if datatype in mimetypelist : 
                break
            else :
                buffer = bytes(" "*100,"ascii")
                bufferSize = len(buffer)
                if GetClipboardFormatName(datatype, buffer, bufferSize) != 0 :
                # ret == 0 means a windows predefined format
                    mime = buffer.decode('ascii').split("\0")[0]
                    if (mime in mimetypelist) :
                        break
            datatype = EnumClipboardFormats(datatype)
        if datatype != 0 :
            handle = GetClipboardData(datatype)
            pcontents = GlobalLock(handle)
            size = GlobalSize(handle)
            if pcontents and size:
                raw_data = ctypes.create_string_buffer(size)
                ctypes.memmove(raw_data, pcontents, size)
                #text = raw_data.raw.decode('utf-8').rstrip(u'\0')
            GlobalUnlock(handle)
            out_file = open(outfile, "wb") # open for [w]riting as [b]inary
            out_file.write(raw_data)
            out_file.close()
            success =  True
    CloseClipboard()
    return success

def putonclipboard(mimestring, data): 
    typeno = RegisterClipboardFormat(mimestring)
    if typeno :
        data = bytes(b for b in data)
        #return str (type(data))+str(data)
        OpenClipboard(None)
        EmptyClipboard()
        handle = GlobalAlloc(GMEM_MOVEABLE | GMEM_ZEROINIT, len(data) + 2)
        pcontents = GlobalLock(handle)
        ctypes.memmove(pcontents, data, len(data))
        GlobalUnlock(handle)
        SetClipboardData(typeno, handle)
        CloseClipboard()
        
if __name__ == u'__main__':
    enum()
    print (getclipboardtype(['image/svg+xml'],"G:/phil/temp/test.svg"))
    #put("toto")
    #putonclipboard('image/svg+xml', bytes("not really svg there","utf-8"))


g_exportedScripts = getclipboardtype, putonclipboard
