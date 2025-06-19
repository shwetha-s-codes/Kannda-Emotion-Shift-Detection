import pandas as pd

#reading csv file
df= pd.read_csv("..\dataset_1.csv")
df['Column2']=df['Column2'].str.strip().replace("Negative","Negetive")
df['Column3']=df['Column3'].str.strip().replace("Negative","Negetive")
print("labels Replaced Sucessfully")
print(df['Column2'].unique())
print(df['Column3'].unique())
print(df['Column1'].head())