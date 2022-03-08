import pandas as pd
import csv
import plotly.express as px
df=pd.read_csv("stars.csv")
data_list=[]
for i in df:
    data_list.append(df)