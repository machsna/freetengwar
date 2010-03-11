#!/usr/local/bin/fontforge

## This script will generate the following files from FreeMonoTengwar.sfd:
##   FreeMonoTengwar.otf
##   FreeMonoTengwar_nogr.ttf
##   FreeMonoTengwar.fea
##   FreeMonoTengwar.gdh
##   FreeMonoTengwar.ttf
##   FreeMonoTengwar-embedding.sfd
##   FreeMonoTengwar-embedding_nogr.ttf
##   FreeMonoTengwar-embedding.eot
##   FreeMonoTengwar-embedding.ttf

import sys
import os
import re
import fontforge

thefont=fontforge.open("FreeMonoTengwar.sfd")

thefont.generate("FreeMonoTengwar.otf","",("opentype","round"))
thefont.generate("FreeMonoTengwar_nogr.ttf","",("opentype","round"))
thefont.generateFeatureFile("FreeMonoTengwar.fea",thefont.gsub_lookups[0])

## Generate FreeMonoTengwar.gdh

feafile=open("FreeMonoTengwar.fea",'rU')
gdhfile=open("FreeMonoTengwar.gdh",'w')
gdhfile.write("// This file is automatically generated\n\n")
gdhfile.write("table(substitution)\n");
fealine=feafile.readline()
while fealine!='':
  raw=re.search("    sub \\\\([\w]*) \\\\([\w]*)  by \\\\([\w]*);",fealine)
  if raw!=None: gdhfile.write('  ps("'+raw.group(1)+'") ps("'+raw.group(2)+'") > ps("'+raw.group(3)+'"):(1 2) _ ;\n')
  raw=re.search("    sub \\\\([\w]*) \\\\([\w]*) \\\\([\w]*)  by \\\\([\w]*);",fealine)
  if raw!=None: gdhfile.write('  ps("'+raw.group(1)+'") ps("'+raw.group(2)+'") ps("'+raw.group(3)+'") > ps("'+raw.group(4)+'"):(1 2 3) _ _ ;\n')
  fealine=feafile.readline()
gdhfile.write("endtable;\n\n")
feafile.close()
gdhfile.close()

os.system("ftxenhancer -m FreeMonoTengwar.mif FreeMonoTengwar_nogr.ttf")
os.system("grcompiler FreeMonoTengwar.gdl FreeMonoTengwar_nogr.ttf FreeMonoTengwar.ttf")

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
thefont.selection.select(("ranges","less"),0xe000,0xe07f)
thefont.selection.select(("less",None),0x0028,0x0029,0x002c,0x002e,0x002f,0x003a,0x003b,0x003f,
                                       0x00a0,0x10fb,0x200c,0x200d,0x2018,0x2019,0x201c,0x201d,
                                       0x204a,0x2058,0x205d,0x25cc,0x2e2c,0x2e2d,0x2e31)
thefont.clear()

thefont.selection.select("tehtaAE","tehtaEE","lambe","alda","lambeN","tehtaB","tehtaE","osseN")
thefont.replaceWithReference()

thefont.save("FreeMonoTengwar-embedding.sfd")
thefont=fontforge.open("FreeMonoTengwar-embedding.sfd")
thefont.generate("FreeMonoTengwar-embedding_nogr.ttf","",("opentype","round"))
os.system("ttf2eot FreeMonoTengwar-embedding_nogr.ttf > FreeMonoTengwar-embedding.eot")
os.system("ftxenhancer -m FreeMonoTengwar.mif FreeMonoTengwar-embedding_nogr.ttf")
os.system("grcompiler FreeMonoTengwar-reduced.gdl FreeMonoTengwar-embedding_nogr.ttf FreeMonoTengwar-embedding.ttf")

exit(0)

