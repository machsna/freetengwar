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

thefont.mergeFeature("FreeMonoTengwar.fea")

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

for char in ("tehtaE","tehtaEB","tehtaEE","tehtaEEB","tehtaN","tehtaB","tehtaGrave",
             "tengwarDoublesection","alda_tehtaB","lambe_tehtaB","lambeN_tehtaB"):
   thefont[char].unlinkRef()

thefont.selection.select(("ranges",None),0x0022,0xffff)
thefont.selection.select(("ranges","less"),0xe000,0xe0bf)
thefont.selection.select(("less",None),0x0028,0x0029,0x002c,0x002e,0x002f,0x003a,0x003b,0x003f,
                                       0x00a0,0x10fb,0x200c,0x200d,0x2018,0x2019,0x201c,0x201d,
                                       0x204a,0x2058,0x205d,0x25cc,0x2e2c,0x2e2d,0x2e31)
thefont.clear()

thefont.selection.select("tehtaAE","tehtaEE","lambe","alda","lambeN","tehtaB","tehtaE","osseN")
thefont.replaceWithReference()

thefont.save("FreeMonoTengwar-embedding.sfd")
thefont=fontforge.open("FreeMonoTengwar-embedding.sfd")
thefont.generate("FreeMonoTengwar-embedding.ttf","",("opentype","round"))

exit(0)

