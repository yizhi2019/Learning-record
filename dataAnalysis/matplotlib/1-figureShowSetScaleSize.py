#coding:utf-8
# from matplotlib import pyplot as plt #导入类
#
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 17, 22, 18, 15]
# plt.plot(x, y)
# plt.show()




# from matplotlib import pyplot as plt
#
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 17, 22, 18, 15]
# plt.figure(figsize=(20,8), dpi=80) #设置图片大小
# plt.plot(x, y)
# plt.savefig('./num1.png')



from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 17, 22, 18, 15]
plt.figure(figsize=(20,8), dpi=80)
plt.xticks([i/2 for i in range(4,50)] ) #x坐标刻度间隔
plt.yticks(range(min(y), max(y)+1)) #y坐标刻度间隔
plt.plot(x, y)
plt.show()

