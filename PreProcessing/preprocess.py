#Removing some punctuation marks to get rid of unwanted data
import re
import pandas as pd

def remove_basic_punct(text):
    # Remove basic punctuation
    text = re.sub(r'[.,;:\'"]', '', text)
    # Normalize spacing: replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()  # Remove leading/trailing spaces

# Load your dataset
df = pd.read_csv("../DataSets/Dataset_3.csv")

# Apply cleanup to the 'Sentence' column
df['Sentence'] = df['Sentence'].astype(str).apply(remove_basic_punct)

#Removing Unwanted Spaces
df['Part1 Sentiment']=df['Part1 Sentiment'].str.strip()
df['Part2 Sentiment']=df['Part2 Sentiment'].str.strip()
df['Sentence']=df['Sentence'].str.strip()
df['Transition Word']=df['Transition Word'].str.strip()


# Save cleaned dataset
df.to_csv("../DataSets/Dataset_3.csv", index=False, encoding='utf-8-sig')
print("✅ Punctuations and extra spaces removed successfully.")
