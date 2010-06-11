#!/bin/bash

fontforge -script dansmith2unicode.py

cp TengwarFormalUC_dumb.ttf TengwarFormalUC_AAT.ttf
ftxenhancer -m TengwarFormalUC.mif TengwarFormalUC_AAT.ttf

grcompiler TengwarFormalUC.gdl TengwarFormalUC_AAT.ttf TengwarFormalUC.ttf
