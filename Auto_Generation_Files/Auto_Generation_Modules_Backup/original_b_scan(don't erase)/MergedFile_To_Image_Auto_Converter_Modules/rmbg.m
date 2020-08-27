function [Y] = rmbg(data, t, t1, k)
% Input:
%   1. data:    field data (No.samples * No.traces)
%   2. t:       time vector (in sec)
%   3. t1:      time duration of first-arrived wave (in nsec)
%   4. k:       number of traces for running average. If k is empty, then the
%               data for each trace are totally averaged.
% Output:
%   Y:          background-removed field data
if nargin == 3
    k = size(data, 2);
end

ndx_t_1arr = max(find(t(:).*1e9 < t1));
data_tmp = data(1:ndx_t_1arr, :);

[m, n] = size(data_tmp);
backgr = movmean(data_tmp', k)';
data_sub = zeros(size(data, 1), size(data, 2));
data_sub(1:ndx_t_1arr, :) = backgr;
Y = data - data_sub;
end