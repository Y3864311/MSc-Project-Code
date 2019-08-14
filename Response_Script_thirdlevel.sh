#!/bin/bash

set -e
set -u

# Replace the X with the general directory that contains the data.
General_Directory=$( echo X )

#H>CR is 1, FA>CR is 2
Contrast=1

echo "Generating FSF Files..."
#Counter starts at 10 otherwise if there are 10 copes and we start at 1, COPE10 will be read as (COPE1)0
counter=10

fsf_file=$( echo Group_thirdlevel_2Contrasts.fsf )
output_dir=$( echo ${General_Directory}/Project/ThirdLevel_2Contrasts)

cp ${General_Directory}/Third_Level_Analysis_Files/FSF_Template_thirdlevel_2Contrasts.fsf ${output_dir}/$fsf_file

for feat in ${General_Directory}/R*/Session*/session*Response_2Contrasts*/cope${Contrast}.feat; do
	
	session=$( echo COPE${counter})
	echo $session
	sed -i "s|OUTPUT|$output_dir/ThirdLevel_Contrast${Contrast}_Response_2Contrasts|" /${output_dir}/${fsf_file}
	sed -i "s|${session}|${feat}|" /${output_dir}/${fsf_file}
	let "counter+=1"

done


