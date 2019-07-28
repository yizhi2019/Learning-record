#coding:utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')

month_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
month_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1, 32)
x_10 = range(51,82)
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)
plt.scatter(x_3, month_3,label="3月份",color="red")
plt.scatter(x_10,month_10,label="10月份")

#调整x轴的刻度
_x = list(x_3) + list(x_10)
_xticks_labels = ["3月{}日".format(i) for i in x_3]
_xticks_labels += ["10月{}日".format(i) for i in x_10]
plt.xticks(_x[::3],_xticks_labels[::3],fontproperties=my_font,rotation=45)

plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("3月份和10月份天气变化")

#添加图例
plt.legend(loc="upper left", prop=my_font)
plt.show()

