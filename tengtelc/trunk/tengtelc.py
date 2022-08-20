import sys
import subprocess
import fontforge
import psMat
import re

weights = {
  100: 'Thin',
  200: 'Extra-Light',
  300: 'Light',
  400: 'Book',  # Huh, LibreOffice seems to conflate Medium with both Regular and Normal
  500: 'Medium',
  600: 'Semi-Bold',
  700: 'Bold',
  800: 'Extra-Bold',
  900: 'Black'
}

weight = int(sys.argv[1])
weightstring = weights[weight]

font = fontforge.open(f"latin{weight}.sfd")
font.mergeFonts(f"tengwar{weight}.sfd")
font.mergeFonts("underline.sfd")

font.familyname = "Tengwar Telcontar"
font.fontname = f"TengwarTelcontar-{weightstring.replace('-', '')}"
font.fullname = f"Tengwar Telcontar {weightstring}"
font.weight = weightstring
font.os2_weight = weight

font.appendSFNTName(0x409, 3, f"FontForge: {font.fullname} {font.version}")
font.appendSFNTName(0x409, 9, "Johan Winge")
font.appendSFNTName(0x409, 11, "http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409, 12, "http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409, 13, "Tengwar Telcontar is distributed under the terms of the GNU General Public License.")
font.appendSFNTName(0x409, 14, "http://www.gnu.org/copyleft/gpl.html")

for char in ("telco_leftdown","telco_leftdown_conl","telco_leftup","telco_leftshort","telco_leftshort_conl","telco_leftext",
             "telco_rightdown","telco_rightdown_conr","telco_rightdown2","telco_rightup","telco_rightup_conr",
             "telco_rightshort","telco_rightshort_conr","telco_rightshort_conrbot","telco_rightshort2","telco_rightshort2_conrbot","telco_rightext",
             "captelco_leftdown","captelco_leftup","captelco_leftshort","captelco_leftup2","captelco_leftshort2","captelco_leftext",
             "captelco_rightdown1","captelco_rightdown2","captelco_rightup","captelco_rightshort1","captelco_rightshort2","captelco_rightext",
             "closingbar_low1","closingbar_low1_conr","closingbar_low2","closingbar_low2_conr","closingbar_low2_desc",
             "closingbar_low3","closingbar_low3_conr","closingbar_low4","closingbar_low4_conr","closingbar_low4_desc",
             "closingbar_high1","closingbar_high1_conl","closingbar_high2","closingbar_high2_conr","closingbar_high2_conl","closingbar_high2_conb",
             "closingbar_high3","closingbar_high3_conl","closingbar_high4","closingbar_high4_conr","closingbar_high4_conl","closingbar_high4_conb",
             "capclosingbar_low1","capclosingbar_low2","capclosingbar_low3","capclosingbar_low4",
             "capclosingbar_high1","capclosingbar_high2","capclosingbar_high3","capclosingbar_high4",
             "teema1luuva","teema1luuva_conr","teema1luuvar","teema1luuvar_conr",
             "teema2luuva","teema2luuvar","teema3luuva","teema3luuvar","teema4luuva","teema4luuvar",
             "capteema1luuva","capteema1luuvar","capteema2luuva","capteema2luuvar",
             "capteema3luuva","capteema3luuvar","capteema4luuva","capteema4luuvar"):
  font[char].unlinkThisGlyph()
  font[char].clear()
#end for

# Clear the bitmaps
for char in font:
  font[char].clear(0)

font.selection.all()
font.removeOverlap()
with open('tracing.mf', 'r') as f:
  scalefactor = float(re.search(r'^scalefactor\s*=\s*([\d.]+)', f.read(), re.MULTILINE).group(1))
font.transform(psMat.scale(scalefactor))
font.round()
font.simplify(1.5, ("setstarttoextremum", "removesingletonpoints"), 0, 0, 5000)
font.round()
font.simplify(0, (), 0, 0, 5000)

font.mergeFonts("numerals.sfd")
font.encoding="unicode"
font.encoding="compacted"

font.os2_version=4  

font.save(font.fontname + ".sfd")
font.generate(f"tengtelc{weight}.ttf", "", ("omit-instructions"))
with open(f'tengtelc{weight}.gdl', 'w') as gdlfile:
  gdlfile.write('\n'.join([
    '#include "stddef.gdh"',
    '#define ps postscript',
    'AutoPseudo=0; // ?',
    f'#include "latin{weight}.gdh"',
    f'#include "tengwar{weight}.gdh"',
    '#include "underline.gdh"',
    '#include "latin.gdh"',
    '#include "tengwar.gdh"',
    '\n'
  ]))
subprocess.run(["grcompiler", "-v4", "-w3521", f"tengtelc{weight}.gdl", f"tengtelc{weight}.ttf", font.fontname + ".ttf"])

font = fontforge.open(font.fontname + ".sfd")
font.mergeFeature("tengtelc.fea")
font.generate(font.fontname + ".otf", flags=("opentype"))
