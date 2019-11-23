# SVG and TeXmacs extension for LibreOffice ([direct download](https://github.com/slowphil/SVG_and_TeXmacs_for_LibreOffice/releases/latest))

Although LO has a pretty good support for SVG, when you copy a drawing in Inkscape it is disappointingly pasted as a bitmap in LO and it is not even possible to use "paste special" to get the vector format.

__The purpose of this extension is to enable copy-pasting SVG drawings between LO and Inkscape__ (or any other app that handles SVG).

In addition, such SVG support makes it possible to use __GNU [TeXmacs](http://www.texmacs.org)__ as a __fully GUI equation editor__ for LO (TeXmacs' name is truly misleading as *it does **not** require knowing any TeX/LaTeX*). Such equations appear as SVG images but they are fully re-editable.

### Additional features : 
* MathType equations (metafile drawings or OLE) can be converted to TeXmacs.
* plain Latex markup in Writer can be converted to a TeXmacs equation.
* the conversion of TexMaths equations will soon be supported too.

## How it works:
The Copying and Pasting of SVG is not (not yet?) transparently integrated with the standard edit menu, and keyboard shortcuts.
After installation, in Writer, Draw and Impress you'll have a toolbar with 3 buttons that implement the functionalities of the extension:
* Paste SVG ![Paste SVG](LO-PasteSvg-icon_16.png)
* Copy SVG ![Copy SVG](LO-CopySvg-icon_16.png)
* Edit TeXmacs ![TeXmacs](LO-TeXmacs-icon_16.png)


## Requirements
This extension is known to work in LibreOffice ⩾ 5.3 in both Linux and Windows. It was not tested in OpenOffice and probably won't work without modifications. If the extension fails to install properly, make sure you have `libreoffice-script-provider-python` installed.

For the TeXmacs equation editor feature to work nicely with LibreOffice, a [patch](https://github.com/slowphil/mingw-w64-texmacs/blob/master/equation-editor-plugin.patch)ed version of TeXmacs is presently strongly recommended (when plugins will be able to have their own preference tab, the patch will be integrated into the "trunk"). You'll also need `pdftocairo` (from Poppler tools). In windows, [get both together here](https://github.com/slowphil/mingw-w64-texmacs/releases/latest). For Linux, [this AppImage](https://download.opensuse.org/repositories/home:/slowphil:/texmacs-devel/AppImage/texmacs-latest-x86_64.AppImage) contains the [patch](https://build.opensuse.org/package/view_file/home:slowphil:texmacs-devel/texmacs/equation-editor-plugin.patch) and is thus presently recommended over the TeXmacs build found at texmacs.org.

## Technical details
This is my first LO extension and it uses a mix of Basic and Python scripts: 
It is easier to hack with Basic as you find much more examples and help, on the other hand Python was more convenient for implementing a couple of things (like for instance working around a bug in the interfacing to windows clipboard in LO).

### Modifying and repacking the LO extension (.oxt file)
If you tweak the Basic code in LO and want to repack the extension, clone the repo and export your modified Basic library to the `TeXmacs_and_SVG` folder. Then open the `SVG_and_Texmacs.odt` (which is a just [Bernard Marcelly's __Extension Compiler__](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler) with proper settings for this extension set in the content of the Basic macro `Standard:Module1` in that file) and recompile the oxt in section 2.3.3 (full instructions in the file).

## Known issues
- Inserting SVG in rescued documents leads to an error: save them first.
- SVG images are well handled in native LO document formats (.odt, .odg, .odp). However, when saved as MS Office documents, LO converts SVG images to lousy bitmaps. When exporting to these formats it is possible to preserve the vector character by converting SVG to metafile images, but any equation then becomes non-editable…
- If the characters in the SVG images appear too bold, you have a bad version of FreeType and need to upgrade (or downgrade if it's easier). This problem occurs for instance in Ubuntu 16.04 which uses FreeType 2.6.1 and it can be solved by using [FreeType 2.7 from this PPA](https://launchpad.net/~no1wantdthisname/+archive/ubuntu/ppa)


## Credits
The extension is packaged using [Bernard Marcelly's excellent __Extension Compiler__](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler)
The conversion of MathType equations is based on the converter originaly included in the [Jex equation editor](http://levine.sscnet.ucla.edu/general/software/jex/), which was ported from Java to Python and adapted.
The icon of the TeXmacs toolbar button is based on an original design by Massimiliano Gubinelli.
