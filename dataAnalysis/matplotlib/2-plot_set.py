#coding:utf-8

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

font = {'family' : 'sont',
              'weight' : 'bold',
              'size'   : 'large'}

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
#matplotlib.rc("font",**font)
#matplotlib.rc("font", family= 'MicroSoft YaHei', weight='bold', size='larger')
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=[20, 8], dpi=80)

plt.plot(x, y)

#调整x轴的刻度


_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45,fontproperties=my_font)#步长为3,旋转45度


#描述信息
plt.xlabel('时间',fontproperties=my_font)
plt.ylabel('温度 单位（度）',fontproperties=my_font)
plt.title('10点到12点每分钟温度变化信息',fontproperties=my_font)
plt.show()
