import pandas as pd

# Load both datasets
df1 = pd.read_csv("../DataSets/Dataset_3.csv")
df2 = pd.read_csv("../DataSets/Merged_dataset.csv")

# Optional: ensure consistent column order and names 
df2 = df2[df1.columns]  

# Merge the datasets
df_combined = pd.concat([df1, df2], ignore_index=True)

# Clean up sentence column to avoid spacing-based mismatches
df_combined['Sentence'] = df_combined['Sentence'].astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Remove duplicates based on the full sentence
df_combined = df_combined.drop_duplicates(subset='Sentence', keep='first')

# Save the merged dataset
df_combined.to_csv("../DataSets/Merged_dataset.csv", index=False, encoding='utf-8-sig')

print(f"✅ Merged dataset saved as 'merged_dataset.csv' with {len(df_combined)} rows.")
