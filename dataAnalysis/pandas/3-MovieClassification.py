#coding:utf-8
import pandas as pd
import numpy as np
from matplotlib import  pyplot as plt
file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)


#print(df.head())

#print(df["Genre"])
temp_list = df["Genre"].str.split(",").tolist()
genre_list = list(set([i for j in temp_list for i in j]))

#创建零矩阵
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
#print(zero_df)

#电影出现分类位置赋值

for i in range(df.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1

print(zero_df.head(1))

genre_count = zero_df.sum(axis=0)
print(genre_count)

genre_sort = genre_count.sort_values()
_x = genre_sort.index
_y = genre_sort.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()