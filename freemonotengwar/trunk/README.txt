FreeMonoTengwar: README
=======================

The FreeMonoTengwar font is based on the FreeMono.sfd of the 2009-01-04
GNU FreeFont. It includes many portions of FreeMono.sfd without
alteration, but adds the tengwar script to the Personal Use Area U+E000
-- U+E07F according the ConScript Unicode Registry, see
http://www.evertype.com/standards/csur/tengwar.html and taking into
account later additions by Johan Winge.

Furthermore, the font makes use of some ligatures. These ligatures are
provided either by the Graphite smart rendering technology or by the
OpenType smart rendering technology.

For more detailed informations, see: http://freetengwar.sourceforge.net/


Statement of Purpose
====================

The Free Tengwar Font Project aims at developing a family of general
purpose fonts that cover J. R. R. Tolkien's tengwar script and that are
compatible with the Unicode standard. Additional aims are tools and
documentation for the use of such fonts. Compatibility with Unicode
means that these fonts' tengwar glyphs will not be mapped over any other
Unicode character. Instead, they are mapped on the Personal Use Area of
Unicode.


Files and their suffixes
========================

TrueType fonts for immediate consumption are the files with the .ttf
(TrueType Font) suffix.  These are ready to use in Xwindows based
systems using FreeType, on Mac OS, and on older Windows systems.

OpenType fonts (with suffix .otf) are for use in Windows Vista. Note
that although they can be installed on Linux, but many applications in
Linux still don't support them.

The files with .sfd (Spline Font Database) are in FontForge's native
format, the free outline font editor by George Williams
<http://fontforge.sourceforge.net/>. The files with .gdl (Graphite
Description Language) describe the Graphite features of the font. The
.sfd and .gdl files have been used for editing these fonts. The file
with .py is a python script that will generate the fonts from the .sfd
and .gdl files (if certain other requirements are met, see the section
Editing and Building).


Installing FreeMonoTengwar
==========================

FreeMonoTengwar can be used in any modern operating system, even if some
ligatures might not work.

This document explains how to install FreeFont on some common systems.


	* Windows 95/98/NT/2000/XP; Vista

		Note that in at least Vista, XP and 2000, the OpenType versions
		perform much better than, and are recommended over, the TrueType
		ones.

		Vista:
			1) From the Start menu, open Control Panels
			2) Drag-n-drop font files onto Fonts control panel
			You may get a dialog saying
				"Windows needs your permission to continue"
			a) Click Continue

		95/98/NT:
			The font installation is similar to Vista.

			In order to use OpenType, users of Windows 95, 98 and NT 4.0
			can install Adobe's 'Type Manager Light'.  It is available
			for download without cost from Adobe's web site.

			Otherwise, use the TrueType versions.

	* Mac OS X

		Installing on Mac OS X consists of moving the .ttf files to
		either /Library/Fonts/  or  ~/Library/Fonts/ depending on
		whether they should be available to all users on your system or
		just to yourself.

	* UNIX/GNU/Linux/BSD Systems

		FreeFont works with any system using the free font rasterizer
		FreeType <http://www.freetype.org/>.

		KDE local installation:
			Users of KDE can install .ttf files on a per-user basis
			using the KDE Control Center module "kcmfontinst", which
			may appear in the menu as

				Settings -> System Administration -> Font Installer

			This is especially helpful for developers and testers.


		Generic X-windows:

			1) Fetch the freefont-ttf.tar.gz package with Free UCS
			outline fonts in the TrueType format.

			2) Unpack TrueType fonts into a suitable directory, e.g.
			/usr/local/share/fonts/default/TrueType/

			3) If you have chosen any other directory, make sure the
			directory you used to install the fonts is listed in the
			path searched by the X Font Server by editing the config
			file in /etc/X11/.

			In some systems, you list the directory in the item
			"catalogue=" in the file /etc/X11/fs/config.

			4) Run ttmkfdir in the directory where you unpacked the
			fonts.


Coverage and differences from GNU FreeMono
==========================================

In addition to the Unicode Personal Use Area tengwar, FreeMonoTengwar
covers a wide range of characters, including Latin Extended characters,
the IPA, Greek, Runic, or mathematical symbols. However, some character
blocks of the original GNU FreeFont FreeMono font have been removed:
Kyrillic, Armenian, Georgian, Hebrew, Box Drawing characters and
Braille.

