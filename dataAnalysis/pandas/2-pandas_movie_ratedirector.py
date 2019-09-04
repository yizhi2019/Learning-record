#coding:utf-8
import pandas as pd
import numpy as np

file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#print(df.info())
#信息
#print(df.head(1))
#第一行

print(df["Rating"].mean())
print(len(set(df["Director"].tolist())))

print(df["Director"].unique())
print(len(df["Director"].unique()))


#获取演员
temp_actors_list = df["Actors"].str.split(",").tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num)


