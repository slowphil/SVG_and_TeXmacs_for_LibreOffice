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

""" generated source for module Jextex """
from __future__ import print_function
# package: jex
class Jextex(object):
    """ generated source for class Jextex """
    texDic = dict()
    dicTex = dict()
    tokens = dict()
    pairs = dict()
    h = dict()

    @classmethod
    def texMacro(cls, x):
        """ generated source for method texMacro """
        #y = str(cls.texDic.get(x))
        #if y != None:
        #    y = y + " "

        if x in cls.texDic :
            return cls.texDic[x] + " "
        else :
            return x

    tokens = dict([
        ("\\leftgrp", "FenceBox"),
        ("\\overset", "OverBox"),
        ("\\underset", "UnderBox"),
        #("\\unicode", "CharBox"),
        ("\\sqrt", "SqrtBox"),
        #("\\root", "RootBox"),
        #("\\root[", "[RootBox"),
        ("{", "RowBox"),
        ("^", "operator"),
        ("_", "operator"),
        ("\\overgrp", "operator"),
        ("\\frac", "DivisionBox"),
        ("\\rightgrp", "closer"),
        ("}", "closer"),
        ("&", "closer"),
        ("\\\\", "closer"),
        ("\\begin", "begin"),
        ("\\end", "end"),
        #("]", "closer"),
        ("\\unicode", "unichar"),
        ("\\mathrm", "RowBox"),
        ("\\operatorname", "RowBox"),
        ("\\,", "space"),
        ("\\:", "space"),
        ("\\;", "space")])
    
    pairs = dict([
        ("}", "{"),
        ("\\rightgrp", "\\leftgrp"),
        ("]", "["),
        ("&", "array"),
        ("\\\\", "array"),
        ("\\end", "array")])
    
    h = dict([
        ("\\", int(2)),
        ("{", int(1)),
        ("}", int(1)),
        (" ", int(0)),
        ("\r", int(0)),
        ("\n", int(0)),
        ("%", int(0)),
        ("_", int(1)),
        ("^", int(1)),
        ("~", int(1)),
        ("[", int(3)),
        ("]", int(3))])
    
    texDic = dict([
        ("*", "\\ast"),
        ("'", "\\prime"),
        ("\\unicode{3b1}", "\\alpha"),
        ("\\unicode{3b2}", "\\beta"),
        ("\\unicode{3c8}", "\\psi"),
        ("\\unicode{3b4}", "\\delta"),
        ("\\unicode{3b5}", "\\epsilon"),
        ("\\unicode{3d5}", "\\phi"),
        ("\\unicode{3b3}", "\\gamma"),
        ("\\unicode{3b7}", "\\eta"),
        ("\\unicode{3b9}", "\\iota"),
        ("\\unicode{3c6}", "\\varphi"),
        ("\\unicode{3ba}", "\\kappa"),
        ("\\unicode{3bb}", "\\lambda"),
        ("\\unicode{3bc}", "\\mu"),
        ("\\unicode{3bd}", "\\nu"),
        ("\\unicode{3bf}", "\\omicron"),
        ("\\unicode{3c0}", "\\pi"),
        ("\\unicode{3c7}", "\\chi"),
        ("\\unicode{3c1}", "\\rho"),
        ("\\unicode{3c3}", "\\sigma"),
        ("\\unicode{3c4}", "\\tau"),
        ("\\unicode{3c5}", "\\upsilon"),
        ("\\unicode{3c9}", "\\omega"),
        ("\\unicode{3be}", "\\xi"),
        ("\\unicode{3b8}", "\\theta"),
        ("\\unicode{3b6}", "\\zeta"),  
        
        ("\\unicode{39e}", "\\Xi"),
        ("\\unicode{3a8}", "\\Psi"),
        ("\\unicode{394}", "\\Delta"),
        ("\\unicode{393}", "\\Gamma"),
        ("\\unicode{3a6}", "\\Phi"),
        ("\\unicode{39b}", "\\Lambda"),
        ("\\unicode{3a0}", "\\Pi"),
        ("\\unicode{3a3}", "\\Sigma"),
        ("\\unicode{3a5}", "\\Upsilon"),
        ("\\unicode{3a9}", "\\Omega"),
        ("\\unicode{398}", "\\Theta"),
        
        ("\\operatorname{tanh}", "\\tanh"),
        ("\\operatorname{tan}", "\\tan"),
        ("\\operatorname{sup}", "\\sup"),
        ("\\operatorname{sinh}", "\\sinh"),
        ("\\operatorname{sin}", "\\sin"),
        ("\\operatorname{sec}", "\\sec"),
        ("\\operatorname{min}", "\\min"),
        ("\\operatorname{max}", "\\max"),
        ("\\operatorname{ln}", "\\ln"),
        ("\\operatorname{limsup}", "\\limsup"),
        ("\\operatorname{liminf}", "\\liminf"),
        ("\\operatorname{lim}", "\\lim"),
        ("\\operatorname{lg}", "\\lg"),
        ("\\operatorname{ker}", "\\ker"),
        ("\\operatorname{inf}", "\\inf"),
        ("\\operatorname{hom}", "\\hom"),
        ("\\operatorname{gcd}", "\\gcd"),
        ("\\operatorname{exp}", "\\exp"),
        ("\\operatorname{dim}", "\\dim"),
        ("\\operatorname{det}", "\\det"),
        ("\\operatorname{deg}", "\\deg"),
        ("\\operatorname{csc}", "\\csc"),
        ("\\operatorname{cot}", "\\cot"),
        ("\\operatorname{coth}", "\\coth"),
        ("\\operatorname{cos}", "\\cos"),
        ("\\operatorname{cosh}", "\\cosh"),
        ("\\operatorname{arctan}", "\\arctan"),
        ("\\operatorname{arcsin}", "\\arcsin"),
        ("\\operatorname{arccos}", "\\arccos"),
        ("\\operatorname{log}", "\\log"),
        
        ("\\unicode{222b}", "\\int"),
        ("\\unicode{2211}", "\\sum"),
        ("\\unicode{220f}", "\\prod"),
        ("\\unicode{22c5}", "\\cdot"),
        ("\\unicode{b7}", "\\bullet"),
        ("\\unicode{b1}", "\\pm"),
        ("\\unicode{2208}", "\\in"),
        ("\\unicode{220d}", "\\ni"),
        ("\\unicode{2209}", "\\notin"),
        ("\\unicode{2264}", "\\leq"),
        ("\\unicode{2265}", "\\geq"),
        ("\\unicode{2260}", "\\neq"),
        ("\\unicode{2282}", "\\subset"),
        ("\\unicode{2286}", "\\subseteq"),
        ("\\unicode{2283}", "\\supset"),
        ("\\unicode{2287}", "\\supseteq"),
        ("\\unicode{2229}", "\\cap"),
        ("\\unicode{222a}", "\\cup"),
        ("\\unicode{2192}", "\\rightarrow"),
        ("\\unicode{2190}", "\\leftarrow"),
        ("\\unicode{2207}", "\\nabla"),
        ("\\unicode{2202}", "\\partial"),
        ("\\unicode{221e}", "\\infty"),
        ("\\unicode{2205}", "\\emptyset"),
        ("\\unicode{211c}", "\\Re"),
        ("\\unicode{2026}", "\\ldots"),
        ("\\unicode{d7}", "\\times"),
        ("\\unicode{221d}", "\\propto"),
        ("\\unicode{2261}", "\\equiv"),
        ("\\unicode{2248}", "\\approx"),
        ("\\unicode{2112}", "\\Ell"),
        ("\\unicode{2113}", "\\ell"),
        ("\\unicode{e090}", "\\|"),
        
        ("\\unicode{7b}","\\{"),
        ("\\unicode{7d}","\\}"),
        ("\\unicode{5e}","\\^"),
        ("\\unicode{5f}","\\_"),
        ("\\unicode{7e}","\\~"),
        ("\\unicode{26}", "\\&"),
        ("\\unicode{6c}", "\backslash"),
        ("\\unicode{25}", "\\%"),
        ("\\unicode{24}", "\\$"),
        ("\\unicode{23}", "\\#"),
        
        ("\\leftgrp{[}", "\\left["),
        ("\\rightgrp{]}", "\\right]"),
        
        ("\\leftgrp{\\| }", "\\left\\Vert"),
        ("\\rightgrp{\\| }", "\\right\\Vert"),
        
        ("\\overgrp{-}", "\\over"),
        
        ("\\overset{-}", "\\overline"),
        ("\\overset{\\^}", "\\widehat"),
        ("\\overset{\\~}", "\\widetilde"),
        #tilde should be unicode rather than backslash tilde
        #backslash tilde apparently means put a tilde over the next letter
        ("\\overset{\\leftarrow }", "\\overleftarrow"),
        ("\\overset{\\rightarrow }", "\\overrightarrow"),
        ("\\overset{.}", "\\dot"),
        ("\\overset{..}", "\\ddot"),
        ("\\overset{...}", "\\dddot"),
        
        ("\\underset{-}", "\\underline"),
        ("\\underset{\\leftarrow }", "\\underleftarrow"),
        ("\\underset{\\rightarrow }", "\\underrightarrow")])
    dicTex = dict()
    for key in texDic :
          dicTex[texDic[key]]= key
    
    
    texDic["\\leftgrp{(}"] = "\\left("
    texDic["\\leftgrp{\\{}"] = "\\left\\{"
    texDic["\\leftgrp."] = "\\left."
    texDic["\\leftgrp{|}"] = "\\left\\vert"
    texDic["\\leftgrp{||}"] = "\\left\\Vert"
    texDic["\\leftgrp{<}"] = "\\langle"
    texDic["\\rightgrp{)}"] = "\\right)"
    texDic["\\rightgrp{\\}}"] = "\\right\\}"
    texDic["\\rightgrp."] = "\\right."
    texDic["\\rightgrp{|}"] = "\\right\\vert"
    texDic["\\rightgrp{||}"] = "\\right\\Vert"
    texDic["\\rightgrp{>}"] = "\\rangle"
    texDic["\\leftgrp{{}}"] = "\\left."
    texDic["\\rightgrp{{}}"] = "\\right."
    
    dicTex["\\left"] = "\\leftgrp"
    dicTex["\\right"] = "\\rightgrp"
    dicTex["\\vert"] = "|"
    dicTex["\\Vert"] = "\\|"
    dicTex["\\hat"] = "\\overset{\\^}"
    dicTex["\\tilde"] = "\\overset{\\~}"
    dicTex["\\vec"] = "\\overset{\\unicode{2192}}"
    dicTex["\\prime"] = "'"     
  
    #     * \bar{o} is a macron (cf. \=)
    #     * \mp minus or plus sign
    #     * \div divided by sign
    #     * \ast an asterisk (centered)
    #     * \star a five-point star (centered)
    #     * \circ an open bullet
    #     * \ll much less than
    #     * \gg much greater than
    #     * \sim similar to
    #     * \simeq similar or equal to
    #     * \per "perpendicular to" symbols
    #     * uparrow (uparrow)
    #     * downarrow (down arrow)
    #     * updownarrow (up/down arrow)
    #     * \cdots horizontally center of line (math mode only)
    #     * \ddots diagonal (math mode only)
    #     * \vdots vertical (math mode only)
    #     * \oint a surface (circular) integral sign
    #     * \bigcup big "U"
    #     * \bigcap big inverted "U"
    #     * \bigvee big "V"
    #     * \bigwedge big inverted "V"
    #     * \bigodot big "O" with dot at center
    #     * \bigotimes big "O" with cross inside
    #     * \bigoplus big "O" with a + inside
    #     * \biguplus big "U" with a + inside
    #     * \varepsilon (variation, script-like)
    #     * \vartheta (variation, script-like)
    #     * \varpi (variation)
    #     * \varrho (variation, with the tail)
    #     * \varsigma (variation, script-like)
    #     * \aleph Hebrew aleph
    #     * \hbar h-bar, Planck's constant
    #     * \imath variation on i; no dot
    #     * \jmath variation on j; no dot
    #     * \wp fancy script lowercase P
    #     * \Im script capital I (Imaginary)
    #     * \surd radical (square root) symbol
    #     * \angle angle symbol
    #     * \forall for all (inverted A)
    #     * \exists exists (left-facing E)
    #     * \breve{o} is a breve
    #     * \triangle open triangle symbol
    #     * \check{o} is a vee or check (cf. \v)
    #     * \acute{o} is an acute accent (cf. \`)
    #     * \grave{o} is a grave accent (cf. >\')
    #     * \Box open square
    #     * \Diamond open diamond
    #     * \flat music: flat symbol
    #     * \natural music: natural symbol
    #     * \clubsuit playing cards: club suit symbol
    #     * \diamondsuit playing cards: diamond suit symbol
    #     * \heartsuit playing cards: heart suit symbol
    #     * \spadesuit playing cards: space suit symbol


