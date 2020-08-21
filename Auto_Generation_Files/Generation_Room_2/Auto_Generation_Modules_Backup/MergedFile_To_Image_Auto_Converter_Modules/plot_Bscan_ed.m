% plot_Bscan.m
% Script to plot EM fields from a gprMax B-scan
%
% Craig Warren

% 2020. 4. 24. the code is modified by W. Kang to include basic processing routine such as 
% background removal & time-domain gain functions
% Requires subfunctions of rmbg.m, gainagc.m, and gainexp.m.

function myFunctionReturn=plot_Bscan_ed(cen_frequency_front_in,cen_frequency_back_in)
    
    %clear all, clc

    cen_frequency_front=int2str(cen_frequency_front_in)
    cen_frequency_back=int2str(cen_frequency_back_in)
    
    concat_center_frequency=strcat(cen_frequency_front,'.')
    concat_center_frequency=strcat(concat_center_frequency,cen_frequency_back)
    input_center_frequency=str2double(concat_center_frequency)
   
    % for DGX
    %absolute_path='/root/Desktop/workspace/youngjun/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files'
    % for DGX1
    absolute_path='/workspace/youngjun/MiLab_Experiment/SinkholeDetection/MiLab_SinkholeDetection/Auto_Generation_Files/Generation_Room_2'
    Files=dir('../../Worktable/*.out')

    merged_out_filename=''

    for k=1:length(Files)
        merged_out_filename=Files(k).name    
    end

    worktable_path=strcat(absolute_path,'/Worktable/')
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

%         % 1. Background removal    
%         %t_1arr_ns = 5.5; % set ns range for background removal
%         %t_1arr_ns=0;
%         %if input_center_frequency<0.3
%         %     t_1arr_ns=23.91
%         %elseif input_center_frequency<0.4
%         %    t_1arr_ns=21.2
%         %elseif input_center_frequency<0.5
%         %    t_1arr_ns=19.69
%         %elseif input_center_frequency<0.6
%         %    t_1arr_ns=18.54
%         %elseif input_center_frequency<0.7
%         %    t_1arr_ns=17.61
%         %elseif input_center_frequency<0.8
%         %    t_1arr_ns=16.74
%         %elseif input_center_frequency>=0.8
%         %    t_1arr_ns=15.97
%         %end
% 
%         t_1arr_ns=6.5
%         
%         k_ma = 36; % at least under trace number
%         field_proc = rmbg(field, time, t_1arr_ns, k_ma);
%         ndx_proc = ndx_proc + 1;
%         field_hist(:, :, ndx_proc) = field_proc;   
% 
%         % 2. AGC Gain
%         field_proc_ag = gainagc(field_proc, dt, time(end));
%         ndx_proc = ndx_proc + 1;
%         field_hist(:, :, ndx_proc) = field_proc_ag;

        % 3. Exponential Gain
        
        A = 0.4e8;
        B = 10e8;
        t1_ns = 7;
        [field_proc_eg, G] = gainexp(A, B, t1_ns, time, field);
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
        

        %About PaperPosition
            % 1 inch = 150pixel
            %Paper Position is inch
        % 300x150 pixel   
        %set(fh1,'PaperUnits','inches');
        %set(fh1,'PaperPosition', [0 0 4 2])              

        %set image save path
        image_save_path_tmp=strcat(absolute_path,'/Result_Images/')
        splited_path=strsplit(merged_out_filename,'_')    
        splited_path2=strcat(splited_path(1),'_')    
        splited_path3=strcat(splited_path2,splited_path(2))  
        combine_path1=strcat(image_save_path_tmp,splited_path3)
        %image_file_save_path=strcat(combine_path1,'.png')
        %final_image_path=string(image_file_save_path)

        %save image
        %saveas(fh1,final_image_path);
        set(fh1,'Position',[0 0 775 368])        
        export_fig([char(combine_path1),'.png'],'-png','-transparent')

        close all

    end
    
    myFunctionReturn=1;
end

% function myFunctionReturn=myFunction(cen_frequency)
%     b=3
%     myFunctionReturn=cen_frequency
% end





