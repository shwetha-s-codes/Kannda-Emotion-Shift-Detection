#Removing some punctuation marks to get rid of unwanted data
import re
import pandas as pd

def remove_basic_punct(text):
    return re.sub(r'[.,;: \']', '', text)  

df=pd.read_csv("../dataset_1.csv")

df['Sentence'] = df['Sentence'].apply(remove_basic_punct)
df.to_csv("../dataset_1.csv")
print("Punctuations Removed Sucessfully")
