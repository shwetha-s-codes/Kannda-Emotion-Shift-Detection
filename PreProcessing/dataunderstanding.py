#python script to understand the data
import pandas as pd

df=pd.read_csv("../DataSets/Dataset_4.csv")
null_rows = df[df.isnull().any(axis=1)]
print(null_rows)
print(df.columns)
print(df.head)
print(df.isnull().sum())
print(len(df))
print(df['Part1 Sentiment'].unique())
print(df['Part2 Sentiment'].unique())