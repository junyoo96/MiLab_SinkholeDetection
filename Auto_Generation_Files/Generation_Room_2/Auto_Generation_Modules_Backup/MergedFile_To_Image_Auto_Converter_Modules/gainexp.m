function [Y, gc] = gainexp(a, b, tau1, t, field_data)
% Exponential Gain
% Gain function = a * t * exp(b * t) for t < tau1
% Gain function = a * tau1 * exp(b * tau1) for t >= tau1
% inputs
%   a, b, and tau1 are the terms of gain function
%   t: time vector
%   field_data: GPR data (no. samples * no. traces)
% outputs
%   Y: processed GPR data after exponential gain
%   gc: gain curve profile

ndx_t1 = max(find(t(:).*1e9 < tau1));
gc = zeros(size(field_data, 1), 1);
gc(1:ndx_t1, 1) = a.*t(1:ndx_t1, 1).*exp(b.*t(1:ndx_t1, 1));
gc(ndx_t1+1:end, 1) = a*t(ndx_t1+1, 1)*exp(b*t(ndx_t1+1, 1));

for tit = 1:1:size(field_data, 2)
    Y(:, tit) = field_data(:, tit).*gc;
end
end
