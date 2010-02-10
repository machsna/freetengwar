#!/bin/bash

fontforge -script dansmith2unicode.py

ftxenhancer -m TengwarFormalUC.mif TengwarFormalUC_dumb.ttf
grcompiler TengwarFormalUC.gdl TengwarFormalUC_dumb.ttf TengwarFormalUC.ttf
