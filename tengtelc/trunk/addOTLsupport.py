import sys
import fontforge

if sys.argv[1]=="regular":
  font=fontforge.open("tengtelc.sfd")
  font.fontname="tengtelcOTL"
  font.familyname="Tengwar Telcontar OTL"
  font.fullname="Tengwar Telcontar OTL"
  sfdfilename="tengtelcOTL.sfd"
  ttffilename="tengtelcOTL.ttf"
elif sys.argv[1]=="bold":
  font=fontforge.open("tengtelcb.sfd")
  font.fontname="tengtelcbOTL"
  font.familyname="Tengwar Telcontar OTL"
  font.fullname="Tengwar Telcontar OTL Bold"
  sfdfilename="tengtelcbOTL.sfd"
  ttffilename="tengtelcbOTL.ttf"
# endif

font.mergeFeature("tengtelc.fea")

font.save(sfdfilename)
font.generate(ttffilename)

