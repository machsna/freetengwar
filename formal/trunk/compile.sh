#!/bin/bash

fontforge -script dansmith2unicode.py

CpMac TengwarFormalUC_dumb.ttf TengwarFormalUC-shortCarrierInsertion_nogr.ttf
ftxenhancer -m TengwarFormalUC-shortCarrierInsertion.mif TengwarFormalUC-shortCarrierInsertion_nogr.ttf

ftxenhancer -m TengwarFormalUC.mif TengwarFormalUC_dumb.ttf
grcompiler TengwarFormalUC.gdl TengwarFormalUC_dumb.ttf TengwarFormalUC.ttf
