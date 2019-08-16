from os.path import join, splitext
import fnmatch
from glob import glob
import os

#Enter the general directory where both timing files are stored
General_Directory = ""

# 1-4 = LUM [M H CR FA]
# 5-8 = S [M H CR FA]
# 9-12 = LM [M H CR FA]

Subject = ""

general_hit = []
general_miss = []
general_cr = []
general_fa = []     

ZeroResponseParfilesDir = sorted(glob("{}/noResponseCoded0ParFiles/R5265/20190503/*.par".format(General_Directory)))


OnlyResponseDir_List = []
for Response in glob("{}/parFilesERDesignStim_ordered/R5265/20190503/*.par".format(General_Directory)):
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
        
        hit_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_H" 
        miss_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_M"
        cr_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_CR"
        fa_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_FA"
        
        hit_file = open(hit_filename, "w")
        miss_file = open(miss_filename, "w")
        cr_file = open(cr_filename, "w")
        fa_file = open(fa_filename, "w")
        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
#            print(Matching_OR_Timing)
            if Parfile_Column[1] == "1":
                miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "2":
                hit_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "3":
                cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "4":
                fa_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "0": 
                if Matching_OR_Timing[1] == "0":
                    cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
                elif Matching_OR_Timing[1] == "1":
                    miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
                
                
    elif "ColDir2" in ZRP_Dir:       
        
        hit_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_H" 
        miss_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_M"
        cr_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_CR"
        fa_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_FA"
        
        hit_file = open(hit_filename, "w")
        miss_file = open(miss_filename, "w")
        cr_file = open(cr_filename, "w")
        fa_file = open(fa_filename, "w")
        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
#            print Matching_OR_Timing[0], Matching_OR_Timing[1]
            if Parfile_Column[1] == "5":
                miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "6":
                hit_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "7":
                cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "8":
                fa_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "0": 
                if Matching_OR_Timing[1] == "0":
                    cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
                elif Matching_OR_Timing[1] == "2":
                    miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
                
                
    elif "ColDir3" in ZRP_Dir:
       
        
        hit_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_H" 
        miss_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_M"
        cr_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_CR"
        fa_filename = str(os.path.splitext(ZRP_Dir)[0]) + "_FA"
        
        hit_file = open(hit_filename, "w")
        miss_file = open(miss_filename, "w")
        cr_file = open(cr_filename, "w")
        fa_file = open(fa_filename, "w")
        
        for Index, ZR_Timing in enumerate(ZR_Parfile.readlines()):
            Parfile_Column = ZR_Timing.strip().split("\t")
#            print (Index)
#            print (ZR_Timing)
            OR_Parfile.seek(0)
            OR_Timings = OR_Parfile.readlines()
            Matching_OR_Timing = OR_Timings[Index].strip().split("\t")
            if Parfile_Column[1] == "9":
               miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "10":
                hit_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "11":
                cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "12":
                fa_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
            elif Parfile_Column[1] == "0": 
                if Matching_OR_Timing[1] == "0":
                    cr_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
                elif Matching_OR_Timing[1] == "3":
                    miss_file.write("{} 2.00 1\n".format(Parfile_Column[0]))
    general_hit.append(hit)
    general_miss.append(miss)
    general_cr.append(cr)
    general_fa.append(fa)
                
