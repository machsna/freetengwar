#!/usr/local/bin/fontforge

import sys
import os
import re
import fontforge

if len(sys.argv) != 2:
  print "This script extracts OpenType substitutions (GSUB) from a font and converts them into Graphite compiler format. Example:"
  print "  fontforge -script " + sys.argv[0] + " myfont.otf"
  print "This will generate myfont.fea and myfont.gdh."
  exit(1);

fontfilename=sys.argv[1]
feafilename=os.path.splitext(fontfilename)[0] + ".fea"
gdhfilename=os.path.splitext(fontfilename)[0] + ".gdh"

thefont=fontforge.open(fontfilename)
# Note: Only the first substitution lookup is output!
thefont.generateFeatureFile(feafilename,thefont.gsub_lookups[0])

feafile=open(feafilename,'rU')
gdhfile=open(gdhfilename,'w')
gdhfile.write("// This file is automatically generated by fea2gdh.py\n\n")
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

exit(0)

