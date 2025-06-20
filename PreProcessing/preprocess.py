import pandas as pd

#reading csv file
df= pd.read_csv("..\dataset_1.csv")
#replacing wrong Labels
df['Column2']=df['Column2'].str.strip().replace("Negative","Negetive")
df['Column3']=df['Column3'].str.strip().replace("Negative","Negetive")
#Removing Unwanted Spaces
df['Column1']=df['Column1'].str.strip()
df['Column4']=df['Column4'].str.strip()
#Saving the changes to csv file
df.to_csv("..\dataset_1.csv",index=False)
print("labels Replaced Sucessfully")
print(df['Column2'].unique())
print(df['Column3'].unique())
print(df['Column1'].head())