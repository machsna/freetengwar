#!/bin/bash

##  Installation script for keyboard layouts, intended for Ubuntu.
##
##  Copyright (C) 2009-2015 Johan Winge
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.

LAYOUTFILE="ucteng"
SHORTDESC=""
DESCRIPTION="Tengwar CSUR QWERTY"
LANGUAGE="art"

## This script must be run as root.
if [ "$UID" -ne 0 ]
then
  echo; echo "You are not root; please start this script with sudo."; echo
  exit 85
fi  

## Installation directory has been the same since at least Ubuntu 8.04.
## Check that it still exists. (If it does, I presume it's right.)
TARGETDIR="/usr/share/X11/xkb/symbols/"
if [ ! -d $TARGETDIR ]
then
   echo; echo "ERROR: Target directory $TARGETDIR does not exist. Sorry, I don't know what to do now. Exiting."; echo
   exit 1
fi

## Where should we store the entry for the layout?
RULESFILE="/usr/share/X11/xkb/rules/evdev.xml"
if [ ! -f $RULESFILE ]
then
   echo; echo "Warning: Could not find $RULESFILE."
   RULESFILE="/etc/X11/xkb/base.xml"
   if [ ! -f $RULESFILE ]
   then
      echo "ERROR: Couldn't find $RULESFILE either! Sorry, I don't know what to do now. Exiting."; echo
      exit 1
   else
      echo "I will use $RULESFILE instead."; echo
   fi
fi

## Installation depends on xmlstarlet
which xmlstarlet &>/dev/null
if [ $? -ne 0 ]
then
   apt-get install xmlstarlet
   if [ $? -ne 0 ]
   then
     echo; echo "ERROR: Could not find nor install xmlstarlet, which is needed. Exiting."; echo
     exit 1
   fi
fi

## Copy the layout file
cp $LAYOUTFILE $TARGETDIR
if [ $? -ne 0 ]
then
  echo; echo "ERROR: Could not copy $LAYOUTFILE to $TARGETDIR. Exiting."; echo
  exit 1
fi

## Create a backup of the rules file
cp $RULESFILE $RULESFILE~
if [ $? -ne 0 ]
then
  echo; echo "ERROR: Could not create backup of $RULESFILE. Exiting."; echo
  exit 1
fi

## Add the layout to the LXDE layout list
LXPANELCFG="/usr/share/lxpanel/xkeyboardconfig/layouts.cfg"
if [ -f $LXPANELCFG ]
then
  cp $LXPANELCFG $LXPANELCFG~
  echo "$LAYOUTFILE = $DESCRIPTION" >> $LXPANELCFG
fi

## Copy the icon for LXDE
LXPANELICONDIR="/usr/share/lxpanel/images/xkb-flags/"
if [ -d $LXPANELICONDIR ]
then
   cp $LAYOUTFILE.png $LXPANELICONDIR
fi

## Copy the icon for Cinnamon
CINNAMONICONDIR="/usr/share/cinnamon/applets/keyboard@cinnamon.org/flags/"
if [ -d $CINNAMONICONDIR ]
then
   cp $LAYOUTFILE.png $CINNAMONICONDIR
fi

## Adding the layout to the list of installed layouts
ROT="/xkbConfigRegistry/layoutList/layout[last()]"
xmlstarlet ed -P \
 -d "/xkbConfigRegistry/layoutList/layout[configItem/name='$LAYOUTFILE']" \
 -s "/xkbConfigRegistry/layoutList" -t elem -n "layout" -v "
      " -i $ROT -t text -n "" -v "    " \
 -s $ROT -t elem -n "configItem" -v "
        " -s $ROT"/configItem" -t elem -n "name" -v "$LAYOUTFILE" \
 -s $ROT"/configItem" -t elem -n "shortDescription" -v "$SHORTDESC" \
 -s $ROT"/configItem" -t elem -n "description" -v "$DESCRIPTION" \
 -s $ROT"/configItem" -t elem -n "languageList" -v "" \
 -s $ROT"/configItem/languageList" -t elem -n "iso639Id" -v "$LANGUAGE" \
 -s $ROT -t elem -n "variantList" -v "" \
 -a $ROT"/configItem/name" -t text -n "" -v "
        " -a $ROT"/configItem/shortDescription" -t text -n "" -v "
        " -a $ROT"/configItem/description" -t text -n "" -v "
        " -a $ROT"/configItem/languageList" -t text -n "" -v "
      " -a $ROT"/configItem" -t text -n "" -v "
      " -a $ROT"/variantList" -t text -n "" -v "
    " -a $ROT -t text -n "" -v "
" $RULESFILE~ > $RULESFILE
if [ $? -ne 0 ]
then
  cp $RULESFILE~ $RULESFILE
  echo; echo "ERROR: Some error occured while editing $RULESFILE. Exiting."; echo
  exit 1
fi

## Generate uninstall script
echo "#!/bin/bash" > uninstall.sh
echo "sudo rm $TARGETDIR$LAYOUTFILE" >> uninstall.sh
echo "sudo mv $RULESFILE~ $RULESFILE" >> uninstall.sh
if [ -f $LXPANELCFG~ ]
then
  echo "sudo mv $LXPANELCFG~ $LXPANELCFG" >> uninstall.sh
fi
if [ -f $LXPANELICONDIR$LAYOUTFILE.png ]
then
  echo "sudo rm $LXPANELICONDIR$LAYOUTFILE.png" >> uninstall.sh
fi
if [ -f $CINNAMONICONDIR$LAYOUTFILE.png ]
then
  echo "sudo rm $CINNAMONICONDIR$LAYOUTFILE.png" >> uninstall.sh
fi
chmod +x uninstall.sh

## Success!
echo; echo "The file $LAYOUTFILE has been copied to $TARGETDIR, and $RULESFILE has been updated to reflect this. An uninstall script, uninstall.sh, has been generated."; echo "To ensure that the new layout is properly recognized, please restart your system before attempting to activate the layout."

exit 0