A few GNU FreeMono characters have been changed so they fit in better
with tengwar text:

	* U+10fb: GEORGIAN PARAGRAPH SEPARATOR,
	* U+2058: FOUR DOT PUNCTUATION,
	* U+205d: TRICOLON,
	* U+25cc: DOTTED CIRCLE,
	* U+2e2d: FIVE DOT MARK,
	* U+2e2c: SQUARED FOUR DOT PUNCTUATION,
	* U+2e31: WORD SEPARATOR MIDDLE DOT.


Editing and building
====================

Get FontForge, the free outline font editor by George Williams
<http://fontforge.sourceforge.net/>. Edit FreeMonoTengwar.sfd, then
generate fonts.

Adding Graphite support to the font is a little bit trickier. It
requires an installation of Sharon Correll's free Graphite Compiler
<http://scripts.sil.org/RenderingGraphite>. Note that the Windows
GraphiteCompiler_2_4.exe runs well on Wine <http://www.winehq.org/>. On
Mac OS X it might be easier to run GraphiteCompiler_2_4.exe through
Wine than building the Unix grcompiler.

After both the Graphite compiler and FontForge are installed, go to a
directory that contains the three following files:

	FreeMonoTengwar.sfd
	FreeMonoTengwar.gdl
	makefonts.py

Then run the following command:

	python makefonts.py

This will generate a bunch of files. The most important one is
FreeMonoTengwar.ttf, a version of FreeMonoTengwar with Graphite
support.

Note that makefonts.py also creates FreeMonoTengwar-embedding, a
smaller version of FreeMonoTengwar. This step requires another small
utility, taviso's free ttf2eot <http://code.google.com/p/ttf2eot/>.

If you are using the Windows GraphiteCompiler_2_4.exe, then the script
makefonts.py will probably not find the Graphite compiler. This means
it will only create the file FreeMonoTengwar_nogr.ttf without Graphite
support. Two solutions: Either don't worry and use the Graphite
compiler manually. Or create your own "grcompiler" that will redirect
to the Windows GraphiteCompiler_2_4.exe. If for instance you have
installed GraphiteCompiler_2_4.exe on Mac OS X using Wine, then your
"grcompiler" could be an executable file that contains but the
following line:

	wine ~/.wine/drive_c/Program\ Files/Graphite\ Compiler/GrCompiler.exe "$@"


Licensing
=========

The Free Tengwar Font Project is free software: You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

The Free Tengwar Font Project fonts are distributed in the hope that
they will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with the Free Tengwar Font Project. If not, see
<http://www.gnu.org/licenses/>.

As a special exception, if you create a document which uses a Free
Tengwar Font Project font, and embed that font or unaltered portions of
that font into the document, that font does not by itself cause the
resulting document to be covered by the GNU General Public License. This
exception does not however invalidate any other reasons why the document
might be covered by the GNU General Public License. If you modify that
font, you may extend this exception to your version of that font, but
you are not obligated to do so. If you do not wish to do so, delete this
exception statement from your version.

Please note that for you to use J. R. R. Tolkien's tengwar script in a
commercial production you may need permission from the Tolkien Estate.


Credits
=======

Most credits go to the contributors of the GNU FreeFonts since this
font includes all of the 2009-01-04 GNU FreeFont's FreeMono.sfd. There
are two additional contributors:


* j. 'mach' wust <j_mach_wust AT shared-files.de>

J. 'mach' wust added tengwar glyphs.

* Johan Winge <johan.winge AT telia.com>

Johan Winge added Graphite support (since FreeMonoTengwar version 2010-01-18).


Here follows without alterations the original CREDITS file of the
2009-01-04 GNU FreeFont:

This file lists contributors and contributions to the GNU FreeFont project.


* URW++ Design & Development GmbH <http://www.urwpp.de/>

URW++ donated a set of 35 core PostScript Type 1 fonts to the
Ghostscript project <http://www.cs.wisc.edu/~ghost/>, to be available
under the terms of GNU General Public License (GPL).

	Basic Latin				(U+0041-U+007A)
	Latin-1 Supplement                      (U+00C0-U+00FF)
	Latin Extended-A                        (U+0100-U+017F)
	Spacing Modifier Letters		(U+02B0-U+02FF)
	Mathematical Operators			(U+2200-U+22FF)
	Block Elements				(U+2580-U+259F)
	Dingbats				(U+2700-U+27BF)


