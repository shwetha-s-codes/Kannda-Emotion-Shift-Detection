import pandas as pd

#reading csv file
df= pd.read_csv("..\dataset_1.csv")
#replacing wrong Labels
df['Part1 Sentiment']=df['Part1 Sentiment'].str.strip().replace("Negative","Negetive")
df['Part2 Sentiment']=df['Part2 Sentiment'].str.strip().replace("Negative","Negetive")
#Removing Unwanted Spaces
df['Sentence']=df['Sentence'].str.strip()
df['Transition Word']=df['Transition Word'].str.strip()
#Saving the changes to csv file
df.to_csv("..\dataset_1.csv",index=False)
print("labels Replaced Sucessfully")
"""print(df['Column2'].unique())
print(df['Column3'].unique())
print(df['Column1'].head())"""