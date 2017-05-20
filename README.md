# SVG and TeXmacs extension for LibreOffice ([direct download]())

Although LO has a pretty good support for SVG, when you copy a drawing in Inkscape it is disapointingly pasted as a bitmap in LO and it is not even possible to use "paste special" to get the vector format.

__The purpose of this extension is enable copy-pasting SVG drawings between LO and Inkscape__ (or any other app that handles SVG).

In addition, such SVG support makes it possible to use __GNU [TeXmacs](http://www.texmacs.org)__ as a __fully GUI equation editor__ for LO (TeXmacs' name is trully misleading as *it does **not** require knowing any TeX/LaTeX*). Such equations appear as SVG images but they are fully re-editable.

### Additional features : 
* MathType equations (metafile drawings or OLE) can be converted to TeXmacs.
* plain Latex markup in Writer can be converted to a TeXmacs equation.
* the conversion of TexMaths equations will soon be supported too.

## How it works:
The Copying and Pasting of SVG is not (not yet?) transparently integrated with the standard edit menu, and keyboard shortcuts.
After installlation, in Writer, Draw and Impress you'll have a toolbar with 3 buttons that implement the functionalities of the extension:
* Paste SVG ![Paste SVG](LO-PasteSvg-icon_16.png)
* Copy SVG ![Copy SVG](LO-CopySvg-icon_16.png)
* Edit TeXmacs ![TeXmacs](LO-TeXmacs-icon_16.png)


## Requirements
This extension is known to work in LibreOffice 5.3 in both Linux and Windows. It was not tested in OpenOffice.
For the TeXmacs equation editor feature, you need both TeXmacs and pdftocairo (from Poppler tools). In windows, [get both together here](https://github.com/slowphil/mingw-w64-texmacs/releases/latest). For Linux, I strongly recommend you use these [TeXmacs packages](https://software.opensuse.org/download.html?project=home:slowphil:texmacs-devel&package=texmacs) available for most distributions instead of the static TeXmacs build found at texmacs.org. 

## Technical details
This is my first LO extension and it uses a mix of Basic and Python scripts: 
It is easier to hack with Basic as you find much more examples and help, on the other hand Python was more convenient for implementing a couple of things (like for instance working around a bug in the interfacing to windows clipboard in LO).

## Known issues
- Inserting SVG in rescued documents leads to an error: save them first.
- SVG images are well handled in native LO document formats. However, when saved as MS Office documents, LO converts SVG images to lousy bitmaps. When exporting to these formats it is possible to preserve the vector character by converting SVG to metafile images, but any equation then becomes non-editable... 


## Credits
The extension is packaged using [Bernard Marcelly's excellent __Extension Compiler__](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler)
The conversion of MathType equations is based on the converter originaly included in the [Jex equation editor](http://levine.sscnet.ucla.edu/general/software/jex/), which was ported from Java to Python and adapted.
