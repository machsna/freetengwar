#!/bin/bash

# fontforge -script dansmith2unicode.py
grcompiler TengwarFormalUC.gdl TengwarFormalUnicode-Regular.ttf TengwarFormalUC.ttf
ftxenhancer -m TengwarFormalUC.mif TengwarFormalUC.ttf
