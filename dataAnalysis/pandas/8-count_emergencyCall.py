#coding:utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("911.csv")

#print(df.head(10))
#print(df.info())

#print(df["title"].str.split(": "))
temp_list = df["title"].str.split(": ").tolist()

cate_list = list(set([i[0] for  i in temp_list]))

#print(cate_list)


#构造全为0的数组

zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))), columns=cate_list)

for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1

#print(zeros_df)

# for i in range(df.shape[0]):
#    zeros_df.loc[i, temp_list[i][0]] = 1
# print(zeros_df)


sum_ret = zeros_df.sum(axis=0)
#print(sum_ret)

cate_list = list([i[0] for i in temp_list])
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)), columns=["cate"])
#print(cate_df)

print(df.groupby(by="cate").count()["title"])

