#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
""" 

This code extracts the content of Mathtype equations encoded
in binary form in wmf and OLE images and converts it to Latex.

The original code was written in Java by David K. Levine
as a Mathtype importer for the Jex equation editor. Unfortunately,
as of 2017, the Mathtype import functionality was broken... 

Jex, its source code and some documentation can be found at 
http://levine.sscnet.ucla.edu/general/software/jex/


I have ported the code to python aided by java2python 
(https://github.com/natural/java2python) keeping only the parts
relevent for importing MathType equations and producing Latex output. 

Finally I fixed the broken parsing (that was easy) and added support
for more MathType contents, notably colors.

*********************************************************

This software falls under the GNU general public license version 2.
It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
in the root directory or <http://www.gnu.org/licenses/gpl-2.0.html>.

*********************************************************
"""
__author__ = "Philippe Joyez"
__credits__ = ["David K. Levine"]
__license__ = "GPL v2"


from Jexmath_mod import *
from Jexfont_mod import *

# package: jex
class Jexmt:
    global colorstack

    """ generated source for class Jexmt """
    def __init__(self, thebytearray):
        """ generated source for method __init__ """
        self.ptr = 0
        self.mtd = thebytearray


    def checkNext(self):
        """ generated source for method checkNext """
        if self.ptr >= len(self.mtd):
            return False
        #print( "checkNext returning true")
        return True

    def getNext(self):
        """ generated source for method getNext """
        b = self.mtd[self.ptr]
        #if self.ptr > 0 : #2268 :
        #  print("getnext :" ,hex(b)," : ",chr(b), "  @",hex(self.ptr))
        self.ptr += 1
        return b

    def getStart(self):
        """ generated source for method getStart """
        done = False
        state = 0
        while not done:
#            if state >0 :
#              print(state," ",self.ptr)
            if not self.checkNext():
                return False
            b = self.getNext()
            if state == 0:
                if b == 5:
                    state = 1
            elif state == 1:
                if (b == 0) or (b == 1):
                    state = 2
                else:
                    state = 0
            elif state == 2:
                if (b == 0) or (b == 1):
                    state = 3
                else:
                    state = 0
            elif state == 3:
                #print(state," ",self.ptr," ",b)
                if b > 3:
                    state = 4
                else:
                    state = 0
            elif state == 4:
                #print(state," ",self.ptr," ",b)
                state = 5
            elif state == 5:
                #print(state," ",self.ptr," ",b)
                if b == ord('D'):
                    state = 6
                else:
                    state = 0
            elif state == 6:
                #print(state," ",self.ptr," ",b)
                if b == ord('S'):
                    state = 7
                else:
                    state = 0
            elif state == 7:
                #print(state," ",self.ptr," ",b)
                if b == ord('M'):
                    state = 8
                else:
                    state = 0
            elif state == 8:
#                print(state," ",self.ptr," ",b)
                if b == ord('T'):
                     state = 9
                else:
                    state = 0
            elif state == 9:
                #print(state," ",self.ptr," ",b)
