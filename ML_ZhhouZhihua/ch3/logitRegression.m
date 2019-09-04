clear
clc
data = load('watermeleon3.0a.txt');  
X = data(:, [2, 3]); y = data(:, 4);  
figure; 
hold on;  
pos=find(y==1);  
neg=find(y==0); 
data(pos,4)
plot(X(pos,1),X(pos,2),'g.','LineWidth',2,'MarkerSize',7);  
plot(X(neg,1),X(neg,2),'k.','MarkerFaceColor','y','MarkerSize',7);  
% Labels and Legend  
xlabel('ÃÜ¶È')  
ylabel('º¬ÌÇÂÊ')  
hold off;  
[m, n] = size(X) ;
% Add intercept term to x and X_test  
X = [X ones(m, 1) ];
% Initialize fitting parameters  
initial_theta = zeros(n + 1, 1)  ;
options = optimset('GradObj', 'on', 'MaxIter', 400);  
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);  
hold on;
    plot_x = X(:,1) ; 
    y = X*theta ;
    plot_y=1./(1.+exp(-1.*y))
    plot(plot_x, plot_y,'r+','LineWidth',2,'MarkerSize',7)    
hold off;  
theta