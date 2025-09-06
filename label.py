import pandas as pd

df=pd.read_csv("DataSets/dataset_with_shift_label.csv")
count=df['Shift_Label'].value_counts()
print(count)