#coding:utf-8

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('911.csv')
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

df.set_index("timeStamp",inplace=True)
#print(df.head())
count_by_mouth = df.resample("M").count()

print(count_by_mouth)

_x = count_by_mouth.index
_y = count_by_mouth.values

_x = [i.strftime("%Y%m%d") for i in _x]
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x, rotation=45)

plt.show()
