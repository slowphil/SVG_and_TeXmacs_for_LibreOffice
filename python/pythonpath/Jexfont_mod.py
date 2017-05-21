#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

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

""" generated source for module Jexfont """
#from Jexmath_mod import *
mFontPLAIN = 0
mFontITALIC = 2
mFontBOLD = 1


# package: jex
class Jexbinding(object):
    """ generated source for class Jexbinding """
    def __init__(self):
        self.dface = None
        self.gface = None
        self.Gface = None
        self.sface = None
        self.uniSym = None
        self.uniFac = None
        self.unigrk = None
        self.uniGrk = None
        self.uniArk = None
        self.svpad = 0
        self.gvpad = 0
        self.Gvpad = 0
        self.aftr = 0
        self.sfixangle = 0
        self.gfixangle = 0
        self.Gfixangle = 0
        self.srescale = 1.0
        self.vgrescale = 1.0
        self.Grescale = 1.0
        self.binpad = 0.0
        self.slpad = 0.1
        self.vsrpad = 0.2
        self.shpad = 0.2


class Jexfont(object):
    """ generated source for class Jexfont """
    def __init__(self, unichar = None):
        self.jbinding = None
        self.g = None
        self.mf = None
        self.esstix = None
        self.symbol = None
        self.euclid = None
        self.ooeuclid = None
        self.opensymbol = None
        self.jopensymbol = None
        self.printBinding = "ooeuclid"
        self.editBinding = ""
        self.printFace = None
        self.editFace = None
        self.mathItalic = True
        self.greekItalic = True
        self.unicode_ = False
        self.bindingList = ["esstix", "symbol", "euclid", "ooeuclid", "opensymbol", "jopensymbol"]
        self.uniSym = None
        self.uniFac = None
        self.unigrk = None
        self.uniGrk = None
        self.uniArk = None
        self.unichar = int()
        self.aschar = int()
        self.style = int()
        self.binary = 1
        self.face = None
        self.aftr = float()
        self.rescale = 1.0
        self.texString = None
        self.MMLString = None
        self.bpad = 0
        self.lpad = 0
        self.rpad = 0
        self.hpad = 0
        self.vpad = 0
        self.fixangle = 0
        self.d = None

        """ generated source for method init """
        self.esstix = Jexbinding()
        self.esstix.dface = str("Times New Roman")
        self.esstix.sface = [None] * 9
        self.esstix.gface = str("ESSTIXNine")
        self.esstix.Gface = str("ESSTIXTen")
        self.esstix.sface[0] = str("ESSTIXFour")
        self.esstix.sface[1] = str("ESSTIXOne")
        self.esstix.sface[2] = str("ESSTIXTwo")
        self.esstix.sface[3] = str("ESSTIXThree")
        self.esstix.sface[4] = str("ESSTIXFive")
        self.esstix.sface[5] = str("ESSTIXSix")
        self.esstix.sface[6] = str("ESSTIXNine")
        self.esstix.sface[7] = str("ESSTIXTen")
        self.esstix.sface[8] = str("ESSTIXFifteen")
        self.esstix.aftr = float(0.2)

        self.uniArk = dict([(0x3b1, 'A'),
                (0x3b2, 'B'),
                (0x3b5, 'E'),
                (0x3b6, 'Z'),                  
                (0x3b7, 'H'),
                (0x3b9, 'I'),
                (0x3ba, 'K'),
                (0x3bc, 'M'),
                (0x3bd, 'N'),
                (0x3bf, 'O'),
                (0x3c1, 'P'),
                (0x3c4, 'T'),
                (0x3c7,  'X')])
                
        self.uniFac = dict([(0x00b1, 4),
                (0x00b7, 4),
                (0x00d7, 4),
                (0x211c, 8),
                (0x2190, 1),
                (0x2192, 1),
                (0x2202, 6),
                (0x2205, 4),
                (0x2207, 7),
                (0x220f, 5),
                (0x2211, 5),
                (0x221d, 3),
                (0x221e, 3),
                (0x2229, 2), 
                (0x222a, 2),
                (0x222b, 5),
                (0x2264, 3),
                (0x2265, 3),
                (0x22c5, 4)])
                
        self.unigrk = dict([(0x3b1, 0x61),
                (0x3b2, 0x62),
                (0x3b3, 0x67),
                (0x3b4, 0x64),
                (0x3b5, 0x65),
                (0x3b6, 0x7a),   
                (0x3b7, 0x68), 
                (0x3b8, 0x71), 
                (0x3b9, 0x69),
                (0x3ba, 0x6b),
                (0x3bb, 0x6c),
                (0x3bc, 0x6d),
                (0x3bd, 0x6e),
                (0x3be, 0x78),
                (0x3bf, 0x6f),
                (0x3c0, 0x70),
                (0x3c1, 0x72),
                (0x3c3, 0x73),
                (0x3c4, 0x74),
                (0x3c5, 0x79),
                (0x3c6, 0x34), 
                (0x3c7, 0x63), 
                (0x3c8, 0x6a), 
                (0x3c9, 0x77), 
                (0x3d5, 0x66)])
                
        self.uniGrk = dict([(0x3b3, 0x47),
                (0x3b4, 0x44),
                (0x3b8, 0x51),
                (0x3bb, 0x4c),
                (0x3be, 0x58),
                (0x3c0, 0x50),
                (0x3c3, 0x53),
                (0x3c5, 0x59),
                (0x3c6, 0x46),
                (0x3c8, 0x4a),
                (0x3c9, 0x57)])
        
        self.uniSym = dict([(0x00b1, 0x47), #pm
                (0x00b7, 0x25), #bullet
                (0x00d7, 0x21), #times
                (0x2026, 0x2e), #ldots
                (0x211c, 0x52), #real
                (0x2190, 0x29), #leftarrow
                (0x2192, 0x2f), #rightarrow
                (0x2202, 0x76), #partial
                (0x2205, 0x5c), #emptyset 5b is script lowercase l
                (0x2207, 0x56), #grad
                (0x2208, 0x32), #in
                (0x2209, 0x3b), #notin
                (0x220b, 0x48), #ni
                (0x220f, 0x2e), #prod 3f is lighter
                (0x2211, 0x3e), #sum  3e is lighter 2d is heavier
                (0x221d, 0x66), #propto
                (0x221e, 0x4e), #infinity
                (0x2229, 0x68), #cap
                (0x222a, 0x67), #cup
                (0x222b, 0x21), #int 45 is more curly
                (0x2248, 0x7a), #approx
                (0x2260, 0x73), #neq
                (0x2261, 0x68), #equiv
                (0x2264, 0x25), #leq
                (0x2265, 0x52), #geq
                (0x2282, 0x33), #subset
                (0x2283, 0x49), #supset
                (0x2286, 0x34), #subseteq
                (0x2287, 0x4a), #supseteq
                (0x22c5, 0x24)]) #cdot 25 is larger dot 
        #unigrk = Hashtable()
        #uniGrk = Hashtable()
        #uniArk = Hashtable()
        #uniSym = Hashtable()
        #uniFac = Hashtable()
        self.esstix.unigrk = self.unigrk
        self.esstix.uniGrk = self.uniGrk
        self.esstix.uniArk = self.uniArk
        self.esstix.uniSym = self.uniSym
        self.esstix.uniFac = self.uniFac
        
        
        
        self.symbol = Jexbinding()
        self.euclid = Jexbinding()
        self.ooeuclid = Jexbinding()
        self.symbol.dface = str("Nimbus Roman")
        self.euclid.dface = str("Euclid")
        self.ooeuclid.dface = str("Euclid")
        self.symbol.sface = [None] * 3
        self.euclid.sface = [None] * 50
        self.ooeuclid.sface = [None] * 3
        self.symbol.gface = str("Symbol")
        self.euclid.gface = str("Euclid Symbol")
        self.ooeuclid.gface = str("Euclid Symbol")
        self.symbol.Gface = str("Symbol")
        self.euclid.Gface = str("Euclid Symbol")
        self.ooeuclid.Gface = str("Euclid Symbol")
        self.symbol.sface[0] = str("Symbol")
        self.symbol.sface[1] = str("Euclid Fraktur")
        self.symbol.sface[2] = str("Euclid Extra")
        self.euclid.sface[0] = str("Euclid Symbol")
        self.euclid.sface[1] = str("Euclid Fraktur")
        self.euclid.sface[2] = str("ESSTIXOne")
        self.euclid.sface[3] = str("ESSTIXFour")
        self.euclid.sface[4] = str("ESSTIXFive")
        self.ooeuclid.sface[0] = str("Euclid Symbol")
        self.ooeuclid.sface[1] = str("Euclid Fraktur")
        self.ooeuclid.sface[2] = str("Euclid Extra")
        self.ooeuclid.svpad = 0.31
        self.ooeuclid.gvpad = 0.05
        self.euclid.binpad = 0.3
        self.ooeuclid.binpad = 0.28
        self.euclid.srpad = 0.0
        self.ooeuclid.srpad = 0.0
        # euclid.grescale = 1.25f;
        # euclid.Grescale = euclid.grescale;
        # euclid.srescale = euclid.grescale;
        self.symbol.svpad = 0.18
        self.symbol.aftr = -0.2
        #unigrk = Hashtable()
        #uniGrk = Hashtable()
        #uniArk = Hashtable()
        #uniSym = Hashtable()
        #uniFac = Hashtable()
        self.uniArk = dict([(0x3b1, 'A'),
                (0x3b2 ,'B'),
                (0x3b5, 'E'),
                (0x3b6, 'Z'), 
                (0x3b7, 'H'),
                (0x3b9, 'I'),
                (0x3ba, 'K'),
                (0x3bc, 'M'),
                (0x3bd, 'N'),
                (0x3bf, 'O'),
                (0x3c1, 'P'),
                (0x3c4, 'T'),
                (0x3c7,  'X')])
        self.uniFac= dict([(0x2113, 1),
                (0x2113, 4),
                (0x220d, 3),
                (0xe090, 2)])
                #(0x220b, 3)
        self.unigrk= dict([(0x3b1, 0x61),
                (0x3b2, 0x62),
                (0x3b3, 0x67),
                (0x3b4, 0x64),
                (0x3b5, 0x65),
                (0x3b6, 0x7a),             
                (0x3b7, 0x68), 
                (0x3b8, 0x71), 
                (0x3b9, 0x69),
                (0x3ba, 0x6b),
                (0x3bb, 0x6c),
                (0x3bc, 0x6d),
                (0x3bd, 0x6e),
                (0x3be, 0x78),
                (0x3bf, 0x6f),
                (0x3c0, 0x70),
                (0x3c1, 0x72),
                (0x3c3, 0x73),
                (0x3c4, 0x74),
                (0x3c5, 0x79),
                (0x3c6, 0x6a), 
                (0x3c7, 0x63), 
                (0x3c8, 0x6a), 
                (0x3c9, 0x77), 
                (0x3d5, 0x66)])
                
        self.uniGrk= dict([(0x3b3, 0x47),
                (0x3b4, 0x44), 
                (0x3b8, 0x51),
                (0x3bb, 0x4c),
                (0x3be, 0x58),
                (0x3c0, 0x50),
                (0x3c3, 0x53),
                (0x3c5, 0x59),
                (0x3c6, 0x46),
                (0x3c8, 0x4a),
                (0x3c9, 0x57)])
        self.uniSym= dict([(0x00b1, 0xb1),
                (0x00b7, 0xb7),
                (0x2026, 0xbc),
                (0x2112, 0x3f), #upper script L
                (0x2113, 0x5b), #ell
                (0x2113, 0x6b), #lower script L
                (0x211c, 0xc2),
                (0x2190, 0xac),
                (0x2192, 0xae),
                (0x2202, 0xb6),
                (0x2205, 0xc6),
                (0x2207, 0xd1),
                (0x2208, 0xce),
                (0x2209, 0xcf),
                (0x220b, 0x27), #ni
                (0x220d, 0x48), #ni
                (0x220f, 0xd5),
                (0x2211, 0xe5),
                (0x221a, 0xd6), #square root	
                (0x221d, 0xb5),
                (0x221e, 0xa5),
                (0x2229, 0xc7),
                (0x222a, 0xc8),
                (0x222b, 0xf2),
                (0x2248, 0xbb),
                (0x2260, 0xb9),
                (0x2261, 0xba),
                (0x2264, 0xa3),
                (0x2265, 0xb3),
                (0x2282, 0xcc),
                (0x2283, 0xc9),
                (0x2286, 0xcd),
                (0x2287, 0xca),
                (0x22c5, 0xd7),
                (0xe090, 0x73)]) #norm
                #(0x220b, 0x48), #ni
                #(0xe090, 0x3f) #norm 
        self.symbol.unigrk = self.unigrk
        self.symbol.uniGrk = self.uniGrk
        self.symbol.uniArk = self.uniArk
        self.symbol.uniSym = self.uniSym
        self.symbol.uniFac = self.uniFac
        self.euclid.unigrk = self.unigrk
        self.euclid.uniGrk = self.uniGrk
        self.euclid.uniArk = self.uniArk
        self.euclid.uniSym = self.uniSym
        self.euclid.uniFac = self.uniFac
        self.ooeuclid.unigrk = self.unigrk
        self.ooeuclid.uniGrk = self.uniGrk
        self.ooeuclid.uniArk = self.uniArk
        self.ooeuclid.uniSym = self.uniSym
        self.ooeuclid.uniFac = self.uniFac
        self.opensymbol = Jexbinding()
        self.jopensymbol = Jexbinding()
        self.opensymbol.dface = str("Lucida Bright")
        self.opensymbol.sface = [None] * 2
        self.opensymbol.gface = str("OpenSymbol")
        self.opensymbol.Gface = str("OpenSymbol")
        self.opensymbol.sface[0] = str("OpenSymbol")
        self.opensymbol.sface[1] = str("Lucida Bright")
        self.opensymbol.gvpad = -0.03
        self.opensymbol.svpad = 0.18
        # opensymbol.aftr = (float) 0.1;
        self.opensymbol.gfixangle = float(0.2)
        self.jopensymbol.dface = str("Lucida Bright")
        self.jopensymbol.sface = [None] * 1
        self.jopensymbol.gface = str("OpenSymbol")
        self.jopensymbol.Gface = str("OpenSymbol")
        self.jopensymbol.sface[0] = str("OpenSymbol")
        # jopensymbol.gvpad = -0.03;
        # jopensymbol.svpad = 0.18;
        # jopensymbol.aftr = (float) 0.1;
        self.jopensymbol.gfixangle = float(0.2)
        #unigrk = Hashtable()
        #uniGrk = Hashtable()
        #uniArk = Hashtable()
        #uniSym = Hashtable()
        #uniFac = Hashtable()
        self.uniArk = dict([(0x3b1, 'A'),
                (0x3b2, 'B'),
                (0x3b5, 'E'), 
                (0x3b6, 'Z'), 
                (0x3b7, 'H'),
                (0x3b9, 'I'),
                (0x3ba, 'K'), 
                (0x3bc, 'M'),
                (0x3bd, 'N'),
                (0x3bf, 'O'),
                (0x3c1, 'P'),
                (0x3c4, 'T'),
                (0x3c7,  'X')])
        self.uniSym= dict()
        self.unigrk= dict([(0x3b1, 0xe0b7),
                (0x3b2, 0xe0b8),
                (0x3b3, 0xe0b9), 
                (0x3b4, 0xe0ba), 
                (0x3b5, 0xe0bb),
                (0x3b6, 0xe0bc),
                (0x3b7, 0xe0bd), 
                (0x3b8, 0xe0be), 
                (0x3b9, 0xe0bf), #iota
                (0x3ba, 0xe0c0),
                (0x3bb, 0xe0c1),
                (0x3bc, 0xe0c2),
                (0x3bd, 0xe0c3),
                (0x3be, 0xe0c4),
                (0x3bf, 0xe0c5),
                (0x3c0, 0xe0c6),
                (0x3c1, 0xe0c7),
                (0x3c3, 0xe0c8),
                (0x3c4, 0xe0c9),
                (0x3c5, 0xe0ca),
                (0x3c6, 0xe0d4), #varphi
                (0x3c7, 0xe0cc), 
                (0x3c8, 0xe0cd), 
                (0x3c9, 0xe0ce), 
                (0x3d5, 0xe0cb)]) #phi
                #(0x3b6, 0xe0d3)
        self.uniGrk= dict([(0x3b3, 0xe0ac), #gamma
                (0x3b4, 0xe0ad), #delta
                (0x3b8, 0xe0ae), #theta
                (0x3bb, 0xe0af), #lambda
                (0x3be, 0xe0b0), #xi
                (0x3c0, 0xe0b1), #pi
                (0x3c3, 0xe0b2), #sigma
                (0x3c5, 0xe0b3), #upsilon
                (0x3c6, 0xe0b4), #varphi
                (0x3c8, 0xe0b5), #psi
                (0x3c9, 0xe0b6), #omega
                (0x3d5, 0xe0b4)])#phi
        self.uniSym= dict([(0x00b1, 0x00b1),
                (0x00b7, 0x2022),
                (0x00d7, 0x00d7),
                (0x2026, 0x2026),
                (0x2112, 0x2112), #upper script L
                (0x2113, 0x2113), #lower script L
                (0x211c, 0x211c),
                (0x2190, 0x2190),
                (0x2192, 0x2192),
                (0x2202, 0x2202),
                (0x2205, 0x2205),
                (0x2207, 0x2207),
                (0x2208, 0x2208),
                (0x2209, 0x2209),
                (0x220b, 0x220b),
                (0x220f, 0x220f),
                (0x2211, 0x2211),
                (0x221d, 0x221d),
                (0x221e, 0x221e),
                (0x2229, 0x2229),
                (0x222a, 0x222a),
                (0x222b, 0x222b),
                (0x2248, 0x2248),
                (0x2260, 0x2260),
                (0x2261, 0x2261),
                (0x2264, 0x2264),
                (0x2265, 0x2265),
                (0x2282, 0x2282),
                (0x2283, 0x2283),
                (0x2286, 0x2286),
                (0x2287, 0x2287),
                (0x22c5, 0x22c5),
                (0xe090, 0xe090)]) #norm
        self.opensymbol.unigrk = self.unigrk
        self.opensymbol.uniGrk = self.uniGrk
        self.opensymbol.uniArk = self.uniArk
        self.opensymbol.uniSym = self.uniSym
        self.opensymbol.uniFac = self.uniFac
        self.jopensymbol.unigrk = self.unigrk
        self.jopensymbol.uniGrk = self.uniGrk
        self.jopensymbol.uniArk = self.uniArk
        self.jopensymbol.uniSym = self.uniSym
        self.jopensymbol.uniFac = self.uniFac
        self.jbinding = self.euclid
        self.editFace = "Euclid"
        self.printFace = "Euclid"

        if unichar != None :
            """ generated source for method __init__ """
            self.unichar = unichar
            #print("type of unichar :",str(type(unichar)))
            #FIXME should be either str OR int
            #if type(unichar) is str :
            #    unichar = ord(unichar)
            self.aschar = chr(unichar)
            self.texString = ""
            y = str(unichar)
            z = chr(unichar)
            if unichar >= 32 & unichar <= 126:
                self.texString = z
                self.MMLString = "<mi>" + z + "</mi>"
            else:
                self.MMLString = "<mi>" + "&#" + y + ";</mi>"
            if self.aschar == '{':
                self.texString = "\\{"
            if self.aschar == '}':
                self.texString = "\\}"
            if self.aschar == '^':
                self.texString = "\\^"
            if self.aschar == '_':
                self.texString = "\\_"
            if self.aschar == '~':
                self.texString = "\\~"
            if self.aschar == '&':
                self.texString = "\\&"
            if self.aschar == '\\':
                self.texString = "\\backslash"
            if self.aschar == '%':
                self.texString = "\\%"
            if self.aschar == '$':
                self.texString = "\\$"
            if self.aschar == '#':
                self.texString = "\\#"
            if self.aschar == '<':
                self.MMLString = "<mo>&lt;</mo>"
            if self.aschar == '>':
                self.MMLString = "<mo>&gt;</mo>"
            self.setBinding("")




    def setBinding(self, binding):
        """ generated source for method setBinding """
        self.d = self.euclid
        if binding == "":
            #self.d = Jexfont.jbinding
            self.d = self.jbinding
        if binding == "esstix":
            self.d = self.esstix
        if binding == "symbol":
            self.d = self.symbol
        if binding == "euclid":
            self.d = self.euclid
        if binding == "ooeuclid":
            self.d = self.ooeuclid
        if binding == "opensymbol":
            self.d = self.opensymbol
        if binding == "jopensymbol":
            self.d = self.jopensymbol
        self.aschar = self.unichar
        self.face = self.d.dface
        self.style = mFontPLAIN
        self.aftr = 0
        if (self.aschar == '-') | (self.aschar == '+') | (self.aschar == '/'):
            self.bpad = self.d.binpad
        if not self.JexStyle("math") & (self.aschar < 128):
            if (self.aschar == '=') | (self.aschar == '<') | (self.aschar == '>'):
                self.setSPad()
        else:
            u = int(self.unichar)
            #print(self.unichar ,"  !!!  ", u, )
            #a = int(self.d.unigrk.get(u))
            if self.unicode_:
                a = u
            else :
                a = self.d.unigrk.get(u)
            if a != None:
                if self.greekItalic:
                    self.style = mFontITALIC
                self.aschar = a.intValue()
                self.face = self.d.gface
                self.vpad = self.d.gvpad
                self.fixangle = self.d.gfixangle
                self.rescale = self.d.grescale
            else:
                #v = u.intValue() + 0x3b1 - 0x391
                v = u + 0x3b1 - 0x391
                #a = int(self.d.uniGrk.get(int(v)))
                if self.unicode_:
                    a = v
                else :
                    a = self.d.uniGrk.get(u)
                if a != None:
                    self.aschar = a.intValue()
                    self.face = self.d.Gface
                    self.vpad = self.d.Gvpad
                    self.fixangle = self.d.Gfixangle
                    self.rescale = self.d.Grescale
                else:
                    #a = int(self.d.uniArk.get(int(v)))
                    if self.unicode_:
                        a = v
                    else :
                        a = self.d.uniArk.get(int(v))
                    if a != None:
                        self.aschar = a.intValue()
                        y = str(self.aschar)
                        z = unichr(y)
                        self.texString = z
                        self.unichar = a.intValue()
                        self.face = self.d.dface
                    else:
                        #a = int(self.d.uniSym.get(u))
                        a = self.d.uniSym.get(u)
                        if a != None:
                            #b = int(self.d.uniFac.get(u))
                            b = self.d.uniFac.get(u)
                            if b == None:
                                self.face = self.d.sface[0]
                            else:
                                self.face = self.d.sface[b.intValue()]
                            if self.unicode_:
                                a = u
                            self.aschar = a.intValue()
                            self.setSPad()

    def JexStyle(self, nstyle):
        """ generated source for method JexStyle """
        if ((self.unichar >= ord('a')) & (self.unichar <= ord('z'))) | ((self.unichar >= ord('A')) & (self.unichar <= ord('Z'))) | (self.unichar == 32):
            pass
        else:
            return False
        z = chr(self.aschar)
        self.face = self.d.dface
        if nstyle == "math":
            self.style = mFontITALIC
            if not self.mathItalic:
                self.style = mFontPLAIN
            ## aftr = (float) 0.2;
            self.aftr = self.d.aftr
            #self.texString = z.__str__()
            self.texString = z
        if nstyle == "mathrm":
            self.style = mFontPLAIN
            self.aftr = 0
            #self.texString = "\\mathrm{" + z.__str__() + "}"
            #self.MMLString = "<mo>" + z.__str__() + "</mo>"
            self.texString = "\\mathrm{" + z + "}"
            self.MMLString = "<mo>" + z + "</mo>"
        return True

