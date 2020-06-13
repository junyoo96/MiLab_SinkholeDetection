#!/bin/bash

#Measure execution time
StartTime=$(date +%s)

ABSOLUTE_PATH=/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files
INPUT_FILE_AUTOMATION_MODULES_MAIN_PY_PATH=$ABSOLUTE_PATH/Auto_Generation_Modules/InputFile_Auto_Generation_Modules/main.py
INPUT_FILES_PATH=$ABSOLUTE_PATH/Input_Files
MERGED_OUT_FILES_PATH=$ABSOLUTE_PATH/Merged_Out_Files
LOG_FILES_PATH=$ABSOLUTE_PATH/Log_Files
WORKTABLE_PATH=$ABSOLUTE_PATH/Worktable

WAVEFORM_INFO_FILE=$WORKTABLE_PATH/waveform_info.txt

underground_object_type_to_generate=$1
numbers_to_generate=$2

#convert to lower case
underground_object_type_to_generate=$(echo "$underground_object_type_to_generate" | tr '[:upper:]' '[:lower:]')

echo ${underground_object_type_to_generate}

#gprmax b-scan trace number : 10 
trace_number=31

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
    python -m tools.outputfiles_merge $WORKTABLE_PATH/${underground_object_type_to_generate}_${underground_object_index} --remove-files
    
    #make image file (convert merged_out file to image file)  
    center_frequency_front_from_file=-1
    center_frequency_back_from_file=-1

    waveform_info_file_content_index_count=0

    while IFS= read -r line
    do
        if [ $waveform_info_file_content_index_count = "0" ]
        then
            center_frequency_front_from_file=$line
        elif [ $waveform_info_file_content_index_count = "1" ]
        then    
            center_frequency_back_from_file=$line
        fi

        waveform_info_file_content_index_count=$((waveform_info_file_content_index_count+1))
    done < $WAVEFORM_INFO_FILE
    
    input_center_frequency_front=$center_frequency_front_from_file
    input_center_frequency_back=$center_frequency_back_from_file

    sudo /usr/local/MATLAB/R2020a/bin/matlab -nodisplay -nosplash -nodesktop -r "run('./MergedFile_To_Image_Auto_Converter_Modules/plot_Bscan_ed($input_center_frequency_front,$input_center_frequency_back)');exit;"    
 

    #move worktable files
    find $WORKTABLE_PATH/ -type f -not -name "${underground_object_type_to_generate}_${underground_object_index}_1.vti" -name "*.vti" -delete
    mv  $WORKTABLE_PATH/*.vti $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.in $INPUT_FILES_PATH
    mv  $WORKTABLE_PATH/*.out $MERGED_OUT_FILES_PATH
    find $WORKTABLE_PATH/ -type f -name "*.txt" -delete

    #remove vti files(not used now)    
    # find $WORKTABLE_PATH/ -type f -name "*.vti" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.out" -delete
    # find $WORKTABLE_PATH/ -type f -name "*.in" -delete
    
done

#Measure execution time
FinishTime=$(date +%s)
ExecutionTime=$(($((FinishTime-StartTime))/60))
echo "Generated underground object : $underground_object_type_to_generate\nGenerated number : $numbers_to_generate\nExecution Time : $ExecutionTime minutes"  > ../Worktable/execution_info.txt
mv  $WORKTABLE_PATH/*.txt $LOG_FILES_PATH

#copy main file
cp -r InputFile_Auto_Generation_Modules/ ../Log_Files/

    