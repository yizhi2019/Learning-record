#coding:utf-8

import pandas as pd
from matplotlib import pyplot as plt

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

data1 = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]

_x = data1.index
_y = data1.values

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x)

plt.show()
