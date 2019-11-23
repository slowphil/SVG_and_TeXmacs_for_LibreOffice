#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
*******************************************************************************
* Inkacpe and Texmacs extension for LibreOffice
* COPYRIGHT  : (C) 2017 Philippe JOYEZ
*******************************************************************************
* This software falls under the GNU general public license version 3 or later.
* It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
* in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.
*******************************************************************************

Starting with Inkscape 0.92, when putting an image on the clipboard, inkscape
places the defs that are needed in the copied drawing into a tag "inscape:clipboard"

Firefox does not draw these elements, but LO does and that messes up the result.
IMHO its a LO bug, but for the moment we work around it by changing
the tag to svg:defs so that the drawing renders as expected.

"""
#------------------------------------------------------------------------------
'''
#this is proper editing of an XML file, but LO does not display
#the resulting file properly (it's blank, non visible, non-selectable!)

from xml.etree import ElementTree as etree

SVG_NS = u"http://www.w3.org/2000/svg"
INKSCAPE_NS="http://www.inkscape.org/namespaces/inkscape"

def fix_svg(svg_name) :
  tree = etree.parse(svg_name)
  root = tree.getroot()
  clip_node = root.find('{%s}clipboard' % INKSCAPE_NS)
  if clip_node :
    clip_node.tag = ('{%s}defs' % SVG_NS)
    tree.write(svg_name)

using simple text edition instead:
'''

def fix_inkscape_svg(svg_name) :    
  f = open(svg_name,'r')
  filedata = f.read()
  f.close()
  
  newdata = filedata.replace("inkscape:clipboard","defs")
  
  f = open(svg_name,'w')
  f.write(newdata)
  f.close()

"""functions exposed to LO"""
g_exportedScripts = fix_inkscape_svg,

if __name__ == u'__main__':
    """allow runing the script standalone for debugging"""
    fix_inkscape_svg("/tmp/inkscape92_paste2.svg")
    
