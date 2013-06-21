function plotData(x, y)
%PLOTDATA Plots the data points x and y into a new figure 
%   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
%   price and year.

figure;                                  % open a new figure window
plot(x, y, 'rx', 'MarkerSize', 8);       % Plot the data
ylabel('Price');                         % Set the y-axis label
xlabel('Year');                          % Set the x-axis label
end

%% Initialization
clear ; close all; clc

%% Plotting training data
fprintf('Plotting Data ...\n')
data = load("./caldina.csv");             % read comma separated data
Y = data(:, 1);                           % price
X = data(:, 2);                           % year
m = length(Y);                            % number of training examples
plotData(X, Y);
print -dpng caldina1.png                  % save figure as png
fprintf('Program paused. Press enter to continue.\n');
pause;