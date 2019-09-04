function [J, grad] = costFunction(theta, X, y)  
m = length(y); % number of training examples  
J = 0;  
grad = zeros(size(theta));  
h=1.0./(1.0+exp(-1*X*theta));  
m=size(y,1);  
J=((-1*y)'*log(h)-(1-y)'*log(1-h))/m;  
for i=1:size(theta,1),  
    grad(i)=((h-y)'*X(:,i))/m;  
end  
end  