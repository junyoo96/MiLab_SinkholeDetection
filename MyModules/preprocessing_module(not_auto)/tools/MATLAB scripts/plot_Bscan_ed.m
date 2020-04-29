% plot_Bscan.m
% Script to plot EM fields from a gprMax B-scan
%
% Craig Warren

% 2020. 4. 24. the code is modified by W. Kang to include basic processing routine such as 
% background removal & time-domain gain functions
% Requires subfunctions of rmbg.m, gainagc.m, and gainexp.m.

clear all, clc

%[filename, pathname] = uigetfile('*.out', 'Select gprMax output file to plot B-scan', 'MultiSelect', 'on');
%filename = fullfile(pathname, filename);

absolute_path='C:/Users/Yoo YoungJun/Desktop/MiLab/Lab_Project/Sinkhole_detection/200424_gprMax_proc_V1/test'
Files=dir('C:/Users/Yoo YoungJun/Desktop/MiLab/Lab_Project/Sinkhole_detection/200424_gprMax_proc_V1/test/*.out')

merged_out_filename=''

for k=1:length(Files)
    
    aaaaa=k
    
    merged_out_filename=Files(k).name    
    
    %worktable_path=strcat(absolute_path,'/Worktable/')
    worktable_path=strcat(absolute_path,'/')
    filename=strcat(worktable_path,merged_out_filename)

    % Open file and read fields
    if filename ~= 0
        iterations = double(h5readatt(filename, '/', 'Iterations'));
        dt = h5readatt(filename, '/', 'dt');        
        
        %Set field to show (There was option 'Ex', 'Ey', 'Ez')
        field = 'Ex'
        fieldpath = strcat('/rxs/rx1/', field);
        field = h5read(filename, fieldpath)';
        time = linspace(0, (iterations - 1) * dt, iterations)';
        %Divide by 2 x-axis of figure 
        traces = 0:size(field, 2);
             
        %Cut figure 0~end of taces 
        %It means 0 30(number of b-scan traces)
        xlim([0 traces(end)]);      
           
        
        N_proc = 10;
        field_hist = zeros(length(time), length(traces)-1, N_proc);
        ndx_proc = 1;
        field_hist(:, :, ndx_proc) = field;

        field_A = field(:, round(length(traces)/2));

       
        t_window_ns = round(time(end)*1e9);
        x = linspace(1, size(field, 2), size(field, 2));   

        % 전처리 1단계 : Background removal
        t_1arr_ns = 5.5;
        k_ma = 11;
        field_proc = rmbg(field, time, t_1arr_ns, k_ma);
        ndx_proc = ndx_proc + 1;
        field_hist(:, :, ndx_proc) = field_proc;   

        % 전처리 2단계 : AGC Gain
        field_proc_ag = gainagc(field_proc, dt, time(end));
        ndx_proc = ndx_proc + 1;
        field_hist(:, :, ndx_proc) = field_proc_ag;

        % 전처리 3단계 : Exponential Gain
        A = 2e8;
        B = 1.4e8;
        t1_ns = 5;
        [field_proc_eg, G] = gainexp(A, B, t1_ns, time, field_proc);
        ndx_proc = ndx_proc + 1;
        field_hist(:, :, ndx_proc) = field_proc_eg;
        
        %Make image as figure
        fh1=figure('Name', filename);
        
        clims = [-max(max(abs(field))) max(max(abs(field)))];
        %Show mixed result on the figure
        imagesc(traces, time.*1e9, field_proc_eg, clims);
        axis([traces(1)-0.5 traces(end)+0.5 0 t_window_ns]);
        
        %remove axis from figure
        axis off  

        % Options to create a nice looking figure for display and printing
        set(fh1,'PaperUnits','inches');

        %About PaperPosition
            % 1 inch = 150pixel
            %Paper Position is inch
        % 300x150 pixel   
        set(fh1,'PaperPosition', [0 0 4 2])              
  
        %set image save path
        image_save_path_tmp=strcat(absolute_path,'/Result_Images/')
        splited_path=strsplit(merged_out_filename,'_')    
        splited_path2=strcat(splited_path(1),'_')    
        splited_path3=strcat(splited_path2,splited_path(2))  
        combine_path1=strcat(image_save_path_tmp,splited_path3)
        image_file_save_path=strcat(combine_path1,'.png')
        final_image_path=string(image_file_save_path)
        
        %save image
        saveas(fh1,final_image_path);
        
        close all

    end

end




