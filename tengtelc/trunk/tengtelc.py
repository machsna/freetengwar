import sys
import fontforge
import psMat

if sys.argv[1]=="regular":
  font=fontforge.open("latinr.sfd")
  font.mergeFonts("tengwarr.sfd")
  font.fontname="tengtelc"
  font.fullname="Tengwar Telcontar"
  font.weight="Regular"
  sfdfilename="tengtelc.sfd"
  ttffilename="tengtelc_nogr.ttf"
elif sys.argv[1]=="bold":
  font=fontforge.open("latinb.sfd")
  font.mergeFonts("tengwarb.sfd")
  font.fontname="tengtelcb"
  font.fullname="Tengwar Telcontar Bold"
  font.weight="Bold"
  sfdfilename="tengtelcb.sfd"
  ttffilename="tengtelcb_nogr.ttf"
# endif

font.mergeFonts("underline.sfd")
font.familyname="Tengwar Telcontar"
font.appendSFNTName(0x409,3,"FontForge: " + font.fullname + " " + font.version)
font.appendSFNTName(0x409,9,"Johan Winge")
font.appendSFNTName(0x409,11,"http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409,12,"http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409,13,"Tengwar Telcontar is distributed under the terms of the GNU General Public License.")
font.appendSFNTName(0x409,14,"http://www.gnu.org/copyleft/gpl.html")

for char in ("telco_leftdown","telco_leftdown_conl","telco_leftup","telco_leftshort","telco_leftshort_conl","telco_leftext",
             "telco_rightdown","telco_rightdown_conr","telco_rightdown2","telco_rightup","telco_rightup_conr",
             "telco_rightshort","telco_rightshort_conr","telco_rightshort_conrbot","telco_rightshort2","telco_rightshort2_conrbot","telco_rightext",
             "captelco_leftdown","captelco_leftup","captelco_leftshort","captelco_leftup2","captelco_leftshort2","captelco_leftext",
             "captelco_rightdown1","captelco_rightdown2","captelco_rightup","captelco_rightshort1","captelco_rightshort2","captelco_rightext",
             "closingbar_low1","closingbar_low1_conr","closingbar_low2","closingbar_low2_conr","closingbar_low2_desc",
             "closingbar_low3","closingbar_low3_conr","closingbar_low4","closingbar_low4_conr","closingbar_low4_desc",
             "closingbar_high1","closingbar_high1_conl","closingbar_high2","closingbar_high2_conr","closingbar_high2_conl","closingbar_high2_conb",
             "closingbar_high3","closingbar_high3_conl","closingbar_high4","closingbar_high4_conr","closingbar_high4_conl","closingbar_high4_conb",
             "capclosingbar_high1","capclosingbar_high2","capclosingbar_high3","capclosingbar_high4",
             "teema1luuva","teema1luuva_conr","teema1luuvar","teema1luuvar_conr",
             "teema2luuva","teema2luuvar","teema3luuva","teema3luuvar","teema4luuva","teema4luuvar",
             "capteema1luuva","capteema1luuvar","capteema2luuva","capteema2luuvar",
             "capteema3luuva","capteema3luuvar","capteema4luuva","capteema4luuvar"):
  font[char].unlinkThisGlyph()
  font[char].clear()
#end for

# Clear the bitmaps (native script command ClearBackground();).
# This does not work at the moment. Bug?
for char in font:
  font[char].layers[0] = fontforge.layer()

font.selection.all()
font.removeOverlap()
font.transform(psMat.scale(1.25))  # Should match scale factor in tracing.mf
#font.addExtrema()
#font.simplify(2,("removesingletonpoints"),0,0,5000)
#font.round()
#font.simplify(2,("ignoreextrema"),0,0,5000)
#font.addExtrema()
#font.round()
#font.simplify(2,("setstarttoextremum"),0,0,5000)

font.mergeFonts("numerals.sfd")
font.encoding="unicode"
font.encoding="compacted"

# Older versions of grcompiler can't handle version=4 (fixed in SVN rev. 1105)
font.os2_version=3  

font.save(sfdfilename)
font.generate(ttffilename,"",("omit-instructions"))

