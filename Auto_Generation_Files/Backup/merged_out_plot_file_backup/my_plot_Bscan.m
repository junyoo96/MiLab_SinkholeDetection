% plot_Bscan.m
% Script to plot EM fields from a gprMax B-scan
%
% Craig Warren

clear all, clc

%Set merged_out filename to turn into B-scan image

fprintf('hello')


absolute_path='/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files'
Files=dir('./Worktable/*.out')

merged_out_filename=''

for k=1:length(Files)
    merged_out_filename=Files(k).name
    
end

fprintf(merged_out_filename)

%filename='/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files/Worktable/sinkhole_1_merged.out'
worktable_path=strcat(absolute_path,'/Worktable/')
filename=strcat(worktable_path,merged_out_filename)

% Open file and read fields
if filename ~= 0
    iterations = double(h5readatt(filename, '/', 'Iterations'));
    dt = h5readatt(filename, '/', 'dt');

    %prompt = 'Which field do you want to view? Ex, Ey, or Ez: ';
    %field = input(prompt,'s');
    
    %Set field to show (There was option 'Ex', 'Ey', 'Ez')
    field = 'Ex'
    fieldpath = strcat('/rxs/rx1/', field);
    field = h5read(filename, fieldpath)';
    time = linspace(0, (iterations - 1) * dt, iterations)';    
    %traces = 0:size(field, 2);
    
    %Divide by 2 x-axis of figure 
    traces = 0:size(field, 2);

    %Make image as figure
    fh1=figure('Name', filename);   
   
    clims = [-max(max(abs(field))) max(max(abs(field)))];
    
    %Show mixed result on the figure
    im = imagesc(traces, time, field, clims);
    
   
    %Cut figure 0~end of taces 
        %It means 0 30(number of b-scan traces)
    xlim([0 traces(end)]);  
    
    %remove axis from figure
    axis off    
   
    %Set paperposition unit as inches
    set(fh1,'PaperUnits','inches')
    
    %About PaperPosition
        % 1 inch = 150pixel
        %Paper Position is inch
    % 300x150 pixel   
    set(fh1,'PaperPosition', [0 0 4 2])   
   
    %save figure as image
    %saveas(fh1,'/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/test_image/sinkhole.png');


    image_save_path_tmp=strcat(absolute_path,'/Result_Images/')
    
    splited_path=strsplit(merged_out_filename,'_')    
    splited_path2=strcat(splited_path(1),'_')    
    splited_path3=strcat(splited_path2,splited_path(2))  

    combine_path1=strcat(image_save_path_tmp,splited_path3)
    image_file_save_path=strcat(combine_path1,'.png')

    final_image_path=string(image_file_save_path)

    
    saveas(fh1,final_image_path);
    
 
end
