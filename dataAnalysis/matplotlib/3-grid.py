#coding:utf-8

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

_xticks_xlabels = ["{}岁".format(i) for i in x]

plt.xticks(x,_xticks_xlabels,fontproperties=my_font)
#fontproperties显示中文
plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4)
#alpha 透明度

plt.show()
