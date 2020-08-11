function dagc = gainagc(d, dt, lw); 
% 
% AGC : Apply Automatic Gain Control to the traces of the GPR section 
%          "d" by scaling the amplitude of the data at the centre of the 
%          sliding window with respect to the RMS amplitude of the window. 
% 
% Inputs : 
%    dt  : time sampling interval  
%     d  : 2-D GPR section 
%    lw  : AGC window length in sec
% 
% Output : 
%   dagc : The agc'ed GPR section 

[ns, ntr] = size(d); 
dagc = zeros(ns,ntr); 

wagc   = lw;                                    % agc window in ns 
iwagc = floor(wagc/dt);                        % agc window in samples 
 
if iwagc < 1  
    erh = errordlg([ 'AGC window = ' num2str(wagc) ... 
        ' but must be positive'],'GAINAGC : ERROR'); 
    uiwait(erh) 
    dagc = []; 
    return 
end 
if iwagc > ns  
    erh = errordlg([ 'AGC window = ' num2str(wagc) ' too long! '],... 
        'GAINAGC : ERROR'); 
    uiwait(erh) 
    dagc = []; 
    return 
end 
iwagc = round(iwagc/2);               % windows are symmetric,  
                                      % so work with half length 
for itr = 1:1:ntr                       % loop over all traces 
     
    tr = d(:,itr);                    % Current trace to process 
    agcdata = zeros(ns,1);            % work array for agc'ed data          
% compute initial window for first datum  
    sum = 0.0; 
    for i = 1:1:iwagc 
        val = tr(i); 
        sum = sum + val^2; 
    end 
    nwin = 2*iwagc + 1; 
    rms = sum/nwin; 
    if rms <= 0.0  
        agcdata(1) = 0.0; 
    else 
        agcdata(1) = tr(1)/sqrt(rms); 
    end
    
    % ramping on
    for i = 1:1:iwagc  
        val = tr(i+iwagc); 
        sum = sum + val^2; 
        nwin= nwin + 1; 
        rms = sum/nwin; 
        if rms <= 0.0 
            agcdata(i) = 0.0; 
        else  
            agcdata(i) = tr(i)/sqrt(rms); 
        end 
    end
    
    % middle range -- full rms window
    for i = iwagc+1:1:ns-1-iwagc 
        val = tr(i+iwagc); 
        sum = sum + val^2; 
        val = tr(i-iwagc); 
        sum = sum - val^2;  
        rms = sum/nwin; 
        if rms <= 0.0 
            agcdata(i) = 0.0; 
        else 
            agcdata(i) = tr(i)/sqrt(rms); 
        end 
    end
    
    % ramping off
    for i = ns-iwagc:1:ns 
        val = tr(i-iwagc); 
        sum = sum - val^2; 
        nwin = nwin-1; 
        rms = sum/nwin; 
        if rms <= 0.0 
            agcdata(i) = 0.0; 
        else 
            agcdata(i) = tr(i)/sqrt(rms); 
        end 
    end
    
    % Trace finished - load onto output array 
    dagc(:,itr) = agcdata; 
end                                           % itr loop over traces 