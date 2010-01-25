#!/bin/bash

CpMac tengtelc.ttf tengtelc-ftx.ttf
CpMac tengtelcb.ttf tengtelcb-ftx.ttf
ftxdumperfuser -t post -o tengtelc-ftx.post.xml tengtelc-ftx.ttf 
ftxdumperfuser -t post -o tengtelcb-ftx.post.xml tengtelcb-ftx.ttf 
./addtengwarglyphnames.sh tengtelc-ftx.post.xml 
./addtengwarglyphnames.sh tengtelcb-ftx.post.xml 
ftxdumperfuser -t post -d tengtelc-ftx.post.xml tengtelc-ftx.ttf 
ftxdumperfuser -t post -d tengtelcb-ftx.post.xml tengtelcb-ftx.ttf 
ftxenhancer -m tengtelc-ftx.mif tengtelc-ftx.ttf
ftxenhancer -m tengtelc-ftx.mif tengtelcb-ftx.ttf
