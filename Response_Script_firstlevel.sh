#!/bin/bash

set -e
set -u

# Replace the X with the general directory that contains the data.
General_Directory=$( echo X )
subject="R5265"
session="1"


t1=$( echo ${General_Directory}/${subject}/Structural/*YNICT1A.nii.gz)
standard_brain=$( echo /usr/share/fsl/data/standard/MNI152_T1_2mm.nii.gz )
#Previously applied FNIRT transformation conducted by FEAT on the t1 image into standard space
t1_2_MNI=$( echo ${General_Directory}/${subject}/Structural/t1_2_MNI.nii.gz) 

echo "Generating FSF Files..."
counter=1


for functional in ${General_Directory}/$subject/Session_$session/scan*/*FMRI*.nii.gz ; do

	###############Registration###############

	#For each scan, transforms 1 volume of the functional data into t1 space
	flirt -in ${functional} -ref ${t1} -out ${General_Directory}/$subject/Session_$session/scan_${counter}/examplefunc_2_t1 -cost mutualinfo -dof 6 -searchrx -5 5 -searchry -5 5 -searchrz -5 5 -omat /	${General_Directory}/$subject/Session_$session/scan_${counter}/examplefunc_2_t1_matrix -v 


	#Applies the above transformation into t1 space to the rest of the scan's data, reducing the processing time
	flirt -in ${functional} -ref ${t1} -out ${General_Directory}/$subject/Session_$session/scan_${counter}/func_2_t1 -applyxfm -init ${General_Directory}/$subject/Session_$session/scan_${counter}/examplefunc_2_t1_matrix -v 

	func_2_t1=$( echo ${General_Directory}/$subject/Session_$session/scan_${counter}/func_2_t1 ) 

	#Applies the FNIRT transformation onto the functional data now in t1 space
	applywarp -i ${func_2_t1} -o ${General_Directory}/$subject/Session_$session/scan_${counter}/func_2_MNI -r ${standard_brain} -w ${General_Directory}/$subject/Structural/highres2standard_warp.nii.gz -v

	func_2_MNI=$( echo ${General_Directory}/$subject/Session_$session/scan_${counter}/func_2_MNI)
	
	###############FSF File Generation###############

	fsf_file=$( echo ${subject}_session_${session}_scan_${counter}_Response_2Contrasts.fsf )

# directory to add relevant files or folders into
	functional_dir=$(dirname ${functional})	
	output_dir=$( echo "$functional_dir" | rev | cut -d'/' -f1- | rev )

# parfile directories: H = Hits, FA = False Alarms, M = Misses and CR = Correct Rejections

	hits_timing=$( echo $output_dir/*ColDir*H )
	false_alarms_timing=$( echo $output_dir/*ColDir*FA)
	misses_timing=$( echo $output_dir/*ColDir*M)
	correct_reject_timing=$( echo $output_dir/*ColDir*CR)
	
# labels the output file depending on colour direction and scan
	condition_title=$( basename "$hits_timing")	
	if [[ $condition_title == *"ColDir1"* ]] ; then
		ColDir=Luminance

	elif [[ $condition_title == *"ColDir2"* ]] ; then
		ColDir=Blue-Yellow

	else
		ColDir=Red-Green
	fi

	output_directory=${output_dir}/${ColDir}_scan_${counter}_Response_2Contrasts
	
# makes a copy for each scan of a template fsf file which we will edit.
	cp ${General_Directory}/First_Level_Analysis_Files/FSF_Template.fsf ${output_dir}/$fsf_file

# Replaces strings in the copied template file with variables we have set in this code
# For instance "OUTPUT" in the template file is replaced with "${output_directory}" defined in this code

	sed -i "s|OUTPUT|${output_directory}|" /${output_dir}/${fsf_file}
	sed -i "s|FINPUT|${func_2_MNI}|" /${output_dir}/${fsf_file}
	sed -i "s|T1a|${t1_2_MNI}|" /${output_dir}/${fsf_file}
	sed -i "s|CONDITION_H|${hits_timing}|" /${output_dir}/${fsf_file}
	sed -i "s|CONDITION_FA|${false_alarms_timing}|" /${output_dir}/${fsf_file}
	sed -i "s|CONDITION_M|${misses_timing}|" /${output_dir}/${fsf_file}
	sed -i "s|CONDITION_CR|${correct_reject_timing}|" /${output_dir}/${fsf_file}

echo ">FSF File<"
echo ${output_dir}/${fsf_file}
echo ">Output Directory<"
echo $output_directory
echo ""
# counter keeps track of scan number
		let "counter+=1"
done

################ cluster submission #################
echo "Submitting FSF files to cluster..."

#submits all fsf files to the cluster.
for fsf in ${General_Directory}/$subject/Session_$session/*/R*Response2Contrasts.fsf ; do
	clusterFeat $fsf
done
echo "Done"