* Yannis Haralambous <yannis.haralambous AT enst-bretagne.fr> and John
  Plaice <plaice AT omega.cse.unsw.edu.au>

Yannis Haralambous and John Plaice are the authors of Omega typesetting
system, <http://omega.enstb.org/>. Omega is an extension of TeX.
Its first release, aims primarily at improving TeX's multilingual abilities.
In Omega all characters and pointers into data-structures are 16-bit wide,
instead of 8-bit, thereby eliminating many of the trivial limitations of TeX.
Omega also allows multiple input and output character sets, and uses
programmable filters to translate from one encoding to another, to perform
contextual analysis, etc. Internally, Omega uses the universal 16-bit Unicode
standard character set, based on ISO-10646. These improvements not only make
it a lot easier for TeX users to cope with multiple or complex languages,
like Arabic, Indic, Khmer, Chinese, Japanese or Korean, in one document, but
will also form the basis for future developments in other areas, such as
native color support and hypertext features. ... Fonts for UT1 (omlgc family)
and UT2 (omah family) are under development: these fonts are in PostScript
format and visually close to Times and Helvetica font families. 
Omega fonts are available subject to GPL

	Latin Extended-B                        (U+0180-U+024F)
	IPA Extensions				(U+0250-U+02AF)
	Greek					(U+0370-U+03FF)
	Armenian				(U+0530-U+058F)
	Hebrew					(U+0590-U+05FF)
	Arabic					(U+0600-U+06FF)
	Currency Symbols			(U+20A0-U+20CF)
	Arabic Presentation Forms-A		(U+FB50-U+FDFF)
	Arabic Presentation Forms-B		(U+FE70-U+FEFF)

Current info: <http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=omega>

* Valek Filippov <frob AT df.ru>

Valek Filippov added Cyrillic glyphs and composite Latin Extended A to
the whole set of the abovementioned URW set of 35 PostScript core fonts,
<ftp://ftp.gnome.ru/fonts/urw/>. The fonts are available under GPL.

	Latin Extended-A                        (U+0100-U+017F)
	Cyrillic				(U+0400-U+04FF)


* Wadalab Kanji Comittee

Between April 1990 and March 1992, Wadalab Kanji Comittee put together
a series of scalable font files with Japanese scripts, in four forms:
Sai Micho, Chu Mincho, Cho Kaku and Saimaru. The font files are
written in custom file format, while tools for conversion into
Metafont and PostScript Type 1 are also supplied. The Wadalab Kanji
Comittee has later been dismissed, and the resulting files can be now
found on the FTP server of the Depertment of Mathematical Engineering
and Information Physics, Faculty of Engineering, University of Tokyo
<ftp://ftp.ipl.t.u-tokyo.ac.jp/Font/>.

	Hiragana				(U+3040-U+309F)
	Katakana				(U+30A0-U+30FF)


* Young U. Ryu <ryoung AT utdallas.edu>

Young Ryu is the author of Txfonts, a set of mathematical symbols
designed to accompany text typeset in Times or its variants. In the
documentation, Young adresses the design of mathematical symbols: "The
Adobe Times fonts are thicker than the CM fonts. Designing math fonts
for Times based on the rule thickness of Times = , , + , / , < ,
etc. would result in too thick math symbols, in my opinion. In the TX
fonts, these glyphs are thinner than those of original Times
fonts. That is, the rule thickness of these glyphs is around 85% of
that of the Times fonts, but still thicker than that of the CM fonts."
TX fonts are are distributed under the GNU public license (GPL). 
<http://www.ctan.org/tex-archive/fonts/txfonts/>.

	Arrows					(U+2190-U+21FF)
	Mathematical Symbols			(U+2200-U+22FF)


* Angelo Haritsis <ah AT computer.org>

Angelo Haritsis has compiled a set of Greek Type 1 fonts, available on
<ftp://ftp.hellug.gr/pub/unix/linux/GREEK/fonts/greekXfonts-Type1-1.1.tgz>.
The glyphs from this source has been used to compose Greek glyphs in
FreeSans and FreeMono.

Angelo's licence says: "You can enjoy free use of these fonts for
educational or commercial purposes.  All derived works should include
this paragraph.  If you want to change something please let me have
your changes (via email) so that they can go into the next
version. You can also send comments etc to the above address."

	Greek					(U+0370-U+03FF)


