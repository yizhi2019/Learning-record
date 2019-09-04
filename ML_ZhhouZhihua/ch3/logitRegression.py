#coding:utf-8

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#load txt
dataset = pd.read_csv('watermeleon3.0a.txt', header=None, sep=' ', names=['编号', '密度', '含糖量', '好瓜'])

#print(dataset.head())
#print(type(dataset))

X = dataset[['密度', '含糖量']]
y = dataset['好瓜']
good_melon = dataset[dataset['好瓜'] == 1]
bad_melon = dataset[dataset['好瓜'] == 0]

f1 = plt.figure(1)
plt.title('watermelon_3a')
plt.xlabel('density')
plt.ylabel('ratio_sugar')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.scatter(bad_melon['密度'], bad_melon['含糖量'], marker='o', color='blue', s=100, label='bad')
plt.scatter(good_melon['密度'], good_melon['含糖量'], marker='o', color='orange', s=100, label='good')
plt.legend(loc='upper right')

#generalization of test and train set
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=0)

#model training
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

#model testing
y_pred = log_model.predict(X_test)

#summarize the accuracy of fitting
print(metrics.confusion_matrix(y_test, y_pred))
print(log_model.coef_)
theta1, theta2 = log_model.coef_[0][0], log_model.coef_[0][1]
x_pred = np.linspace(0, 1, 1000)
line_pred = theta1 + theta2*x_pred
plt.plot(x_pred, line_pred)


plt.show()




