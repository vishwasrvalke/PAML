# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:52:26 2019

@author: Vrvalke
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 20,10
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))


heap1="C:\\Users\\Vrvalke\\Desktop\\221heap3030.csv"
heap2="C:\\Users\\Vrvalke\\Desktop\\222heap3030.csv"
heap3="C:\\Users\\Vrvalke\\Desktop\\223heap3030.csv"
jdbc1="C:\\Users\\Vrvalke\\Desktop\\221jdbc30.csv"
jdbc2="C:\\Users\\Vrvalke\\Desktop\\222jdbc30.csv"
jdbc3="C:\\Users\\Vrvalke\\Desktop\\223jdbc30.csv"
thread1="C:\\Users\\Vrvalke\\Desktop\\221thread30.csv"
thread2="C:\\Users\\Vrvalke\\Desktop\\222thread30.csv"
thread3="C:\\Users\\Vrvalke\\Desktop\\223thread30.csv"

x='Date'
y='value'

def intake(nameofthefile):
    rd = pd.read_csv(nameofthefile)
    df=pd.DataFrame(rd)
    return df
def cleandata(df):
    df = df.drop([0,1]).reset_index(drop=True)
    df = pd.DataFrame(df.Chart.str.split(";",2).tolist(),columns = ['Date','value','empty'])
    df.head()
    del df['empty']
    df['Date'] = pd.to_datetime(df['Date'])
    df.dtypes
    df['value'] = pd.to_numeric(df.value, errors='ignore')
    df.dtypes
    df.head()
    return df
def plotgraph(x,y,df):
    rcParams['figure.figsize'] = 30,10
    plt.plot(df[x],df[y])
    plt.show()
    
def mplotgraph(x,y,df,df1,df2):
    rcParams['figure.figsize'] = 30,10
    plt.plot(df[x],df[y])
    plt.plot(df1[x],df1[y])
    plt.plot(df2[x],df2[y])
    plt.show()
     
   


dataframe0=intake(heap1)
dataframe1=intake(heap2)
dataframe2=intake(heap3)
dataframe3=intake(thread1)
dataframe4=intake(thread2)
dataframe5=intake(thread3)
dataframe6=intake(jdbc1)
dataframe7=intake(jdbc2)
dataframe8=intake(jdbc3)
cdata0=cleandata(dataframe0)
cdata1=cleandata(dataframe1)
cdata2=cleandata(dataframe2)
cleandata3=cleandata(dataframe3)
cleandata4=cleandata(dataframe4)
cleandata5=cleandata(dataframe5)
cleandata6=cleandata(dataframe6)
cleandata7=cleandata(dataframe7)
cleandata8=cleandata(dataframe8)

#plot mutliple line in the same graph
mplotgraph(x,y,cdata0,cdata1,cdata2)
mplotgraph(x,y,cleandata3,cleandata4,cleandata5)
mplotgraph(x,y,cleandata6,cleandata7,cleandata8)


