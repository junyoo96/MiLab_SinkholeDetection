% plot_Bscan.m
% Script to plot EM fields from a gprMax B-scan
%
% Craig Warren

clear all, clc

%Set merged_out filename to turn into B-scan image
%filename='C:\Users\Yoo YoungJun\Desktop\MiLab\Lab_Project\Sinkhole_detection\Sinkhole_Files\MiLab_SinkholeDetection\Automation_Files\input_file_generation_test_files\sinkhole_1__merged.out'
filename='/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/input_file_generation_test_files/sinkhole_1__merged.out'


% Open file and read fields
if filename ~= 0
    iterations = double(h5readatt(filename, '/', 'Iterations'));
    dt = h5readatt(filename, '/', 'dt');

    %prompt = 'Which field do you want to view? Ex, Ey, or Ez: ';
    %field = input(prompt,'s');
    
    %Set field to show (There was option 'Ex', 'Ey', 'Ez')
    field = 'Ez'
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
    set(fh1,'PaperPosition', [0 0 8 4])   
   
    %save figure as image
    saveas(fh1,'/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Automation_Files/test_image/sinkhole.png');
    
 
end
