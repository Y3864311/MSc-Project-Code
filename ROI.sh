#!/bin/bash

set -e
set -u

#Replace the X with the general project directory
General_Directory=$( echo X)

subject=""
session=""
#Choose the colour direction: Red-Green; Blue-Yellow; Luminance
Colour_Direction="Red-Green"

for ROIMasks in ${General_Directory}/masks/Bilateral/* ; do

ROI_File=$(basename ${ROIMasks})
ROI=$(echo ${ROI_File} | rev | cut -d'_' -f3- | rev )
echo ${ROI}

for scan in ${General_Directory}/$subject/*/*/*scan*SC.feat* ; do

echo ${scan}


featquery 1 ${scan} 3 stats/pe1 stats/pe3 stats/pe5 $ROI -p -s ${ROIMasks} 



done
done