#there may be a digit after the T instead of 0 : incrementing pointer
                if b != 0 :
                    self.ptr += 1
                done = True
            else:
                state = 0
        if state != 9:
            return False
        self.ptr += 1
        #print("returning true at ", self.ptr)
        return True

    def parseForNull(self):
        """ generated source for method parseForNull """
        done = False
        while not done:
            if not self.checkNext():
                return
            b = self.getNext()
            if b == 0:
                return
        return

    endct = 0

    def parseString(self): #fetches string (null-terminated)
        """ generated source for method parseForNull """
        done = False
        ret = bytearray()
        while not done:
            if not self.checkNext():
                return
            b = self.getNext()
            if b == 0:
                return bytes(ret)
            ret.append(b)
        return


    def lineAfterFont(self):
        """ generated source for method lineAfterFont """
        if True:
            return
        if self.mtd[self.ptr] == 1:
            self.ptr += 1
            self.endct += 1
            print("LINE after font")
            if self.mtd[self.ptr] == 0:
                # ptr++;
                # endct--;
                print("END after font LINE")

    recType = int()

    def parseRuler(self):
        """ generated source for method parseRuler """
        c = int(self.getNext())
        self.ptr = self.ptr + (c * 3)

    def skipNudge(self):
        """ generated source for method skipNudge """
        b = self.getNext()
        bb = self.getNext()
        if (b == 128) and (bb == 128):
            self.ptr = self.ptr + 4

    def getInt(self):
        """ generated source for method getInt """
        b = int(self.getNext()) & 0xFF
        bb = int(self.getNext()) & 0xFF
        # print("" + b + " " + bb);
        return b + (0x100 * bb)

    def getUInt(self):
        """ generated source for method getUInt """
        b = int(self.getNext()) & 0xFF
        bl = int(b)
        if b >= 255:
            b = int(self.getNext()) & 0xFF
            bb = int(self.getNext()) & 0xFF
            bl = b + (0x100 * bb)
        return bl

    subType = 0

    def nextReal(self):
        """ generated source for method nextReal """
        mb = None
        self.subType = 0
        self.recType = -1
        while mb == None:
            if not self.checkNext():
                return None
            mb = self.nextRecord(True)
        return mb

    embellOver = True

    #def getEmbell(self, bb):
        #""" generated source for method getEmbell """
        #rb = RowBox()
        #uni = 0
        #rep = 1
        #self.embellOver = True
        #if bb == 2:
            #uni = ord('.')
        #elif bb == 3:
            #uni = ord('.')
            #rep = 2
        #elif bb == 4:
            #uni = ord('.')
            #rep = 3
        #elif bb == 8:
            #uni = ord('~')
        #elif bb == 9:
            #uni = ord('^')
        #elif bb == 11:
            #uni = 0x2192
        #elif bb == 12:
            #uni = 0x2190
        #elif bb == 17:
            #uni = ord('-')
        #elif bb == 24:
            #uni = ord('.')
            #rep = 4
        #elif bb == 25:
            #uni = ord('.')
            #self.embellOver = False
        #elif bb == 26:
            #uni = ord('.')
            #self.embellOver = False
            #rep = 2
        #elif bb == 27:
            #uni = ord('.')
            #self.embellOver = False
            #rep = 3
        #elif bb == 28:
            #uni = ord('.')
            #self.embellOver = False
            #rep = 4
        #elif bb == 29:
            #uni = ord('-')
            #self.embellOver = False
        #elif bb == 30:
            #uni = ord('~')
            #self.embellOver = False
        #elif bb == 33:
            #uni = 0x2192
            #self.embellOver = False
        #elif bb == 34:
            #uni = 0x2190
            #self.embellOver = False
        #else:
            #return None
        #ii = 0
        #while ii < rep:
            #rb.addChild(CharBox(uni))
            #ii += 1
        #return rb

    def getNull(self, id):
        """ generated source for method getNull """
        mb = None
        self.subType = 0
        self.recType = -1
        while self.recType != 0:
            if not self.checkNext():
                return
            mb = self.nextRecord(True)
        print("END of TMPL " + str(id))

    def getLine(self, rb):
        """ generated source for method getLine """
        done = False
        while not done:
            mb = self.nextRecord(True)
            #print( "getline : " , mb)
            if mb != None:
                if self.subType == 1:
                    #print( "getline : subType == 1")
                    zb = rb.c.removeLast()
                    zbnew = RowBox()
                    zbnew.addChild(zb)
                    lb = mb
                    lb.c.remove(0)
                    lb.c.add(0, zbnew)
                    rb.addChild(mb)
                elif self.recType == 1:
                    #print( "getline : recType == 1")
                    zrb = mb
                    nn = len(zrb.c)
                    ii = 0
                    while ii < nn:
                        mbx = zrb.c.remove(0)
                        if not mbx.isEmpty():
                            rb.addChild(mbx)
                        ii += 1
                else:
                    rb.addChild(mb)
            if (self.recType == 0) or (not self.checkNext()):
                self.subType = 0
                self.recType = 1
                if len(rb.c) == 0:
                    rb.addChild(EmptyBox())
                #print( "getline : return ",len(rb.c))
                return rb
        #print( "getline : return None")
        return None

    nid = 0

    def nextRecord(self, prs):
        global colorstack

        """ generated source for method nextRecord """
        self.subType = 0
        self.recType = -1
        if not self.checkNext():
            return None
        b = self.getNext()
        self.recType = b
        if not prs: return
        print ("nextrecord ",b, " (=",hex(b), ")  @",hex(self.ptr - 1) )
        if b == 0:
            print("END")
            return None
        elif b == 1:
            b = self.getNext()
            print ("line options :" ,str(b))
            if (b & 0x8) != 0:
                self.skipNudge()
            if (b & 0x4) != 0:
                self.ptr = self.ptr + 2
            # lspace
            if (b & 0x2) != 0:
                print("we have a ruler")
                # ruler
                #self.ptr += 1
                self.parseRuler()
            rb = RowBox()
            if (b & 0x1) != 0:
                print("LINE + END")
                rb.addChild(EmptyBox())
                self.subType = 0
                self.recType = 1
                self.subType = 2
                self.recType = -1
                rb = None
                return rb
            self.nid += 1
            tline = self.nid
            print("LINE " + str(tline))
            self.getLine(rb) #get all subsequent line elements
            print(str(tline) + ": " + rb.toTex())
            return rb
        elif b == 2:
            bb = self.getNext()
            if (bb | 0x8) == 0:
                self.skipNudge()
            # skip over the typeface
            bbb = self.getNext()
            if bbb == 255:
                self.ptr = self.ptr + 2
            # signed integer is not packed
            # 0x01  mtefOPT_CHAR_EMBELL  	character is followed by an embellishment list
            # 0x02 	mtefOPT_CHAR_FUNC_START character starts a function (sin, cos, etc.)
            # 0x04 	mtefOPT_CHAR_ENC_CHAR_8 character is written with an 8-bit encoded value
            # 0x10 	mtefOPT_CHAR_ENC_CHAR_16 character is written with an 16-bit encoded value
            # 0x20 	mtefOPT_CHAR_ENC_NO_MTCODE character is written without an 16-bit MTCode value
            uni = 0
            if (bb & 0x20) == 0:
                uni = self.getInt()
            if uni == 0x2212:
                uni = ord('-')
            if (uni == 60423) or (uni == 60424) : #left and right absolute value bar or middle bar for bra-ket according to MT (http://www.dessci.com/en/support/mathtype/tech/encodings/mtc_fences.htm)
                uni = ord("|")
            if (uni == 60425) or (uni == 60426) : #left and right norm bar according to MT (http://www.dessci.com/en/support/mathtype/tech/encodings/mtc_fences.htm)
                uni = ord("‖")
                
            cb = CharBox(uni)
            if uni == 61192:
                self.subType = 0
                self.recType = 2
                return None
            if uni == 61185:
                cb = SpaceBox("\\,")
            if uni == 61186:
                cb = SpaceBox("\\,")
            if uni == 61188:
                cb = SpaceBox("\\:")
            if uni == 61189:
                cb = SpaceBox("\\;")
            print("CHAR " + str(uni) + " : " + chr(uni))
            if (bb & 0x4) != 0:
                self.ptr += 1
            if (bb & 0x10) != 0:
                self.ptr = self.ptr + 2
            if (bb & 0x01) != 0:
                bmb = cb
                emb = None
                donee = False
                while not donee:
                    if not self.checkNext():
                        donee = True
                    else:
                        emb = self.nextRecord(True) #now returns embell type, for embellbox
                    if not donee:
                        if (emb != None) and (self.recType == 6):
                            bmb = EmbellBox(bmb, emb)
                            #if self.embellOver:
                                #bmb = OverBox(bmb, emb)
                            #else:
                                #bmb = UnderBox(bmb, emb)
                        if self.recType == 0:
                            donee = True
                    if donee:
                        self.subType = 0
                        self.recType = 2
                        return bmb
            self.subType = 0
            self.recType = 2
            return cb
        elif b == 3:
            bb3 = self.getNext()
            if (bb3 | 0x8) == 0:
                self.skipNudge()
            tt = self.getNext()
            self.nid += 1
            ttmpl = self.nid #template's index in the template counter
            print("TMPL " + str(tt) + " " + str(ttmpl))
            var = self.getNext()
            #tt template type 0<= tt <=8 : simple matched fences
            # 9, 30 unmatched brackets and dirac bra-ket
            ivar = int(var)
            if (var & 0x80) !=0 : #2-bytes variations
                tmp = self.getNext()
                ivar = int(((var & 0x7F) | (tmp << 8)))
            topt = self.getNext() #template-specific options
            if (tt == 27) or (tt == 28) or (tt == 29):
                print( "SUBSUP")
                ssb = SubSupBox()
                rmain = RowBox()
                rmain.addChild(EmptyBox())
                ssb.addChild(rmain)
                if tt == 28:
                    ssb.addChild(ssb.wrapBox(EmptyBox()))
                    ssb.addChild(ssb.wrapBox(self.nextReal()))
                if tt == 27:
                    ssb.addChild(ssb.wrapBox(self.nextReal()))
                    ssb.addChild(ssb.wrapBox(EmptyBox()))
                if tt == 29:
                    ssb.addChild(ssb.wrapBox(self.nextReal()))
                    ssb.addChild(ssb.wrapBox(self.nextReal()))
                self.getNull(ttmpl)
                self.subType = 1
                self.recType = 3
                return ssb
            if tt == 10:
                print("SQRT ")
                if ivar == 0:
                    col = colorstack [-1]
                    sb = SqrtBox(self.nextReal())
                    sb.color = col
                    # nextReal();
                    self.getNull(ttmpl)
                    self.subType = 0
                    self.recType = 3
                    return sb
            if tt == 11:
                print("FRAC ")
                if (ivar & 0x06) != 0 : #fraction with slash
                    db = DivisionBox(self.nextReal(), CharBox(ord('/')), self.nextReal()) #SpaceBox("/") ?
                else :
                    db = DivisionBox(m0 = self.nextReal(), m2 = self.nextReal())
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return db
            if tt <= 8: #simple matched fences
                print("FENCES")
                col = colorstack[-1]
                mainslot = self.nextReal()
                if (ivar & 0x0001) != 0:
                    lf = self.nextReal()
                else :
                    lf = EmptyBox()
                if (ivar & 0x0002) != 0:
                    rf = self.nextReal()
                else :
                    rf = EmptyBox()

                fb = FenceBox(lf, mainslot, rf)
                fb.color = col
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return fb
            if tt == 30: #Dirac bra-kets
                print("BRA-KET")
                col = colorstack[-1]
                if (ivar & 0x0001) == 1:
                    leftslot = self.nextReal()
                if (ivar & 0x0002) == 2:
                    rightslot = self.nextReal()
                if (ivar & 0x0001) == 1:
                    lf = self.nextReal()
                else :
                    lf = EmptyBox()
                mf = self.nextReal()
                if (ivar & 0x0002) == 2:
                    rf = self.nextReal()
                else :
                    rf = EmptyBox()
                if (ivar & 0x0003) ==3 :
                    fb = FenceBox(lf, leftslot, mf, rightslot, rf)
                elif (ivar & 0x0001) == 1:
                    fb = FenceBox(lf, leftslot, mf)
                elif (ivar & 0x0002) == 2:
                    fb = FenceBox(mf, rightslot, rf)
                else :
                    raise "unexpected situation"
                fb.color = col
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return fb
            if (tt == 12) : #underbar
                print("UNDERBAR")
                b = EmbellBox(self.nextReal(), 29)
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return b
            if (tt == 13) : #overbar
                print("OVERBAR")
                b = EmbellBox(self.nextReal(), 17)
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return b
            ##if (tt == 14) : #extensible arrows
                #if (ivar & 0x0001) != 0: # double arrow (else single)
                #if (ivar & 0x0002) != 0: # harpoon
                #if (ivar & 0x0004) != 0: # slot over arrow present
                #if (ivar & 0x0008) != 0: # slot under arrow present
                #if (ivar & 0x0010) != 0: # arrow points left ; if double or harpoon, large over small
                #if (ivar & 0x0020) != 0: # if single, arrow points right ; if double or harpoon, small over large
                #mainslot = self.nextReal()
                #arrowchar = self.nextReal()

                ##b = OverBox(self.nextReal(), Charbox(self.nextReal()))
                ##self.subType = 0
                ##self.recType = 3
                ##return b
            #if (tt == 31) : #vector
                #if (ivar & 0x0001) != 0: # arrow points left
                #if (ivar & 0x0002) != 0: # arrow points right
                #if (ivar & 0x0004) != 0: # arrow under slot, else over
                #if (ivar & 0x0008) != 0: # harpoon
                #b = EmbellBox(self.nextReal(), 17)
                #self.subType = 0
                #self.recType = 3
                #return b
            if (tt == 32) : #wide tilde over
                b = EmbellBox(self.nextReal(), 8)
                self.subType = 0
                self.recType = 3
                return b
            if (tt == 33) : #wide hat over
                b = EmbellBox(self.nextReal(), 9)
                self.subType = 0
                self.recType = 3
                return b
            #if (tt == 34) : #wide arc over
                #b = EmbellBox(self.nextReal(), 17)
                #self.subType = 0
                #self.recType = 3
                #return b
            if (tt == 24) or (tt == 25) : #horizontal brace or bracket
                #if (ivar & 0x0001) != 0: # underbrace else over
                # we hijack subsupbox, and perform post processing
                # in toTeX, similar to what is done for sum, int, etc.
                mainslot = self.nextReal()
                smallslot = self.nextReal()
                bracechar = self.nextReal()
                ssb = SubSupBox()
                ssb.addChild(bracechar);
                ssb.addChild(mainslot)
                ssb.addChild(smallslot)
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 3
                return ssb
                
            if (tt >= 15) and (tt <= 22):
                # variation bits
                #  0x0001  	tvBO_LOWER  	lower limit is present
                #  0x0002 	tvBO_UPPER 	upper limit is present
                #  the previous is as documented, but appears wrong, should be 0x0010, 0x0020
                #  0x0040 	tvBO_SUM 	summation-style limit positions, else integral-style
                mainslot = None
                # according the to documentation tt = 21, 22 should also have mainslot, but does not
                if tt <= 20:
                    mainslot = self.nextReal()
                # documentation claims the upper limit is first, but in fact lower limit is
                llim = None
                if (ivar & 0x0010) != 0:
                    llim = self.nextReal()
                ulim = None
                if (ivar & 0x0020) != 0:
                    ulim = self.nextReal()
                newrow = RowBox()
                if (ulim != None) or (llim != None):
                    ochar = self.nextReal()
                    ssb = SubSupBox()
                    ssb.addChild(ssb.wrapBox(ochar))
                    if llim != None:
                        ssb.addChild(ssb.wrapBox(llim))
                    else:
                        ssb.addChild(ssb.wrapBox(EmptyBox()))
                    if ulim != None:
                        ssb.addChild(ssb.wrapBox(ulim))
                    else:
                        ssb.addChild(ssb.wrapBox(EmptyBox()))
                    newrow.addChild(ssb)
                else:
                    unitmp = 0
                    # Mathtype passes the proper unicode symbol; we just store it and 
                    # substitute with proper latex op in toTex of SubSupBox
                    #if tt == 15: 
                        #unitmp = 8747 # integral 0x222B
                        ## latex form is \int_{low}^{up}
                    #if tt == 16:
                        #unitmp = 8721 # 0x2211 Summation
                        ## latex form is \sum_{low}^{up}
                    #if tt == 17:
                        #unitmp = 8719 # 0x220F Product
                        ## latex form is \prod_{low}^{up}
                    #if tt == 19:
                        #unitmp = 8746 # Union 0x222A
                        ## latex form is \bigcup_{low}^{up}
                    #if tt == 20:
                        #unitmp = 8745 # intsersection 0x2229
                        ## latex form is \bigcap_{low}^{up}
                    newrow.addChild(newrow.wrapBox(self.nextReal()))
                if mainslot != None:
                    newrow.addChild(mainslot)
                self.getNull(ttmpl)
                self.subType = 0
                self.recType = 1
                return newrow
            rb3 = RowBox()
            self.nid += 1
            tun = self.nid
            print("unknown/unhandled TMPL " + str(tun))
            self.getLine(rb3)
            bogus = FenceBox()
            bogus.addChild(bogus.wrapBox(CharBox(ord('?'))))
            bogus.addChild(rb3)
            bogus.addChild(bogus.wrapBox(CharBox(ord('?'))))
            self.subType = 0
            self.recType = 3
            return bogus
        elif b == 4:
            self.nid += 1
            tpile = self.nid
            print("PILE " + str(tpile))
            bb4 = self.getNext()
            if (bb4 | 0x8) == 0:
                self.skipNudge()
            halign4 = self.getNext()
            valign4 = self.getNext()
            if (b & 0x2) != 0:
                self.ptr += 1
                self.parseRuler()
            maBx = MatrixBox()
            maBx.cols = 2
            maBx.halign.add("r")
            maBx.halign.add("l")
            maBx.texType = "align"
            maBx.spacef = 0.0
            maBx.leadf = 0.0
            d4 = False
            while not d4:
                if not self.checkNext():
                    d4 = True
                elif self.mtd[self.ptr] == 0:
                    d4 = True
                    self.ptr += 1
                if d4:
                    self.recType = 4
                    self.subType = 0
                    print("PILE END " + str(tpile))
                    return maBx
                mb4 = self.nextReal()
                maBx.rows += 1
                maBx.addChild(maBx.wrapBox(mb4))
                maBx.addChild(maBx.wrapBox(EmptyBox()))
        elif b == 5:
            self.nid += 1
            tmat = self.nid
            print("MATRIX " + str(tmat))
            bb5 = self.getNext()
            if (bb5 | 0x8) == 0:
                self.skipNudge()
            valign = self.getNext()
            hjust = self.getNext()
            vjust = self.getNext()
            rows = self.getNext()
            cols = self.getNext()
            self.getNext()
            # parse over row_parts
            self.getNext()
            # parse over col_parts
            mab = MatrixBox()
            mab.rows = rows
            mab.cols = cols
            if vjust == 3:
                mab.valign = "c"
            hh = "l"
            if hjust == 2:
                hh = "c"
            if hjust == 3:
                hh = "r"
            d5 = False
            jj = 0
            while jj < cols:
                mab.halign.add(hh)
                jj += 1
            ii = 0
            while ii < rows:
                jj = 0
                while jj < cols:
                    if not d5:
                        mb5 = self.nextReal()
                        if self.recType == 0:
                            d5 = True
                        else:
                            mab.addChild(mab.wrapBox(mb5))
                    if d5:
                        mab.addChild(mab.wrapBox(EmptyBox()))
                    jj += 1
                ii += 1
            if self.recType != 0:
                self.getNull(-1)
            self.recType = 5
            self.subType = 0
            print("END MATRIX " + str(tmat))
            return mab
        elif b == 6:
            bb6 = self.getNext()
            if (bb6 | 0x8) == 0:
                self.skipNudge()
            emb6 = self.getNext()
            print("EMBELL " + str(emb6))
            #gemb = self.getEmbell(emb6)
            self.subType = 0
            self.recType = 6
            #return gemb
            return emb6
        elif b == 7:
            print("RULER")
            self.parseRuler()
        elif b == 8:
            print("FONT_STYLE_DEF")
            self.getUInt()
            self.getNext()
        elif b == 9:
            print("SIZE")
            bb9 = self.getNext()
            if bb9 == 101:
                self.ptr = self.ptr + 2
            elif bb9 == 100:
                self.ptr = self.ptr + 3
            else:
                self.ptr += 1
        elif b == 10:
            print("FULL size")
            self.lineAfterFont()
        elif b == 11:
            print("SUB size")
            self.lineAfterFont()
        elif b == 12:
            print("SUB2 size")
            self.lineAfterFont()
        elif b == 13:
            print("SYM size")
            self.lineAfterFont()
        elif b == 14:
            print("SUBSYM size")
            self.lineAfterFont()
        elif b == 15:
            cindex = self.getUInt()
            print("COLOR :", cindex, "  ////////////////// was ", colorstack[-1])
            colorstack.append(cindex)
            return None
        elif b == 16:
            print("COLOR_DEF")
            bb16 = self.getNext() #options byte
            #each color encoded from 0 to 1000 on 2 bytes
            if (bb16 & 0x1) != 0: # cmyk color model
                c = (self.getNext() + 256*self.getNext())/1000.
                m = (self.getNext() + 256*self.getNext())/1000.
                y = (self.getNext() + 256*self.getNext())/1000.
                k = (self.getNext() + 256*self.getNext())/1000.
                r = int(255*(k-1)*(c-1))
                g = int(255*(k-1)*(m-1))
                b = int(255*(k-1)*(y-1))
            else :
                r = int(255* (self.getNext() + 256*self.getNext())/1000.)
                g = int(255* (self.getNext() + 256*self.getNext())/1000.)
                b = int(255* (self.getNext() + 256*self.getNext())/1000.)
            if r > 255 : r = 255
            if g > 255 : g = 255
            if b > 255 : b = 255
            
            col = hex(b+256*g+65536*r+16777216)[3:]
            