* Yannis Haralambous and Virach Sornlertlamvanich

In 1999, Yannis Haralambous and Virach Sornlertlamvanich made a set of
glyphs covering the Thai national standard Nf3, in both upright and
slanted shape. The collection of glyphs have been made part of GNU
intlfonts 1.2 package and is available under the GPL at
<ftp://ftp.gnu.org/pub/gnu/intlfonts/>.

	Thai					(U+0E00-U+0E7F)


* Shaheed R. Haque <srhaque AT iee.org>

Shaheed Haque has developed a basic set of basic Bengali glyphs
(without ligatures), using ISO10646 encoding. They are available under
the XFree86 license at <http://www.btinternet.com/~shaheedhaque/>.

Copyright (C) 2001 S.R.Haque <srhaque AT iee.org>.  All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL S.R.HAQUE BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of S.R.Haque shall not be
used in advertising or otherwise to promote the sale, use or other
dealings in this Software without prior written authorization from
S.R.Haque.

	Bengali					(U+0980-U+09FF)


* Sam Stepanyan <sam AT arminco.com>

Sam Stepanyan created a set of Armenian sans serif glyphs visually
compatible with Helvetica or Arial. Available on
<http://www.editum.com.ar/mashtots/html/fonts/ara.tar.gz>. On
2002-01-24, Sam writes: "Arial Armenian font is free for
non-commercial use, so it is OK to use under GPL license."

	Armenian				(U+0530-U+058F)


* Mohamed Ishan <ishan AT mitf.f2s.com>

Mohamed Ishan has started a Thaana Unicode Project
<http://thaana.sourceforge.net/> and among other things created a
couple of Thaana fonts, available under FDL or BDF license.

	Thaana					(U+0780-U+07BF)


* Sushant Kumar Dash <sushant AT writeme.com> (*)

Sushant Dash has created a font in his mother tongue, Oriya. As he
states on his web page <http://members.tripod.com/~sushantdash/>:
"Please feel free to foreword this mail to your Oriya friends. No
copyright law is applied for this font. It is totally free!!! Feel
free to modify this using any font editing tools. This is designed for
people like me, who are away from Orissa and want to write letters
home using Computers, but suffer due to unavailability of Oriya
fonts.(Or the cost of the available packages are too much)."

	Oriya					(U+0B00-U+0B7F)


* Harsh Kumar <harshkumar AT vsnl.com>

Harsh Kumar has started BharatBhasha <http://www.bharatbhasha.net/> -
an effort to provide "FREE software, Tutorial, Source Codes
etc. available for working in Hindi, Marathi, Gujarati, Gurmukhi and
Bangla. You can type text, write Web pages or develop Indian Languages
Applications on Windows and on Linux. We also offer FREE help to
users, enthusiasts and software developers for their work in Indian
languages."

	Devanagari				(U+0900-U+097F)
	Bengali					(U+0980-U+09FF)
	Gurmukhi				(U+0A00-U+0A7F)
	Gujarati				(U+0A80-U+0AFF)


* Prasad A. Chodavarapu <chprasad AT hotmail.com>

Prasad A. Chodavarapu created Tikkana, a Telugu font available in Type
1 and TrueType format on <http://chaitanya.bhaavana.net/fonts/>. 
Tikkana exceeds the Unicode Telugu range with some composite glyphs.
Available under the GNU General Public License.

	Telugu					(U+0C00-U+0C7F)


* Frans Velthuis <velthuis AT rc.rug.nl> and Anshuman Pandey
  <apandey AT u.washington.edu>

In 1991, Frans Velthuis from the Groningen University, The
Netherlands, released a Devanagari font as Metafont source, available
under the terms of GNU GPL. Later, Anshuman Pandey from the Washington
University, Seattle, USA, took over the maintenance of font. Fonts can
be found on CTAN, <ftp://ftp.dante.de/tex-archive/language/devanagari/>. I
converted the font to Type 1 format using Péter Szabó's TeXtrace
program <http://www.inf.bme.hu/~pts/textrace/> and removed some
redundant control points with PfaEdit.

	Devanagari				(U+0900-U+097F)


* Hardip Singh Pannu <HSPannu AT aol.com>

