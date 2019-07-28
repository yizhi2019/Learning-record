#coding:utf-8

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')

a = ["数据1","数据2","数据3"]
b = [11.1,19.9,8.6]

plt.figure(figsize=[10,8],dpi=80)

#绘制竖着的
#plt.bar(range(len(a)),b,width=0.3)
#绘制横着的
plt.barh(range(len(a)),b,height=0.3,color="orange")

plt.yticks(range(len(a)),a,fontproperties=my_font,rotation=45)
plt.grid(alpha=0.3)

plt.show()




