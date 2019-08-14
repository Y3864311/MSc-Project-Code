#ipython --gui=qt
import os, surfer
os.environ['SUBJECTS_DIR'] = '/usr/share/freesurfer-data/subjects'
import glob
from os.path import join

General_Directory = ''

Hemisphere = 'lh'
Viewpoint = ["lateral", "medial", "parietal", "ventral"]
C1_Col = 'Reds'
C2_Col = 'Greens'
C3_Col = 'Wistia'

brain = surfer.Brain('fsaverage','{}'.format(Hemisphere),'inflated', config_opts = {'cortex':'bone','background':'white'})
light_settings = [{'elevation':0,'azimuth':0,'intensity':0.7}, {'elevation':0,'azimuth':-90,'intensity':0.7}, {'elevation':0,'azimuth':90,'intensity':0.7}, {'elevation':0,'azimuth':180,'intensity':0.7},
{'elevation':-90,'azimuth':0,'intensity':0.7},
{'elevation':90,'azimuth':0,'intensity':0.7}
]

# Assign light manager to variable for brevity
light_manager = brain._figures[0][0].scene.light_manager
# Create required number of lights
light_manager.number_of_lights = len(light_settings)
# Loop over lights
for i, x in enumerate(light_settings):
	light = light_manager.lights[i] # get current light
	light.activate = True # turn it on
	light.elevation = x['elevation'] # set elevation
	light.azimuth = x['azimuth'] # set azimuth
	light.intensity = x['intensity'] # set intensity
    
Inflated_Brain_Files = sorted(glob.glob('{}/Inflated_Brains/FullThresh_ByContrast3CX/*/*{}.mgh'.format(General_Directory, Hemisphere)))

for File_Dir in Inflated_Brain_Files:
    overlay = surfer.io.read_scalar_data(File_Dir)
    File = os.path.basename(File_Dir)
    File = File.split('.')
    File = File[0]
    brain.add_overlay(overlay, min = 2.3, max = 8, name = '{}'.format(File), sign = 'pos')
    brain.overlays["{}".format(File)].pos_bar.visible = False
    if "C1" in File:
        #print(File)
        brain.overlays["{}".format(File)].pos_bar.lut_mode = C1_Col
        for View in Viewpoint:
            brain.show_view(View)
            Image_Name = 'zstat_{}_{}_{}.png'.format(File, View, C1_Col)
            brain.save_image(Image_Name)
    elif "C2" in File:
        brain.overlays["{}".format(File)].pos_bar.lut_mode = C2_Col
        for View in Viewpoint:
            brain.show_view(View)
            Image_Name = 'zstat_{}_{}_{}.png'.format(File, View, C2_Col)
            brain.save_image(Image_Name)
    elif "C3" in File:
        brain.overlays["{}".format(File)].pos_bar.lut_mode = C3_Col
        for View in Viewpoint:
            brain.show_view(View)
            Image_Name = 'zstat_{}_{}_{}.png'.format(File, View, C3_Col)
            brain.save_image(Image_Name)
            
    brain.overlays[File].remove()
    
