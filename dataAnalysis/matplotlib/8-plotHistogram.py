#coding:utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

#处理没有统计过的数据

a = [131,98,99,80,99,120,131,160,70,79,80,120,130,131,101,101,99]

#计算组数
d = 5
num_bins = (max(a)-min(a))//d
print(num_bins)
plt.figure(figsize=(20,8),dpi=80)

plt.hist(a,num_bins)
#normed=True便为频率直方图

plt.xticks(range(min(a),max(a)+d,d))

plt.show()