In 1991, Hardip Singh Pannu has created a free Gurmukhi TrueType font,
available as regular, bold, oblique and bold oblique form. Its license
says "Please remember that these fonts are copyrighted (by me) and are
for non-profit use only." 

	Gurmukhi				(U+0A00-U+0A7F)


* Jeroen Hellingman <jehe AT kabelfoon.nl>

Jeroen Hellingman created a set of Malayalam metafonts in 1994, and a
set of Oriya metafonts in 1996. Malayalam fonts were created as
uniform stroke only, while Oriya metafonts exist in both uniform and
modulated stroke. From private communication: "It is my intention to
release the fonts under GPL, but not all copies around have this
notice on them." Metafonts can be found on CTAN,
<ftp://ftp.dante.de/tex-archive/language/oriya/> and
<ftp://ftp.dante.de/tex-archive/language/malayalam/>.

	Oriya					(U+0B00-U+0B7F)
	Malayalam				(U+0D00-U+0D7F)


* Thomas Ridgeway <> (*)

Thomas Ridgeway, then at the Humanities And Arts Computing Center,
Washington University, Seattle, USA, (now defunct), created a Tamil
metafont in 1990. Anshuman Pandey from the same university took over
the maintenance of font. Fonts can be found at CTAN,
<ftp://ftp.dante.de/tex-archive/language/tamil/wntamil/>.

	Tamil					(U+0B80-U+0BFF)


* Berhanu Beyene <1beyene AT informatik.uni-hamburg.de>,
  Prof. Dr. Manfred Kudlek <kudlek AT informatik.uni-hamburg.de>, Olaf
  Kummer <kummer AT informatik.uni-hamburg.de>, and Jochen Metzinger <?>

Beyene, Kudlek, Kummer and Metzinger from the Theoretical Foundations
of Computer Science, University of Hamburg, prepared a set of Ethiopic
metafonts, found on
<ftp://ftp.dante.de/tex-archive/language/ethiopia/ethiop/>. They also
maintain home page on the Ethiopic font project,
<http://www.informatik.uni-hamburg.de/TGI/mitarbeiter/wimis/kummer/ethiop_eng.html>,
and can be reached at <ethiop AT informatik.uni-hamburg.de>. The current
version of fonts is 0.7 (1998), and they are released under GNU GPL. I
converted the fonts to Type 1 format using Péter Szabó's TeXtrace-A
program <http://www.inf.bme.hu/~pts/textrace/> and removed some
redundant control points with PfaEdit.

	Ethiopic				(U+1200-U+137F)


* Maxim Iorsh <iorsh AT users.sourceforge.net>

In 2002, Maxim Iorsh started the Culmus project, aiming at providing
Hebrew-speaking Linux and Unix community with a basic collection of
Hebrew fonts for X Windows. The fonts are visually compatible with
URW++ Century Schoolbook L, URW++ Nimbus Sans L and URW++ Nimbus Mono
L families, respectively, and are released under GNU GPL license. See
also <http://culmus.sourceforge.net/>.

	Hebrew					(U+0590-U+05FF)


* Panayotis Katsaloulis <panayotis AT panayotis.com>

Panayotis Katsaloulis helped fixing Greek accents in the Greek
Extended area.

	Greek Extended				(U+1F00-U+1FFF)


* Vyacheslav Dikonov <sdiconov AT mail.ru>

Vyacheslav Dikonov made a Braille unicode font that could be merged
with the UCS fonts to fill the 2800-28FF range completely. (uniform
scaling is possible to adapt it to any cell size). He also contributed
a free syriac font, whose glyphs (about half of them) are borrowed
from the "Carlo Ator" font freely downloadable from
<http://www.aacf.asso.fr/>. Vyacheslav also filled in a few missing
spots in the U+2000-U+27FF area, e.g. the box drawing section, sets of
subscript and superscript digits and capital Roman numbers.

	Syriac					(U+0700-U+074A)
	Box Drawing				(U+2500-U+257F)
	Braille					(U+2800-U+28FF)


* M.S. Sridhar <mssridhar AT vsnl.com>

