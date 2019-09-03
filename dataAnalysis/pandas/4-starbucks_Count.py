#coding:utf-8

import pandas as pd

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

grouped = df.groupby(by="Country")

#print(grouped)
#对象 可以遍历 聚合

#print(df.info())

#for li in grouped:
#  print(li)
#    print("*"*100)

country_count = grouped["Brand"].count()
#print(country_count["US"])
#print(country_count["CN"])

china_data = df[df["Country"]=="CN"]
grouped = china_data.groupby(by="State/Province").count()["Brand"]
#print(grouped)

grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()

print(grouped)

grouped = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]]).count()
print(type(grouped))