#https://www.processing.org/discourse/alpha/board_Tools_action_display_num_1082055374.html
#CMYK -> CMY
#CMYK values = From 0 to 1
#C = ( C * ( 1 - K ) + K )
#M = ( M * ( 1 - K ) + K )
#Y = ( Y * ( 1 - K ) + K )
 
#-- 
 
#CMY -> RGB
#CMY values = From 0 to 1
 
#R = ( 1 - C ) * 255
#G = ( 1 - M ) * 255
#B = ( 1 - Y ) * 255 
    
            if (bb16 & 0x4) != 0: #named color
                cname = self.parseString()
            else :
                cname = "color-"+str(len (colorlist))
            colorlist.append([col,cname])
            cindex = len (colorlist)-1
            print ("new color def :", col, " index=" , cindex)
            return None
        elif b == 17:
            print("FONT_DEF")
            self.parseForNull()
        elif b == 18:
            print("EQN_PREFS")
            test = True
            while test:
                self.nextRecord(False)
                if not self.checkNext():
                    self.subType = 0
                    self.recType = 18
                    return None
                if self.recType == 10:
                    if not self.checkNext():
                        self.subType = 0
                        self.recType = 18
                        return None
                    self.nextRecord(False)
                    if (self.recType == 1) or (self.recType == 4) or (self.recType == 16): #added test for 16??
                        self.ptr = self.ptr - 1
                        self.subType = 0
                        self.recType = 18
                        if prs:
                            print("OK")
                        return None
        elif b == 19:
            print("ENCODING_DEF")
            self.parseForNull()
        else:
            print("NOT IMPLEMENTED REC: " + str(b))
            if (b >= 100) or (b < 0):
                bl = self.getUInt()
                self.ptr = self.ptr + int(bl)
        return None

    def parseMT(self):
        """ generated source for method parseMT """
        print("starting");
        ans = RowBox()
        if self.getStart():
            print("Found start")
            nends = 0
            while self.checkNext(): 
                print("Starting interpreter")
                mb = self.nextRecord(True)
                if mb != None:  #if this is true, parseMT terminates: we come here only once
                    if self.recType == 1: # type LINE add all children of mb to ans
                        for nmb in mb.c :
                            if not nmb.isEmpty():
                                ans.addChild(nmb)
                        ## if(endct == 0) return ans;
                        self.endct -= 1
                    #elif self.subType == 1: # take last element of ans, put it in a rowbox, replace first of mb with the rowbox, finally insert mb in ans
