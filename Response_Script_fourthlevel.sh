#!/bin/bash

set -e
set -u

# Replace the X with the general directory that contains the data.
General_Directory=$( echo X )

echo "Generating FSF Files..."

#H>CR is 1, FA>CR is 2
Contrast=1

#b-y = 1; lum = 2; r-y = 3
ColDir=1
if [[ ${ColDir} == 1 ]] ; then
	Colour=Blue-Yellow

elif [[ ${ColDir} == 2 ]] ; then
	Colour=Luminance

else
	Colour=Red-Green
fi

counter=1

fsf_file=$( echo Group_fourthlevel_2Contrasts.fsf )
output_dir=$( echo ${General_Directory}/FourthLevel_2Contrasts)

cp ${General_Directory}/Fourth_Level_Analysis/FSF_Template_fourthlevel_2Contrasts.fsf ${output_dir}/$fsf_file

for feat in ${General_Directory}/ThirdLevel_2Contrasts/Group_analysis*${Contrast}*/cope${ColDir}.feat/stats/cope*.nii.gz; do

	echo ${feat}		
	Participant=$( echo PARTICIPANT${counter})
	echo $Participant
	sed -i "s|OUTPUT|$output_dir/Contrast${Contrast}_${Colour}_Response_2Contrasts|" /${output_dir}/${fsf_file}
	sed -i "s|${Participant}|${feat}|" /${output_dir}/${fsf_file}
	let "counter+=1"

done


