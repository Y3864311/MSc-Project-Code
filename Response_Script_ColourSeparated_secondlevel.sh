#!/bin/bash

set -e
set -u

# Replace the X with the general directory that contains the data.
General_Directory=$( echo X )
subject="R5265"
session="1"

echo "Generating FSF Files..."
counter=1


fsf_file=$( echo ${subject}_session_${session}_2Contrasts.fsf )
output_dir=$( echo ${General_Directory}/${subject}/Session_${session}/)

cp ${General_Directory}/Second_Level_Analysis_Files/FSF_Template_secondlevel.fsf ${output_dir}/$fsf_file

array=( )


#Need to change the feat name below depending on feat output name
for feat in ${General_Directory}/${subject}/Session_$session/scan*/*Response_2Contrasts.feat ; do
	#echo ${feat}
	feat_file=$(basename ${feat})
	array[${counter}]=$feat_file
	let "counter+=1"
done


#Sorts the feat files into alphabetical order so each of the colour directions are in the same order for each session
array=($(for each in ${array[@]}; do echo $each; done | sort))
counter=1
for x in ${array[@]}; do
	scan="SCAN${counter}"
	scan_number=$(echo "$x" | cut -d '_' -f3- )
	scan_number=$(echo "$scan_number" | rev | cut -d '_' -f2- | rev )
	echo $scan_number
	scan_directory=$( echo ${General_Directory}/${subject}/Session_${session}/scan_${scan_number}/${x} )
	echo $scan_directory
	sed -i "s|${scan}|${scan_directory}|" /${output_dir}/${fsf_file}
	sed -i "s|OUTPUT|${output_dir}session_${session}_Response_2Contrasts|" /${output_dir}/${fsf_file}

	let "counter+=1"

done



# sets the newly creted feat directory folders to the group permissions.
#for feat_directory in /groups/Projects/P1385/data/er/fsl/subjects/$subject/Session_$session/scan_*/scan_*.feat ; do
#	chgrp -R p1385 $feat_directory
#done

