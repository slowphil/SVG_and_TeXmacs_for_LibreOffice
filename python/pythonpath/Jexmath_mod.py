#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
This module is used by Jexmt_mod, See docstring there.

*********************************************************

This software falls under the GNU general public license version 2.
It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
in the root directory or <http://www.gnu.org/licenses/gpl-2.0.html>.

*********************************************************
"""
__author__ = "Philippe Joyez"
__credits__ = ["David K. Levine"]
__license__ = "GPL v2"

from collections import deque
from Jexfont_mod import *
from Jextex_mod import *

class LinkedList(deque):

    def __init__(self):
      super(LinkedList, self).__init__()

    def add(self, i, j = None):
      if j== None :
          return self.append(i)
      else :
          self.rotate(-i)
          o = self.appendleft(j)
          self.rotate(i)
          return o

    def addAll(self, j):
      for elem in j :
          self.append(elem)
      return true
        
    def get(self, j):
      return self[j]

    def getLast(self):
      return self[-1]

    def removeLast(self):
      if len(self) > 0 :
        return self.pop()
      else :
        return EmptyBox()

    def remove(self, j):
      self.rotate(-j)
      o = self.popleft()
      self.rotate(j)
      return o

    
# the linked list is a linked list of integers representing an index into a mathbox
# that is a collection of other mathboxes
class Selection(LinkedList):
    """ generated source for class Selection """

    def __init__(self):
        self.width = int()
        self.old = None
        self.maxWidth = 1000

    def pop(self, d):
        """ generated source for method pop """
        d.sel = d.sel.old

    def push(self, d):
        """ generated source for method push """
        s = Selection()
        s.width = self.width
        s.old = self
        d.sel = s

    def dup(self, d):
        """ generated source for method dup """
        self.push(d)
        d.sel.addAll(self)
        d.sel.width = self.width

    def empty(self, d):
        """ generated source for method empty """
        self.push(d)
        d.sel.old = None

    #@overloaded
    def add(self, j):
        """ generated source for method add """
        return self.add(int(j))

    #@add.register(object, int, int)
    def add_0(self, i, j):
        """ generated source for method add_0 """
        self.add(i, int(j))

    def getInt(self, i):
        """ generated source for method getInt """
        ii = int(get(i))
        return ii.intValue()

    def getLastInt(self):
        """ generated source for method getLastInt """
        ii = int(getLast())
        return ii.intValue()

    def removeInt(self, i):
        """ generated source for method removeInt """
        ii = int(remove(i))
        return ii.intValue()

    def removeLastInt(self):
        """ generated source for method removeLastInt """
        ii = int(removeLast())
        return ii.intValue()

    def setWidth(self, d):
        """ generated source for method setWidth """
        start = self.old
        stop = self
        minSize = min(len(start), len(stop))
        if minSize == 0:
            self.old.width = 0
            d.sel = self.old
            return
        ci = len(start) - 2
        jj = 0
        kk = 0
        i = int()
        while i < minSize:
            jj = start.getInt(i)
            kk = stop.getInt(i)
            if jj != kk:
                break
            i += 1
        if i == ci + 2:
            self.old.width = 0
            d.sel = self.old
            return
        if i == ci + 1:
            jj = start.getInt(ci + 1)
            kk = stop.getInt(ci + 1)
            self.old.width = kk - jj
            d.sel = self.old
            return
        if kk > jj:
            self.old.width = self.maxWidth
        else:
            self.old.width = -self.maxWidth
        d.sel = self.old

    def normalize(self, d):
        """ generated source for method normalize """
        self.dup(d)
        top = d.sel
        if size() == 0:
            return
        if self.width >= 0:
            return
        sw = self.width
        ibot = top.removeLastInt()
        newbot = ibot + sw
        sw = -sw
        if newbot <= 1:
            sw = sw + newbot - 1
            newbot = 1
        top.width = sw
        top.add(newbot)
        return


mFontPLAIN = 0
mFontITALIC = 2
mFontBOLD = 1



class mColor(object):
    """ generated source for class mColor """

    def __init__(self, r, g, b):
        """ generated source for method __init__ """
        if isinstance(r, int) :
            self.r = r
        else :
            self.r = int((255 * r))
        if isinstance(g, int) :
            self.g = g
        else :
            self.g = int((255 * g))
        if isinstance(b, int) :
            self.b = b
        else :
            self.b = int((255 * b))
mColorred = mColor(255, 0, 0)
mColorblack = mColor(0, 0, 0)
mColorwhite = mColor(255, 255, 255)
mColordarkGray = mColor(64, 64, 64)
mColorlightGray = mColor(192, 192, 192)
      
class DefaultContext(object):
    """ generated source for class DefaultContext """
    eqn = None
    sel = Selection()

    # public Graphics2D g = null;
    #g = mGraphics(None)
    md = None
    mf = None
    undoMe = LinkedList()
    redoMe = LinkedList()
    caretColor = mColorred
    defFontColor = mColorblack
    fontColor = defFontColor
    highColor = mColorwhite
    backHighColor = mColordarkGray
    x = int()
    y = int()
    copyonly = False
    printeq = False
    mathrm = False
    dirty = False
    size = int()
    binding = Jexfont().editBinding
    italicAngleFactor = float(0.5)
    emptyPad = float(0.2)
    defSlantf = 0.35
    slantf = defSlantf
    hPad = float(0.2)
    showEmpty = True
    showPhantom = True
    maxSelWidth = 200
    defSupf = float(0.75)
    defSubf = float(0.55)
    defDscale = float(0.7)
    defPad = float(0.08)
    defPrepad = float(0.05)
    supf = defSupf
    subf = defSubf
    dscale = defDscale
    pad = defPad
    prepad = defPrepad
    red = 0.55
    green = 0.99
    blue = 0.80
    highlightLevels = False
    matrix = None
    matrixRow = 0
    matrixCol = 0
    z = int()



class MathBox(object):
    """ generated source for class MathBox """

    def __init__(self):
        self.isHighlight = False
        self.boxMetrics = None
        self.buildState = "closed"
        self.lang = "tex"
        self.te = None


    def isRow(self):
        """ generated source for method isRow """
        return False

    def isEmpty(self):
        """ generated source for method isEmpty """
        return False


    def toTex(self):
        """ generated source for method toTex """
        raise NotImplementedError("Please Implement this method")

    def wrapBox(self, m):
        """ generated source for method wrapBox """
        if m == None:
            m = EmptyBox()
        if m.isRow():
            return m
        rb = RowBox()
        rb.addChild(m)
        return rb

class LayoutBox(MathBox):

    def __init__(self):
        super(LayoutBox, self).__init__()
        self.c = LinkedList()


    def isEmpty(self):
        """ generated source for method isEmpty """
        if len(self.c) == 1:
            c0 = self.c.get(0)
            if c0.isEmpty():
                return True
        return False

    def addChild(self, mbox):
        """ generated source for method addChild """
        self.c.add(mbox)


class RowBox(LayoutBox):

    """ generated source for class RowBox """

    def __init__(self):
        self.c = LinkedList()
        self.dc = None
        self.pBox = None
        self.bMathrm = False
        self.color = colorstack[-1]
    #pBox = None
    #bMathrm = False


    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        #if (copen != "") :
            #x = copen
        #else :
            #x = "{"
        x = "{" + copen
        for mb in self.c :
            x = x + mb.toTex()

        #x = x + "}"
        x = x + cclose + "}"
        if copen != "": x = x + popcolor()
        return x

class SubSupBox(LayoutBox):
    global colorstack

    """ generated source for class SubSupBox """
    #supf = DefaultContext.defSupf
    #subf = DefaultContext.defSubf
    #dscale = DefaultContext.defDscale
    #pad = DefaultContext.defPad
    #prepad = DefaultContext.defPrepad
    #slantf = DefaultContext.defSlantf

    #@overloaded
    def __init__(self, m0 = None, m1 = None, m2 = None):
        """ generated source for method __init__ """
        super(SubSupBox, self).__init__()
        if (m0 != None) & (m1 != None) & (m2 != None):
            self.addChild(self.wrapBox(m0))
            self.addChild(self.wrapBox(m1))
            self.addChild(self.wrapBox(m2))
        #self.initSubSup()
        global colorstack
        self.color = colorstack[-1]        

    #def initSubSup(self):
        #""" generated source for method initSubSup """
        #if self.te != None:
            #if self.te.dc != None:
                #self.supf = self.te.dc.supf
                #self.subf = self.te.dc.subf
                #self.dscale = self.te.dc.dscale
                #self.pad = self.te.dc.pad
                #self.prepad = self.te.dc.prepad
                #self.slantf = self.te.dc.slantf

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        m1 = self.c.get(1)
        m2 = self.c.get(2)
        mainslot = m0.toTex()
        
        #particular cases when we (ab)used subsup for under/overbrace construct
        if mainslot == chr(65080) : #underbace 65080 : ︸
            x = copen + "\\underbrace{"+m1.toTex()+"}_" + m2.toTex() + cclose
        elif mainslot == chr(65079) : #overbace 65079 : ︷
            x = copen + "\\overbrace{"+m1.toTex()+"}^" + m2.toTex() + cclose
        elif mainslot == chr(65096) : #underbace ﹈
            x = copen + "\\underbrace{"+m1.toTex()+"}_" + m2.toTex() + cclose
        elif mainslot == chr(65095) : #overbace ﹇
            x = copen + "\\overbrace{"+m1.toTex()+"}^" + m2.toTex() + cclose

        else : #more general case
            if m1.isEmpty() :
                sub = ""
            else :
                sub = "_" + m1.toTex()
            if m2.isEmpty() :
                sup = ""
            else :
                sup = "^" + m2.toTex()
            # recognizing sum,int,prod...
            if mainslot == "{∑}" : mainslot = "\\sum"
            elif mainslot == "{"+chr(8747)+"}" : mainslot = "\\int"
            elif mainslot == "{"+chr(8745)+"}" : mainslot = "\\bigcap"
            elif mainslot == "{"+chr(8746)+"}" : mainslot = "\\bigcup"
            elif mainslot == "{"+chr(8719)+"}" : mainslot = "\\prod"

            x = copen + mainslot + sub + sup + cclose
            
        if copen != "": x = x + popcolor()
        return x


class FenceBox(LayoutBox):
    """ generated source for class FenceBox """
    #@overloaded
    def __init__(self, m0 = None, m1 = None , m2 = None, m3 = None, m4 = None):
        """ generated source for method __init__ """
        super(FenceBox, self).__init__()
        if (m0 != None) & (m1 != None) & (m2 != None):
            self.addChild(self.wrapBox(m0))
            self.addChild(self.wrapBox(m1))
            self.addChild(self.wrapBox(m2))
        if (m3 != None)  & (m4 != None): # it's a dirac braket
            self.addChild(self.wrapBox(m3))
            self.addChild(self.wrapBox(m4))
        print ("len self.c =",len (self.c),"  ",m3,"  ",m4)
        self.color = colorstack[-1]

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        m1 = self.c.get(1)
        m2 = self.c.get(2)
        if len(self.c) == 3 :
            left = m0.toTex()
            if m0.isEmpty():
                left = "."
            right = m2.toTex()
            if m2.isEmpty():
                right = "."
            x = Jextex.texMacro("\\leftgrp" + left) + " " + m1.toTex() + " "
            x = x + Jextex.texMacro("\\rightgrp" + right) + " "
        else :
            m3 = self.c.get(3)
            m4 = self.c.get(4)
            left = m0.toTex()
            mid = m2.toTex()
            right = m4.toTex()
            if m0.isEmpty() or m4.isEmpty() :
                if m0.isEmpty():
                    x =  Jextex.texMacro("\\leftgrp" +mid) + m3.toTex() + Jextex.texMacro("\\rightgrp" + right)
                if m4.isEmpty():
                    x = Jextex.texMacro("\\leftgrp" +left) + m1.toTex() + Jextex.texMacro("\\rightgrp" + mid)
            else :
                x = Jextex.texMacro("\\leftgrp" + left) + m1.toTex() 
                x = x + mid + m3.toTex() + Jextex.texMacro("\\rightgrp" + right)
        x = copen + x + cclose
        if copen != "": x = x + popcolor()
        return x
           

class OverBox(LayoutBox):
    """ generated source for class OverBox """
    #@overloaded
    def __init__(self, m0 = None, m1 = None ):
        """ generated source for method __init__ """
        super(OverBox, self).__init__()
        if (m0 != None) & (m1 != None):
            self.addChild(self.wrapBox(m0))
            self.addChild(self.wrapBox(m1))
        self.color = colorstack[-1]
        
    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        m1 = self.c.get(1)
        x = copen +" " + Jextex.texMacro("\\overset" + m1.toTex()) + m0.toTex() + cclose
        if copen != "": x = x + popcolor()
        return x

class EmbellBox(LayoutBox):
    def __init__(self, m0 = None, typ = None ):
        """ generated source for method __init__ """
        super(EmbellBox, self).__init__()
        self.addChild(m0)
        self.typ=typ
        self.color = colorstack[-1]

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        y = m0.toTex()
        if self.typ == 2 :
            x = x + "\\dot{"+y + "}"
        elif self.typ == 3 :
            x = "\\ddot{"+y + "}"
        elif self.typ == 4 :
            x = "\\dddot{" + y + "}"
        elif self.typ == 5 :
            x = y + "'"
        elif self.typ == 6 :
            x = y + "''"
        elif self.typ == 7 :
            x = "{\\backprime}" + x
        elif self.typ == 8 :
            x = "\\tilde{" + y + "}"
        elif self.typ == 9 :
            x = "\\hat{" + y + "}"
        elif self.typ == 11 :
            x = "\\vec{" + y + "}" 
            #x = "\\overrightarrow{" + y + "}" 
        elif self.typ == 17 :
            x = "\\bar{" + y + "}"
        elif self.typ == 29 :
            x = "\\underline{" + y + "}"
        else :
            x = y+"??"
        x = copen + x + cclose
        if copen != "": x = x + popcolor()
        return x


class UnderBox(OverBox):
    """ generated source for class UnderBox """
    #@overloaded
    def __init__(self, m0 = None, m1 = None ):
        """ generated source for method __init__ """
        super(UnderBox, self).__init__()
        if (m0 != None) & (m1 != None):
            self.addChild(self.wrapBox(m0))
            self.addChild(self.wrapBox(m1))
        self.color = colorstack[-1]

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        m1 = self.c.get(1)
        x = copen +" " + Jextex.texMacro("\\underset" + m1.toTex()) + m0.toTex() + cclose
        if copen != "": x = x + popcolor()
        return x

class DivisionBox(LayoutBox):
    """ generated source for class DivisionBox """
    #@overloaded
    def __init__(self, m0 = None, m1= None, m2 = None ):
        """ generated source for method __init__ """
        super(DivisionBox, self).__init__()
        if (m0 != None) & (m2 != None) :
            self.addChild(self.wrapBox(m0))
            if m1 == None :
                pass
                #self.addChild(self.wrapBox(CharBox(45))) #FIXME ???
            else :
                self.addChild(self.wrapBox(m1))
            self.addChild(self.wrapBox(m2))
        self.color = colorstack[-1]

    divLev = int()

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        if len(self.c) == 2 :
            m0 = self.c.get(0)
            m2 = self.c.get(1)
            x = " \\frac" + m0.toTex() + "" + m2.toTex() + ""
        else:
            m0 = self.c.get(0)
            m1 = self.c.get(1)
            m2 = self.c.get(2)
            x = " {" + m0.toTex() +  m1.toTex() + m2.toTex() + "} "
        x = copen + x + cclose
        if copen != "": x = x + popcolor()
        return x

class SqrtBox(LayoutBox):
    global colorstack

    """ generated source for class SqrtBox """
    #@overloaded
    def __init__(self, m0 = None):
        """ generated source for method __init__ """
        super(SqrtBox, self).__init__()
        if m0 != None :
            self.addChild(self.wrapBox(CharBox(0x221a)))
            self.addChild(self.wrapBox(m0))
        global colorstack
        self.color = colorstack[-1]

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        rb = self.c.get(1)
        x = copen+"\\sqrt {" + rb.toTex() + "}"+cclose
        if copen != "": x = x + popcolor()
        return x

class RootBox(LayoutBox):
    """ generated source for class RootBox """
    #@overloaded
    def __init__(self, m0 = None, m1 = None):
        """ generated source for method __init__ """
        super(RootBox, self).__init__()
        if ( m0 != None) & ( m1 != None) :
            self.addChild(self.wrapBox(m0))
            self.addChild(self.wrapBox(m1))
        global colorstack
        self.color = colorstack[-1]

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        m0 = self.c.get(0)
        m1 = self.c.get(1)
        x = copen +" \\sqrt[" + m0.toTex() + "]" + m1.toTex() + " " +cclose
        if copen != "": x = x + popcolor()
        return x

class MatrixBox(LayoutBox):
    """ generated source for class MatrixBox """
    rows = int()
    cols = int()
    halign = LinkedList()
    spacef = 1.0
    leadf = 1.0
    valign = "b"
    defHalign = "l"
    texType = "array"

    #@overloaded
    def __init__(self, mb0 = None , mb1 = None , mb2 = None , mb3 = None):
        """ generated source for method __init__ """
        super(MatrixBox, self).__init__()
        self.color = colorstack[-1]
        if (mb2 is None) & (mb3 is None) & isinstance( mb0, int ) &  isinstance( mb1, int ):
            i = mb0
            j = mb1
            self.rows = i
            self.cols = j
            ii = 0
            while ii < self.rows:
                jj = 0
                while jj < self.cols:
                    self.addChild(self.wrapBox(EmptyBox()))
                    jj += 1
                ii += 1
            self.setHalign()
        if isinstance( mb0, RowBox ) & isinstance( mb0, RowBox ) & isinstance( mb0, RowBox ) &  isinstance( mb1, RowBox ):
            self.rows = 2
            self.cols = 2
            self.halign.add("r")
            self.halign.add("l")
            addChild(mb0)
            addChild(mb1)
            addChild(mb2)
            addChild(mb3)
            self.texType = "align"
            self.spacef = 0.0
            self.leadf = 0.0

    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        
        texTypez = self.texType
        if texTypez == "align":
            texTypez = "align*"
        x = "\\begin{" + texTypez + "} "
        if self.texType == "array":
            x = x + "[" + self.valign + "] "
        if self.texType == "array":
            x = x + "{"
            ii = 0
            while ii < self.cols:
                x = x + self.halign.get(ii)
                ii += 1
            x = x + "} "
        ii = 0
        while ii < self.rows:
            jj = 0
            while jj < self.cols:
                mb = self.c.get((ii * self.cols) + jj)
                x = x + mb.toTex()
                if jj < self.cols - 1:
                    x = x + " &  "
                jj += 1
            if ii < self.rows - 1:
                x = x + " \\\\ "
            ii += 1
        x = copen + x + "\\end{" + texTypez + "}" +cclose
        if copen != "": x = x + popcolor()
        return x


    colct = int()

class CharBox(MathBox):
    """ generated source for class CharBox """
    def __init__(self, token = None):
        """ generated source for method __init__ """
        super(CharBox, self).__init__()
        self.flux = float(0.3)
        self.f = None
        self.c = None
        self.thin = float()
        self.jf = None
        self.lpad = int()
        self.jfstyle = "math"
        self.vshift = int()
        self.size = int()
        self.stretch = float()
        self.ratio = float()
        self.color = colorstack[-1]

        if token != None :
            self.jf = Jexfont(token)
            self.c = DefaultContext.defFontColor
            if self.te != None:
                if self.te.dc != None:
                    self.c = self.te.dc.fontColor


    def toTex(self):
        copen, cclose =  checkcolor(self.color)
        """ generated source for method toTex """
        self.jf.JexStyle(self.jfstyle)
        x = copen + self.jf.texString +cclose
        if copen != "": x = x + popcolor()
        return x

class SpaceBox(CharBox):
    """ generated source for class SpaceBox """
    sbwidth = 1.0
    texString = "\\,"
    jfstyle = "math"
    c = None
    jf = None

    def __init__(self, texString):
        """ generated source for method __init__ """
        super(SpaceBox, self).__init__()
        self.texString = texString
        if texString == "\\,":
            self.sbwidth = 0.5
        if texString == "\\:":
            self.sbwidth = 1.0
        if texString == "\\;":
            self.sbwidth = 1.5
        self.jf = Jexfont(32)
        self.color = colorstack[-1]


    def toTex(self):
        """ generated source for method toTex """
        copen, cclose =  checkcolor(self.color)
        return copen + self.texString + cclose


colorlist=[["000000", 'black']]    #default (index 0) if black, newly defined have indices >=1 in order they are defined
colorstack = [0]

   
def popcolor() :
     oldcol = colorstack.pop()
     if len(colorstack) == 1 :
        return ""# "\\color{black}"
        #return "\\color{black}"
     else :
        return ""
      

def checkcolor(col) :
    if colorstack[-1] != col :
        colorstack.append(col)
        colstring, name = colorlist[col]
        return ["{\\color[HTML]{"+ colstring + "}", "}"]
        #return [" \\color[HTML]{"+ colstring + "} ", " "]
    else :
        return ["", ""]


class EmptyBox(MathBox):
    """ generated source for class EmptyBox """
    def __init__(self, signal = None):
        """ generated source for method __init___0 """
        super(EmptyBox, self).__init__()
        self.c = mColorlightGray
        self.signal = signal
        self.stretch = float()
        self.color = colorstack[-1]

    
    def isEmpty(self):
        """ generated source for method isEmpty """
        return True

    def toTex(self):
        """ generated source for method toTex """
        return "{}"


        
