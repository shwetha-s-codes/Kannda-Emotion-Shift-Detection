import pandas as pd

# Load the dataset
df = pd.read_csv("../dataset_1.csv")  # Replace with your actual file name

# Check how many total and duplicate sentences exist
print(f"Original total rows: {len(df)}")
print(f"Duplicate sentences: {df.duplicated(subset='Sentence').sum()}")

# Remove duplicates based on the 'sentence' column
#df_cleaned = df.drop_duplicates(subset='Sentence', keep='first')  # keep='first' keeps the first occurrence

# Save to a new CSV file
#df_cleaned.to_csv("../dataset_1.csv", index=False, encoding="utf-8-sig")

#print("✅ Duplicates removed and saved to 'dataset_1_deduplicated.csv'")
#print(f"Remaining rows: {len(df_cleaned)}")
