#!/bin/bash

#generate inputfile
# python /root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/inputfile_auto_generation.py

python -m gprMax /root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/input_file_generation_test_files/sinkhole_1_.in -n 30 -gpu

python -m tools.outputfiles_merge /root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/input_file_generation_test_files/sinkhole_1_ --remove-files

sudo /usr/local/MATLAB/R2019b/bin/matlab -nodisplay -nosplash -nodesktop -r "run('my_plot_Bscan.m');exit;"

#remove vti files
find /root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/input_file_generation_test_files/ -type f -not -name "Line01_1.vti" -name "*.vti" -delete
find /root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/input_file_generation_test_files/ -type f -name "*.out" -delete