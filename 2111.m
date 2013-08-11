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
data = load("./2111.csv");             % read comma separated data
Y = data(:, 1);                           % price
X = data(:, 2);                           % year
m = length(Y);                            % number of training examples
plotData(X, Y);
print -dpng 2111.png                  % save figure as png
fprintf('Program paused. Press enter to continue.\n');
pause;

%% Theta
X = [ones(m, 1), data(:,2)];              % Add a column of ones to x
theta = pinv(X'*X)*X'*Y;

% Plot the linear fit
hold on;                                  % keep previous plot visible
plot(X(:,2), X*theta, '-')
legend('Training data', 'Linear regression')
print -dpng 2111_.png
hold off                                  % don't overlay any more plots on this figure

% Predict price for year 2005
predict = [1, 2005] *theta;
fprintf('For year = 2005, we predict a price of %f\n', predict);
fprintf('Program paused. Press enter to continue.\n');
pause;