## used for adding exponent and index to elem
                        #zb = ans.c.removeLast() #? is ans ever non-empty, here???
                        #zbnew = RowBox()
                        #zbnew.addChild(zb)
                        #lb = mb
                        #lb.c.remove(0)
                        #lb.c.add(0, zbnew)
                        #ans.addChild(mb)
                    else: # add mb (as a block) as a single child of ans 
                        ans.addChild(mb)
                    return ans  #
                if self.recType == 0: #mb == None, if we find more than 6, stop
                    nends += 1
                    if nends > 6: 
                        return ans
        return ans #we've hit end of file



def getMTData(fname):
    fh= open(fname, "rb")
    ba = bytearray(fh.read())
    """ generated source for method getMTData """
    jmt = Jexmt(ba)
    return jmt.parseMT()
    
def MTtoLatex(filename) :
    global colorlist
    del colorlist[:]
    colorlist.append(["000000", 'black'])   #default (index 0) if black, newly defined have indices >=1 in order they are defined
    global colorstack
    del colorstack[:]
    colorstack.append(0)
    objlist=getMTData(filename)
    del colorstack[:]
    colorstack.append(0)
    latex = objlist.toTex()
    latex = (latex.replace("rightgrp", "right").replace("leftgrp","left"))
    print (latex)
    latex2 = simplifcolor( latex)
    while len(latex2) < len(latex) :
        latex = latex2
        latex2 = simplifcolor(latex)
    print (latex)
    return latex
    
