#!/bin/bash

ABSOLUTE_PATH=/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files


numbers_to_generate=$1
echo $numbers_to_generate

for sinkhole_index in $(seq 1 $numbers_to_generate);
do
    #generate inputfile
    python $ABSOLUTE_PATH/inputfile_auto_generation.py $sinkhole_index

    #run gprmax with inputfile
    WORKTABLE_DIR=$ABSOLUTE_PATH/Worktable
    for entry in $WORKTABLE_DIR/*.in;
    do 
        echo 'hi'
        echo $entry
        input_file_name=$entry
        python -m gprMax $input_file_name -n 2 -gpu
    done

    #make merged_out file ( remove other out files )
    python -m tools.outputfiles_merge $WORKTABLE_DIR/sinkhole_$sinkhole_index --remove-files

    
    #make image file (convert merged_out file to image file)    
    sudo /usr/local/MATLAB/R2019b/bin/matlab -nodisplay -nosplash -nodesktop -r "run('my_plot_Bscan.m');exit;"    

    #remove vti files
    #find $WORKTABLE_DIR/ -type f -not -name "Line01_1.vti" -name "*.vti" -delete
    find $WORKTABLE_DIR/ -type f -name "*.vti" -delete
    find $WORKTABLE_DIR/ -type f -name "*.out" -delete
    find $WORKTABLE_DIR/ -type f -name "*.in" -delete
done
    