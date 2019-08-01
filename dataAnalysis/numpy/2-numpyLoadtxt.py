#coding:utf-8
import numpy as np

test_file_path = r'.\NumpyTest.txt'
uk_file_path = "./"


t1 = np.loadtxt(test_file_path, delimiter=",",dtype="int")#按照逗号分隔 unpack=True便将矩阵转置
print(t1)

#t1.transpose()转置
print(t1[1])
print(t1[1:])
print(t1[[0,2]])

c = t1[[0,0],[1,1]]