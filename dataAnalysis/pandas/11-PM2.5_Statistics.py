#coding:utf-8

import pandas as pd
from matplotlib import pyplot as plt
filePath = './PM2.5/BeijingPM20100101_20151231.csv'

df = pd.read_csv(filePath)

#Put the separate time string through the periodIndex method for the time type of pandas
period = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
df["datetime"] = period

#set datetime to index
df.set_index("datetime",inplace=True)

#Downsampling, averaged monthly
df = df.resample("7D").mean()
#handling missing data,del that
#print(df["PM_US Post"])
data = df["PM_US Post"].dropna()

#data of china
data_china = df["PM_Dongsi"].dropna()

#plot
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = data.values

_x_china = data_china.index
_x_china =  [i.strftime("%Y%m%d") for i in _x_china]
_y_china = data_china.values

plt.figure(figsize=(20, 8),dpi=80)
plt.plot(range(len(_x)), _y,label="US")
plt.plot(range(len(_x_china)),_y_china,label="china")
plt.xticks((range(0, len(_x), 10)),list(_x)[::10], rotation=45)

plt.legend(loc="best")
plt.show()
