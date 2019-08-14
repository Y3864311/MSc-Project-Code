#!/bin/bash

set -e
set -u

#. /mnt/common/naf/initnaf

for Parfiles in /home/o/ofh502/Project/R5161/Session_*/scan_*/*-*SC.feat/*SC-Timeseries/*; do


Parfile_Basename=$(basename ${Parfiles})
Timeseries_name=$( echo "${Parfile_Basename}" | cut -d'_' -f8-)
echo ${Timeseries_name}
Output_dir=$( echo ${Parfiles} | rev | cut -d'/' -f2- | rev)
echo $Output_dir

#cp ${Parfiles} ${Output_dir}/$Timeseries_name

done

#nafMRICompileTimeseriesCSV --indirs echo /home/o/ofh502/Project/R5161/Session*/scan_*/*-*SC.feat/*SC*Timeseries --conds CR FA H -m V1_thr_35 V2_thr_35 V3V_thr_35 V4_thr_35 V5_thr_35 -o '/home/o/ofh502/Project/MRI_TS/R5161/ChromaticColDir'

