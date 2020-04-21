#!/bin/bash

ABSOLUTE_PATH=/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files
INPUT_FILES_PATH=$ABSOLUTE_PATH/Input_Files
MERGED_OUT_FILES_PATH=$ABSOLUTE_PATH/Merged_Out_Files
WORKTABLE_PATH=$ABSOLUTE_PATH/Worktable

numbers_to_generate=$1
echo $numbers_to_generate

trace_number=30

for sinkhole_index in $(seq 1 $numbers_to_generate);
do
    #generate inputfile
    python $ABSOLUTE_PATH/inputfile_auto_generation.py $sinkhole_index

    #run gprmax with inputfile
    
    for entry in $WORKTABLE_PATH/*.in;
    do         
        input_file_name=$entry
        python -m gprMax $input_file_name -n $trace_number -gpu
    done

    #make merged_out file ( remove other out files )
    python -m tools.outputfiles_merge $WORKTABLE_PATH/sinkhole_$sinkhole_index --remove-files

    
    #make image file (convert merged_out file to image file)    
    sudo /usr/local/MATLAB/R2019b/bin/matlab -nodisplay -nosplash -nodesktop -r "run('my_plot_Bscan.m');exit;"    

    #remove vti files
    
    # find $WORKTABLE_PATH/ -type f -name "*.vti" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.out" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.in" -delete

    find $WORKTABLE_PATH/ -type f -not -name "sinkhole_${sinkhole_index}_1.vti" -name "*.vti" -delete
    mv  $WORKTABLE_PATH/*.vti $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.in $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.out $MERGED_OUT_FILES_PATH
    
done
    