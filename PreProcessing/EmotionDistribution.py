#Python Script to Analyze number of labels belonging to each category
import pandas as pd

# Load your CSV file
df = pd.read_csv("../DataSets/Merged_dataset.csv")

# To ensure Consistency
df['Part1 Sentiment'] = df['Part1 Sentiment'].str.strip().str.lower()
df['Part2 Sentiment'] = df['Part2 Sentiment'].str.strip().str.lower()

#  Count how many times each individual sentiment appears
#value_counts() function does this job 

print(df['Part1 Sentiment'].value_counts())

print(df['Part2 Sentiment'].value_counts())

#  Count sentiment shift pairs (e.g., positive → negative)
df['sentiment_transition'] = df['Part1 Sentiment'] + " → " + df['Part2 Sentiment']
print("\n Sentiment transition counts:")
print(df['sentiment_transition'].value_counts())


