#!/bin/bash

set -e
set -u

. /mnt/common/naf/initnaf

#Replace the X with the general project directory
General_Directory=$( echo X )

subject="R5045"
session="4"
scan="5"
echo "Generating FSF Files..."
counter=1

#Iterates through the first-level feat directories
#Both chromatic colours have hyphen in their folder name therefore can use this to identify them
for feat in ${General_Directory}/${subject}/Session_$session/scan_${scan}/*SC.feat ; do
	#echo ${feat}
	Scan_Name=$(basename ${feat})
	Scan_Name=$( echo "${Scan_Name}" | rev | cut -d'.' -f2- | rev )
	echo ${Scan_Name}
	Scan_Directory=$( echo "${feat}" | rev | cut -d'/' -f2- | rev )
	echo $Scan_Directory

#Applies deconvolution to the functional data which is already in MNI space
	#nafMRIEVDeconvolve -f ${feat} -s ${subject}_S${session}_${Scan_Name} -e ${Scan_Directory}/*CR ${Scan_Directory}/*FA ${Scan_Directory}/*H --ev-duration 2 --std-masks -m /groups/Projects/P1385/data/er/fsl/masks/Bilateral/V*.nii.gz

done

	
