#coding:utf-8

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')
file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
df = df[df["Country"]=="CN"]#chinese

datal = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

_x = datal.index
_y = datal.values

plt.figure(figsize=(20,8), dpi=80)

plt.bar(range(len(_x)), _y, width=0.3, color="red")

plt.xticks(range(len(_x)), _x, fontproperties=my_font,rotation=45)

plt.show()


