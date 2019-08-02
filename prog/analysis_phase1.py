import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams

#rcParams['figure.figsize'] = 20,10
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0, 1))
thread1="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\231thread30.csv"
thread2="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\232thread30.csv"
thread3="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\233thread30.csv"
heap1="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\231heap30.csv"
heap2="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\232heap30.csv"
heap3="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\233heap30.csv"
jdbc1="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\231jdbc30.csv"
jdbc2="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\232jdbc30.csv"
jdbc3="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\data23\\233jdbc30.csv"
cpu_used="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\22cpu_user_per30.csv"
mem_used="C:\\Users\\Vrvalke\\Desktop\\PAML\\data\\22mem_used_per30.csv"
column_x='date'
column_y='value'


def dyna_input(nameofthefile,nofwrittento):
    df = pd.read_csv(nameofthefile,skiprows=[0,1,2,3,4,5,6], names=['date','value','empty'], delimiter=';',na_filter=True,skip_blank_lines=True,parse_dates=[0],infer_datetime_format=True)
    if 'empty' in df.columns:
        df=df.drop('empty',axis=1)
    else: pass 
    df.to_csv("C:\\Users\\Vrvalke\\.spyder-py3\\dashboard\\data\\"+nofwrittento+".csv",index=False)
    return df
def splunk_input(nameofthefile,nofwrittento):
    df = pd.read_csv(nameofthefile,skiprows=[0], names=['date','value'],skip_blank_lines=True,parse_dates=['date'],infer_datetime_format=True) 
    df.to_csv("C:\\Users\\Vrvalke\\.spyder-py3\\dashboard\\data\\"+nofwrittento+".csv",index=False)
    return df

def plotgraph(x,y,df):
    rcParams['figure.figsize'] = 30,10
    plt.plot(df[x],df[y])
    plt.show()

def deltab(df):
    df.drop(df.tail(1).index,inplace=True)
    return df
    
def mplotgraph(x,y,df,df1,df2,df3,df4,label1,label2,label3,label4,label5,y_label,g_title):
    rcParams['figure.figsize'] = 30,10
    plt.plot(df[x],df[y],label=label1)
    plt.plot(df1[x],df1[y],label=label2)
    plt.plot(df2[x],df2[y],label=label3)
    plt.plot(df3[x],df3[y],label=label4)
    plt.plot(df4[x],df4[y],label=label5)
    plt.legend(loc='upper right')
    plt.xlabel('datetime')
    plt.ylabel(y_label)
    plt.title(g_title)
    plt.axis('tight')
    plt.show()
    
#plot only one graph
#dataframe0=intake(thread3)
#print(dataframe0)
#dellastrow=deltab(dataframe0)
#print(dellastrow) 
#cleandatas=cleandata(dellastrow) 
#plotgraph(x,y,cleandatas)

dyna_df0=dyna_input(thread1,"wthread231")
dyna_df1=dyna_input(thread2,"wthread232")
dyna_df2=dyna_input(thread3,"wthread233")
dyna_df3=dyna_input(heap1,"wheap231")
dyna_df4=dyna_input(heap2,"wheap232")
dyna_df5=dyna_input(heap3,"wheap233")
dyna_df6=dyna_input(jdbc1,"wjdbc231")
dyna_df7=dyna_input(jdbc2,"wjdbc232")
dyna_df8=dyna_input(jdbc3,"wjdbc233")

splunk_df0=splunk_input(cpu_used,"wcpu_used22")
splunk_df1=splunk_input(mem_used,"wmem_used22")




#plot mutliple line in the same graph
mplotgraph(column_x,column_y,dyna_df0,dyna_df1,dyna_df2,splunk_df0,splunk_df1,'tjvm1','tjvm2','tjvm3','cpu','mem','active thread count','cpu,mem & thread')
mplotgraph(column_x,column_y,dyna_df3,dyna_df4,dyna_df5,splunk_df0,splunk_df1,'hjvm1','hjvm2','hjvm3','cpu','mem','mb','cpu,mem & heap')
mplotgraph(column_x,column_y,dyna_df6,dyna_df7,dyna_df8,splunk_df0,splunk_df1,'jdjvm1','jdjvm2','jdjvm3','cpu','mem','collection pool size','cpu,mem & jdbc')
