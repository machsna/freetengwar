## Tengwar Telcontar - a Tengwar unicode typeface.
## Copyright (C) 2005-2007 Johan Winge
## 
## Tengwar Telcontar is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
## 
## As a special exception, if you create a document which uses this
## font, and embed this font or unaltered portions of this font into
## the document, this font does not by itself cause the resulting
## document to be covered by the GNU General Public License. This
## exception does not however invalidate any other reasons why the
## document might be covered by the GNU General Public License. If you
## modify this font, you may extend this exception to your version of
## the font, but you are not obligated to do so. If you do not wish to
## do so, delete this exception statement from your version.
## 
## Tengwar Telcontar is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Tengwar Telcontar; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

import sys
import re
import os
fn=sys.argv[1].strip();

print "Running MetaFont."
os.system("mf \"\\mode:=pixpt; mag:=200; input %s.mf\"" % fn)

print "Generating enc, pe and gdh file."
charnames=[]
for i in range(256):
  charnames.append('.notdef')
f=open(fn+'.log','rU')
pef=open(fn+'.pe','w')
gdf=open(fn+'.gdh','w')
logline=f.readline()
while logline!='':
  raw=re.search("^ec: ([A-Za-z_][A-Za-z0-9._]*) \[(\d{1,3})\]",logline)
  if raw!=None:
    if int(raw.group(2))<256:
      charnames[int(raw.group(2))]=raw.group(1)
    else:
      charnames.append(raw.group(1))
  raw=re.search("^pe: ([^\n]*)",logline)
  if raw!=None: pef.write(raw.group(1)+'\r\n')
  raw=re.search("^gd: ([^\n]*)",logline)
  if raw!=None: gdf.write(raw.group(1)+'\r\n')
  gf=re.search("^Output written on (\S*)",logline)
  logline=f.readline()
f.close()
pef.close()
gdf.close()
f=open(fn+'.enc','w')
f.write('/'+fn+' [ \n')
for i in range(len(charnames)):
  f.write('/'+charnames[i]+'\n')
f.write('] def\n')
f.close()

os.system("gftopk %s %s.pk" % (gf.group(1), fn))
os.system("fontforge -script %s.pe %s" % (fn,fn))
