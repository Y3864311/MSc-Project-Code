#!/bin/bash

set -e
set -u

. /mnt/common/naf/initnaf

#Replace the X with the general project directory
General_Directory=$( echo X )

subject="R5045"
session="4"

#Both chromatic colours have hyphen in their folder name therefore can use this to identify them
for Parfiles in ${General_Directory}/${subject}/Session_*/scan_*/*-*SC.feat/*SC-Timeseries/*; do


Parfile_Basename=$(basename ${Parfiles})
Timeseries_name=$( echo "${Parfile_Basename}" | cut -d'_' -f8-)
echo ${Timeseries_name}
Output_dir=$( echo ${Parfiles} | rev | cut -d'/' -f2- | rev)
echo $Output_dir

#cp ${Parfiles} ${Output_dir}/$Timeseries_name

done

nafMRICompileTimeseriesCSV --indirs echo ${General_Directory}/${subject}/Session*/scan_*/*-*SC.feat/*SC*Timeseries --conds CR FA H -m V1_thr_35 V2_thr_35 V3V_thr_35 V4_thr_35 V5_thr_35 -o "${General_Directory}/MRI_TS/${subject}/ChromaticColDir"