M/S Cyberscape Multimedia Limited, Mumbai, developers of Akruti
Software for Indian Languages (http://www.akruti.com/), have released
a set of TTF fonts for nine Indian scripts (Devanagari, Gujarati,
Telugu, Tamil, Malayalam, Kannada, Bengali, Oriya, and Gurumukhi)
under the GNU General Public License (GPL). You can download the fonts
from the Free Software Foundation of India WWW site
(http://www.gnu.org.in/akruti-fonts/) or from the Akruti website.

For any further information or assistance regarding these fonts,
please contact mssridhar AT vsnl.com.

	Devanagari				(U+0900-U+097F)
	Bengali					(U+0980-U+09FF)
	Gurmukhi				(U+0A00-U+0A7F)
	Gujarati				(U+0A80-U+0AFF)
	Oriya					(U+0B00-U+0B7F)
	Tamil					(U+0B80-U+0BFF)
	Telugu					(U+0C00-U+0C7F)
	Kannada					(U+0C80-U+0CFF)	
	Malayalam				(U+0D00-U+0D7F)


* DMS Electronics, The Sri Lanka Tipitaka Project, and Noah Levitt
  <nlevitt AT columbia.edu>

Noah Levitt found out that the Sinhalese fonts available on the site
<http://www.metta.lk/fonts/> are released under GNU GPL, or,
precisely, "Public Domain under GNU Licence
 Produced by DMS
Electronics for The Sri Lanka Tipitaka Project" (taken from the font
comment), and took the effort of recoding the font to Unicode.

	Sinhala					(U+0D80-U+0DFF)
       

* Daniel Shurovich Chirkov <dansh AT chirkov.com>

Dan Chirkov updated the FreeSerif font with the missing Cyrillic
glyphs needed for conformance to Unicode 3.2. The effort is part of
the Slavjanskij package for Mac OS X,
<http://www.versiontracker.com/dyn/moreinfo/macosx/18680>.

	Cyrillic				(U+0400-U+04FF)


* Denis Jacquerye <moyogo AT gmail.com>

Denis Jacquerye added new glyphs and corrected existing ones in the
Latin Extended-B and IPA Extensions ranges.

	Latin Extended-B                        (U+0180-U+024F)
	IPA Extensions				(U+0250-U+02AF)


* K.H. Hussain <hussain AT kfri.org> and R. Chitrajan

`Rachana' in Malayalam means `to write', `to create'. Rachana Akshara Vedi,
a team of socially committed information technology professionals and
philologists, has applied developments in computer technology and desktop
publishing to resurrect the Malayalam language from the disorder,
fragmentation and degeneration it had suffered since the attempt to adapt
the Malayalam script for using with a regular mechanical typewriter, which
took place in 1967-69. K.H. Hussein at the Kerala Forest Research Institute
has released "Rachana Normal" fonts with approximately 900 glyphs required
to typeset traditional Malayalam. R. Chitrajan apparently encoded the
glyphs in the OpenType table.

In 2008, the Malayalam ranges in FreeSerif were updated under the advise 
and supervision of Hiran Venugopalan of Swathanthra Malayalam Computing,
to reflect the revised edition Rachana_04.

	Malayalam				(U+0D00-U+0D7F)


* Solaiman Karim <solaiman AT ekushey.org>

	Bengali					(U+0980-U+09FF)

Solaiman Karim has developed several OpenType Bangla fonts and
released them under GNU GPL on <http://www.ekushey.org>.


* Sonali Sonania <sonalisonania AT gmail.com> and Monika Shah
  <monikapatira AT gmail.com>

	Devanagari				(U+0900-U+097F)
	Gujarati				(U+0A80-U+0AFF)

Glyphs were drawn by Cyberscape Multimedia Ltd., #101,Mahalakshmi
Mansion 21st Main 22nd "A" Cross Banashankari 2nd stage Banglore
560070, India. Converted to OTF by IndicTrans Team, Powai, Mumbai,
lead by Prof. Jitendra Shah. Maintained by Monika Shah and Sonali
Sonania of janabhaaratii Team, C-DAC, Mumbai. This font is released
under GPL by Dr. Alka Irani and Prof Jitendra Shah, janabhaaratii
Team, C-DAC, Mumabi. janabhaaratii is localisation project at C-DAC
Mumbai (formerly National Centre for Software Technology); funded by
TDIL, Govt. of India. Contact:monika_shah AT lycos.com,
sonalisonania AT yahoo.com, jitendras AT vsnl.com, alka AT ncst.ernet.in.
website: www.janabhaaratii.org.in.


* Pravin Satpute <pravin_ind21 AT hotmail.com>, Bageshri Salvi
  <sbagrshri AT yahoo.co.in>, Rahul Bhalerao <rahul_pb_india AT
  yahoo.com> and Sandeep Shedmake <surgs2k47 AT yahoo.co.in>

	Devanagari				(U+0900-U+097F)
	Gujarati				(U+0A80-U+0AFF)
	Oriya					(U+0B00-U+0B7F)
	Malayalam				(U+0D00-U+0D7F)
	Tamil					(U+0B80-U+0BFF)

In December 2005 the team at www.gnowledge.org released a set of two
Unicode pan-Indic fonts: "Samyak" and "Samyak Sans". "Samyak" font
belongs to serif style and is an original work of the team; "Samyak
Sans" font belongs to sans serif style and is actually a compilation
of already released Indic fonts (Gargi, Padma, Mukti, Utkal, Akruti
and ThendralUni). Both fonts are based on Unicode standard. You can
download the font files (released under GNU/GPL License) from
http://www.gnowledge.org/Gnoware/localization/font.htm


* Kulbir Singh Thind

	Gurmukhi				(U+0A00-U+0A7F)

Dr. Kulbir Singh Thind designed a set of Gurmukhi Unicode fonts,
AnmolUni and AnmolUni-Bold, which are available under the terms of GNU
Generel Public Licens from the Punjabu Computing Resource Center,
http://guca.sourceforge.net/typography/fonts/anmoluni/.


* Gia Shervashidze <giasher AT telenet.ge>

        Georgian				(U+10A0-U+10FF)

Starting in mid-1990s, Gia Shervashidze designed many
Unicode-compliant Georgian fonts: Times New Roman Georgian, Arial
Georgian, Courier New Georgian. His work on Georgian localization can
be reached at http://www.gia.ge/.


* Primož Peterlin <primoz.peterlin AT biofiz.mf.uni-lj.si>

Primož Peterlin filled in missing glyphs here and there (e.g. Latin
Extended-B and IPA Extensions ranges in the FreeMono familiy), and
created the following UCS blocks:

	Latin Extended-B                        (U+0180-U+024F)
	IPA Extensions				(U+0250-U+02AF)
	Arrows					(U+2190-U+21FF)
	Box Drawing				(U+2500-U+257F)
	Block Elements				(U+2580-U+259F)
	Geometrical Shapes			(U+25A0-U+25FF)

* Mark Williamson

Made the MPH 2 Damase font, from which 
	Hanunóo                                 (U+1720-U+173F)
	Buginese                                (U+1A00-U+1A1F)
	Tai Le                                  (U+1950-U+197F)
	Ugaritic                                (U+10380-U+1039F)
	Old Persian                             (U+103A0-U+103DF)

* Jacob Poon

Submitted a very thorough survey of glyph problems and other suggestions.

* Alexey Kryukov

Made the TemporaLCGUni fonts, based on the URW++ fonts, from which at one 
point FreeSerif Cyrillic, and some of the Greek, was drawn.  He also provided
valuable direction about Cyrillic and Greek typesetting.

* George Douros

The creator of several fonts focusing on ancient scripts and symbols.
Many of the glyphs are created by making outlines from scanned images
of ancient sources.

	Aegean:   Phoenecian
	Analecta: Gothic                        (U+10330-U+1034F)
	Musical:  Byzantine & Western                  
	Unicode:  many Miscellaneous Symbols, Miscellaneous Technical,
	          supplemental Symbols, and Mathematical Alphanumeric symbols,
		  Mah Jong, and the outline of the Domino.

* Daniel Johnson

Created by hand a Cherokee range specially for FreeFont to be "in line with
the classic Cherokee typefaces used in 19th century printing", but also to
fit well with ranges previously in FreeFont.
	Cherokee                                (U+13A0-U+13FF)

Notes:

*: The glyph collection looks license-compatible, but its author has
   not yet replied and agreed on their work being used in part of
   this glyph collection.


--------------------------------------------------------------------------
This README.txt file is based on the original 2009-01-04 GNU FreeFont
files README,v 1.6 2008/12/25, INSTALL, v 1.7 2008/12/26, and CREDITS,v
1.23 2009/01/04, all of them by Steve White <stevan.white AT googlemail.com>

README.txt 2009-01-19, j. 'mach' wust <j_mach_wust AT shared-files.de>
