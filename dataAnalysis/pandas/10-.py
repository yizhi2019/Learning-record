#coding:utf-8

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#converting a time type string to a time type
df = pd.read_csv('911.csv')
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

#添加列、表示分类
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]

df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
df.set_index("timeStamp",inplace=True)

plt.figure(figsize=(20, 8))

for group_name, group_data in df.groupby(by="cate"):
    #对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]
    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)


plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()