import pandas as pd


df = pd.read_csv("../DataSets/Merged_dataset.csv")

# Clean and standardize labels
df['Part1 Sentiment'] = df['Part1 Sentiment'].str.strip().str.lower()
df['Part2 Sentiment'] = df['Part2 Sentiment'].str.strip().str.lower()

# Derive shift label
df['Shift_Label'] = df.apply(
    lambda row: 'Yes' if row['Part1 Sentiment'] != row['Part2 Sentiment'] else 'No',
    axis=1
)
df.drop(columns=['Part1 Sentiment','Part2 Sentiment','Transition Word'],inplace=True)

# Save for training
df.to_csv("../DataSets/dataset_with_shift_label.csv", index=False, encoding='utf-8-sig')
print("✅ Shift label added and saved.")