def simplifcolor( latex):
    
    latex = latex.replace("\\{", "\\leftbrace").replace("\\}", "\\rightbrace")
    latex = latex.replace("{\\color[HTML]{000000}", "{\\color{black}")
    #latex = latex.replace("\\color{black}  &", "&")
    #latex = latex.replace("\\color{black}  {\\color", "{\\color")
    #latex = latex.replace("\\color{black} }", "}")
    start = latex.find("{\\color") #find first color statement
    while start >= 0 :
        startend = latex.find("}",start)
        print(latex[start:startend+1] +" starts at " , start)
        nesting = 1
        for i in range( startend+1 , len(latex)):
            ch = latex[i]
            if ch == "{" : nesting += 1
            elif ch == "}" : nesting -= 1
            if nesting ==0 : break 
        stop = i # this is the closing bracket of the color
        print("ends at " , stop, " : ", latex[start:stop+1])
        # if, within the same nesting level, a following color is the same, merge them
        start2 = latex.find("{\\color",stop) # look for next color statement
        while start2 >= 0 :
            # is it at the same nesting level?
            nesting = 0
            sk=""
            for l in range( stop+1 , start2):
                ch = latex[l]
                sk=sk+ch
                if ch == "{" : nesting += 1
                elif ch == "}" : nesting -= 1
                if nesting < 0 : break
            if nesting < 0 : 
                break
            elif nesting > 0 :
                start2 = latex.find("{\\color",start2+6) #try next color
            else :
                start2end = latex.find("}",start2)
                print("next color at same level is ", latex[start2:start2end+1] +" starts at " , start2)
                print ("skipped ",sk)
                if (latex[start:startend] == latex[start2:start2end]) :
                    print ("are the same : merging")
                    print( latex[start:start2end+5],"...  ->  ",latex[start:stop]+latex[stop+1:start2]+latex[start2end+1:start2end+5]+"...")
                    latex = latex[:stop]+latex[stop+1:start2]+latex[start2end+1:]
                    nesting = 1
                    for i in range( start2end+1 , len(latex)):
                        ch = latex[i]
                        if ch == "{" : nesting += 1
                        elif ch == "}" : nesting -= 1
                        if nesting ==0 : break 
                    stop = i
                    start2 = latex.find("{\\color",stop)
                else :
                    start2 = latex.find("{\\color",start2+6)
        #if the color statement contains only (other) color statements or non-printing characters, remove it
        j = startend + 1
        nothingbetween = False
        while j < stop :
            k = latex.find("{\\color",j,stop)
            if k < 0 : k = stop
            nothingbetween = True
            for ch in latex[j:k] :
                if not ((ch == " " ) or (ch == "{" ) or (ch == "}" )): 
                    nothingbetween = False
                    break
            if nothingbetween and (k < stop): # goto to next included color
                nesting = 1 #first find end of this one
                for l in range( k+6 , stop):
                    ch = latex[l]
                    if ch == "{" : nesting += 1
                    elif ch == "}" : nesting -= 1
                    if nesting ==0 : break
                j = l + 1
            else : break
        if nothingbetween : #remove the color tag ...
            latex = latex[:start]+latex[startend + 1:stop]+latex[stop+1:]
            start = latex.find("{\\color",start) #... and move to next color tag
        
        start = latex.find("{\\color",start+6)
                
    latex = latex.replace("\\leftbrace","\\{").replace("\\rightbrace","\\}")
    return latex

if __name__ == '__main__':
    MTtoLatex("/tmp/test.wmf")

g_exportedScripts = MTtoLatex,

