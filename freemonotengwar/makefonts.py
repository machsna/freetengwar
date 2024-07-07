#!/usr/local/bin/fontforge

## This script will generate the following files from FreeMonoTengwar.sfd:
##   FreeMonoTengwar.ttf
##   FreeMonoTengwar-embedding.sfd
##   FreeMonoTengwar-embedding.ttf

import sys
import os
import re
import fontforge

thefont=fontforge.open("FreeMonoTengwar.sfd")

# For testing purposes, append "-draft"  in font name
# TBD: remove this!
thefont.fontname=thefont.fontname+"-draft"
thefont.familyname=thefont.familyname+"-draft"
thefont.fullname=thefont.fullname+"-draft"

## Shift some glyphs by 600
#thefont.selection.select("atehta", "yatehta", "tixe", "tixe_etehta", "etehta", "etehta_etehta", "otehta", "utehta", "otehta_tixe", "utehta_tixe", "otehta_otehta", "utehta_utehta", "otehta_otehta_tixe", "utehta_utehta_tixe", "nengwetehta", "watehta", "watehta.alt", "ytehta", "etehtanuquerna", "etehtanuquerna_etehtanuquerna", "yantatehta", "atehtanuquerna", "unuatehta", "unuyatehta", "putta", "unuetehta", "unuetehta_unuetehta", "unuotehta", "unuutehta", "andatehta", "thinnas", "thinnas_putta", "combiningsarince.mark", "combiningsarince.alt", "tixeoverlay", "tengwardigitMark", "gravecomb", "acutecomb", "circumflexcmb", "tildecomb", "macroncomb", "overlinecmb", "brevecomb", "dotaccentcmb", "diaeresiscomb", "hookabovecomb", "ringcmb", "hungarumlautcmb", "caroncmb", "linevertnosp", "linevertdblnosp", "gravedblnosp", "breve_dotaccent", "uni0311", "horncmb", "hooksubpalatnosp", "hooksubretronosp", "cedillacmb", "ogonekcmb", "strokeshortoverlaycmb", "strokelongoverlaycmb", "slashshortnosp", "slashlongnosp", "perispomenigreekcmb", "dialytikatonoscmb", "ypogegrammenigreekcmb", "commasubnosp", "leftharpoonaccent", "rightharpoonaccent", "uni20D2", "uni20E1", "uni20EC", "uni20ED", "uni20EE", "uni20EF", "uni20D6", "uni20D7", "zwnj", "zwj", "afii300", "afii299", "dotbelowcomb", "macronbelowcmb", "uni033A", "uni032a", "uni0346", "uni20e2", "uni20DD", "uni20DE", "uni20DF", "uni20E0", "uni20DC", "uni20DB", "uni20e3", "uni0312", "uni0313", "uni0314", "uni031c", "uni0315", "ringrighthalfsubnosp", "uni0340", "uni0341", "uni034c", "uni0351", "uni0357", "uni031d", "uni031e", "uni031f", "tildeoverlaycmb", "uni0316", "uni0317", "uni0324", "uni0325", "uni0329", "uni032D", "uni032E", "uni032F", "uni032C", "uni0343", "uni0348", "uni034d", "uni0330", "uni0332", "uni0318", "uni0319", "uni0352", "uni0320", "uni0333", "uni033b", "overscoredblnosp", "uni0347", "uni031a", "uni032b", "uni033c", "uni033d", "uni033e", "uni0350", "uni0353", "uni0354", "uni0355", "uni0356", "uni0358", "uni0359", "uni035a", "uni0349", "uni034B")
#thefont.transform([1,0,0,1,-600,0])
#thefont.save("FreeMonoTengwar-moved.sfd")

thefont.mergeFeature("FreeMonoTengwar.fea")
thefont.save("FreeMonoTengwar-mergeFeature.sfd")
thefont.generateFeatureFile("FreeMonoTengwar-mergeFeature.sfd.fea")

thefont.generate("FreeMonoTengwar.ttf","",("opentype","round"))

## Generate the smaller Embedding version:

thefont.fontname=thefont.fontname+"-embedding"
thefont.familyname=thefont.familyname+"-embedding"
thefont.fullname=thefont.fullname+"-embedding"

newnames=[]
for name in thefont.sfnt_names:
   if name[0]=='English (US)':
      newnames.append(name)
thefont.sfnt_names=tuple(newnames)

for lookup in ("'mark' Mark Positioning in Greek", "'mark' Mark Positioning in Latin 1", "'mark' Mark Positioning in Latin 2"):
   thefont.removeLookup(lookup)

for char in ("etehta","unuetehta","etehta_etehta","unuetehta_unuetehta","nengwetehta","andatehta","etehtanuquerna",
             "tengwarDoublesection"):
   thefont[char].unlinkRef()

thefont.selection.select(("ranges",None),0x0022,0xffff)
thefont.selection.select(("ranges","less"),0xe000,0xe0bf)
thefont.selection.select(("less",None),0x0028,0x0029,0x002c,0x002e,0x002f,0x003a,0x003b,0x003f,
                                       0x00a0,0x10fb,0x200c,0x200d,0x2018,0x2019,0x201c,0x201d,
                                       0x204a,0x2058,0x205d,0x25cc,0x2e2c,0x2e2d,0x2e31)
thefont.clear()

thefont.selection.select("atehtanuquerna","etehta_etehta","lambe","alda","lambenuquerna","andatehta","etehta","ossenuquerna")
thefont.replaceWithReference()

thefont.save("FreeMonoTengwar-embedding.sfd")
thefont=fontforge.open("FreeMonoTengwar-embedding.sfd")
thefont.generate("FreeMonoTengwar-embedding.ttf","",("opentype","round"))

exit(0)

