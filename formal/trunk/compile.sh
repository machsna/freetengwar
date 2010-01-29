#!/bin/bash

fontforge -script dansmith2unicode.py
grcompiler TengwarFormalUC.gdl TengwarFormalUC_dumb.ttf TengwarFormalUC.ttf
ftxenhancer -m TengwarFormalUC.mif TengwarFormalUC.ttf
