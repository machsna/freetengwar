#!/bin/bash
mkdir ../tags/$(date "+%Y-%m-%d")
cd ../tags/$(date "+%Y-%m-%d")
cp ../../trunk/FontLog.txt ../../trunk/GPL.txt .
mkdir source
cp ../../trunk/FreeMonoTengwar.sfd ../../trunk/FreeMonoTengwar.gdl ../../trunk/makefonts.py source/
cd source/
fontforge -script makefonts.py
mv FreeMonoTengwar-embedding.ttf FreeMonoTengwar-embedding.eot ..
rm *
cd ..
cp ../../trunk/FreeMonoTengwar.sfd ../../trunk/FreeMonoTengwar.gdl ../../trunk/makefonts.py source/
cd ..
zip FreeMonoTengwar-embedding.$(date "+%Y-%m-%d").zip $(date "+%Y-%m-%d")/*txt $(date "+%Y-%m-%d")/FreeMonoTengwar-embedding* $(date "+%Y-%m-%d")/source/* 
