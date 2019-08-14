import numpy as np, os, math
from os.path import join, splitext
import matplotlib.pyplot as plt
import glob
import fnmatch
from glob import glob
import os


# 1-4 = LUM [M H CR FA]
# 5-8 = S [M H CR FA]
# 9-12 = LM [M H CR FA]
Subject = "R5045"

general_hit = []
general_miss = []
general_cr = []
general_fa = []  
general_nr = []   

ZeroResponseParfilesDir = sorted(glob("/home/o/ofh502/Project/noResponseCoded0ParFiles/{}/*/*.par".format(Subject)))
#files = sorted(glob("/home/o/ofh502/Downloads/noResponseCoded0ParFiles/noResponseCoded0ParFiles/*/*/*.par"))


OnlyResponseDir_List = []
for Response in glob("/home/o/ofh502/Project/parFilesERDesignStim_ordered/{}/*/*.par".format(Subject)):
    OnlyResponseDir_List.append(Response)
#print(sorted(OnlyResponse_List))

#Zero Response Parfile ZRP
for ZRP_Dir in ZeroResponseParfilesDir:
    File_Name = os.path.basename(ZRP_Dir).split("_")
    Participant, ColDir, OptSec, = File_Name[5], File_Name[4], File_Name[3], 
    Matching_ORParfile = fnmatch.filter(OnlyResponseDir_List, "*{}*{}*{}*".format(Participant, OptSec, ColDir))
#    print(Zresponse_file)
#    print(Matching_ORParfile)
    ZR_Parfile = open(ZRP_Dir, "r")
    OR_Parfile = open(Matching_ORParfile[0], 'r')
#    print(ZR_Timings.readlines())
#    print(OR_Timings.readlines())
    hit = []
    miss = []
    cr = []
    fa = [] 
    nr = []    

    if "ColDir1" in ZRP_Dir:

        
        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
#            print(Matching_OR_Timing)
            if Parfile_Column[1] == "1":
                miss.append("Miss")
            elif Parfile_Column[1] == "2":
                hit.append("Hit")
            elif Parfile_Column[1] == "3":
                cr.append("Correct Reject")
            elif Parfile_Column[1] == "4":
                fa.append("False Alarms")
            elif Parfile_Column[1] == "0":
                nr.append("No Response")
                if Matching_OR_Timing[1] == "0":
                    cr.append("Correct Reject")
                elif Matching_OR_Timing[1] == "1":
                    miss.append("Miss")
                
                
                
    elif "ColDir2" in ZRP_Dir:       
        
        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
#            print Matching_OR_Timing[0], Matching_OR_Timing[1]
            if Parfile_Column[1] == "5":
                miss.append("Miss")
            elif Parfile_Column[1] == "6":
                hit.append("Hit")
            elif Parfile_Column[1] == "7":
                cr.append("Correct Reject")
            elif Parfile_Column[1] == "8":
                fa.append("False Alarms")
            elif Parfile_Column[1] == "0": 
                nr.append("No Response")
                if Matching_OR_Timing[1] == "0":
                    cr.append("Correct Reject")
                elif Matching_OR_Timing[1] == "2":
                    miss.append("Miss")
                
                
    elif "ColDir3" in ZRP_Dir:
       

        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
#            print Matching_OR_Timing[0], Matching_OR_Timing[1]
            if Parfile_Column[1] == "9":
                miss.append("Miss")
            elif Parfile_Column[1] == "10":
                hit.append("Hit")
            elif Parfile_Column[1] == "11":
                cr.append("Correct Reject")
            elif Parfile_Column[1] == "12":
                fa.append("False Alarms")
            elif Parfile_Column[1] == "0": 
                nr.append("No Response")
                if Matching_OR_Timing[1] == "0":
                    cr.append("Correct Reject")
                elif Matching_OR_Timing[1] == "3":
                    miss.append("Miss")
    general_hit.extend(hit)
    general_miss.extend(miss)
    general_cr.extend(cr)
    general_fa.extend(fa)
    general_nr.extend(nr)
                
    
    
#print(hit)
#print(len(miss))
#print(cr)
#print(fa)