#python script to understand the data
import pandas as pd

df=pd.read_csv("../dataset_1.csv")
null_rows = df[df.isnull().any(axis=1)]
print(null_rows)
print(df.columns)
print(df.head)
print(df.isnull().sum())
print(len(df))
print(df['Column2'].unique())
print(df['Column3'].unique())