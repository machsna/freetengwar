#!/bin/bash
mkdir ../tags/$(date "+%Y-%m-%d")
cd ../tags/$(date "+%Y-%m-%d")
cp ../../trunk/FontLog.txt ../../trunk/GPL.txt .
mkdir source
cp ../../trunk/FreeMonoTengwar.sfd ../../trunk/FreeMonoTengwar.gdl ../../trunk/makefonts.py source/
cd source/
fontforge -script makefonts.py
mv FreeMonoTengwar.ttf FreeMonoTengwar.otf ..
rm *
cd ..
cp ../../trunk/FreeMonoTengwar.sfd ../../trunk/FreeMonoTengwar.gdl ../../trunk/makefonts.py source/
cd ..
zip FreeMonoTengwar.$(date "+%Y-%m-%d").zip $(date "+%Y-%m-%d")/*txt $(date "+%Y-%m-%d")/FreeMonoTengwar.* $(date "+%Y-%m-%d")/source/* 
