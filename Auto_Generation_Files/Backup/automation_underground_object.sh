#!/bin/bash

ABSOLUTE_PATH=/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files
INPUT_FILE_AUTOMATION_MODULES_MAIN_PY_PATH=$ABSOLUTE_PATH/InputFile_Auto_Generation_Modules/main.py
INPUT_FILES_PATH=$ABSOLUTE_PATH/Input_Files
MERGED_OUT_FILES_PATH=$ABSOLUTE_PATH/Merged_Out_Files
WORKTABLE_PATH=$ABSOLUTE_PATH/Worktable

underground_object_type_to_generate=$1
numbers_to_generate=$2

#convert to lower case
underground_object_type_to_generate=$(echo "$underground_object_type_to_generate" | tr '[:upper:]' '[:lower:]')

echo ${underground_object_type_to_generate}

#gprmax b-scan trace number : 10 
trace_number=10

for underground_object_index in $(seq 1 $numbers_to_generate);
do
    #generate inputfile
    python $INPUT_FILE_AUTOMATION_MODULES_MAIN_PY_PATH $underground_object_type_to_generate $underground_object_index

    #run gprmax with inputfile    
    for entry in $WORKTABLE_PATH/*.in;
    do         
        input_file_name=$entry
        python -m gprMax $input_file_name -n $trace_number -gpu
    done

    #make merged_out file ( remove other out files )
    python -m tools.outputfiles_merge $WORKTABLE_PATH/${underground_object_type_to_generate}_$underground_object_index --remove-files

    
    #make image file (convert merged_out file to image file)    
    sudo /usr/local/MATLAB/R2019b/bin/matlab -nodisplay -nosplash -nodesktop -r "run('my_plot_Bscan.m');exit;"    

    #remove vti files
    
    # find $WORKTABLE_PATH/ -type f -name "*.vti" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.out" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.in" -delete

    find $WORKTABLE_PATH/ -type f -not -name "${underground_object_type_to_generate}_${underground_object_index}_1.vti" -name "*.vti" -delete
    mv  $WORKTABLE_PATH/*.vti $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.in $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.out $MERGED_OUT_FILES_PATH
    
done
    