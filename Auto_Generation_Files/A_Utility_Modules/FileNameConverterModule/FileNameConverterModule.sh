startIndex=$1

ToConvertFilesPath="./ToConvertFiles"
ConvertedFilesPath="ConvertedFiles"
for toConvertFile in $ToConvertFilesPath/*;
do         
    
    echo $toConvertFile

    splitedName1=$(echo $toConvertFile | tr "/" "\n")
    echo $splitedName1
    tmp1=${splitedName1[0]}
    echo $tmp1
    # splitedName2=$(echo ${tmp1} | tr "_" "\n")
    # objectName=$splitedName2[0]
    # echo $splitedName2
    # splitedName2_1=$splitedName2[1]
    # splitedName3=$(echo ${splitedName2_1} | tr "." "\n")
    # fileType=$splitedName3[1]
    # echo $splitedName3
    # changedName="${objectName}_${startIndex}.${fileType}"
    # echo $changedName

    # mv $toConvertFile $ConvertedFilesPath/$changedName
    
    # $startIndex=$startIndex+1
    break
done