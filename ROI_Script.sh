#!/bin/bash

set -e
set -u

subject="R5045"
session="1"
Colour_Direction="Red-Green"

for ROIMasks in /home/o/ofh502/Project/masks/Bilateral/* ; do

ROI_File=$(basename ${ROIMasks})
ROI=$(echo ${ROI_File} | rev | cut -d'_' -f3- | rev )
echo ${ROI}

#for scan in /home/o/ofh502/Project/$subject/Session_$session/*/*${Colour_Direction}* ; do

#for scan in /home/o/ofh502/Project/$subject/Session_$session/*/*scan*SC.feat* ; do

for scan in /home/o/ofh502/Project/$subject/*/*/*scan*SC.feat* ; do

echo ${scan}
#File_name=$(basename ${scan})
#echo $File_name

#featquery 1 "${scan}" 3 ${scan}/stats/cope3.nii.gz ${scan}/stats/cope4.nii.gz ${scan}/stats/cope5.nii.gz ${ROI} -p ${ROIMasks} 

featquery 1 ${scan} 3 stats/pe1 stats/pe3 stats/pe5 $ROI -p -s ${ROIMasks} 



done
done
