import numpy as np

t1 = np.arange(3)
print(t1)
print(t1.shape)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2.shape)


t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,21]]])
print(t3.shape)
t3.flatten()
print(t3)

t4= np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(t4.reshape((3,4)))

print(t4 + 2)

t5 = np.array([[1,2],[3,4]])


t6 = np.arange


