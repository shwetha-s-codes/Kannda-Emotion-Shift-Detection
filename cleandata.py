import pandas as pd
import re

# Load extracted sentences from CSV
df = pd.read_csv("extracted_sentences.csv", encoding="utf-8")

def clean_text(text):
    text = text.strip()  # Remove leading/trailing spaces
    text = re.sub(r"[^\w\s.,!?]", "", text)  # Keep only words, spaces, and common punctuation
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    return text

# Apply cleaning function to the 'Sentence' column
df["Sentence"] = df["Sentence"].apply(clean_text)

# Drop duplicate sentences
df.drop_duplicates(subset=["Sentence"], inplace=True)

# Save cleaned data
df.to_csv("cleaned_sentences.csv", index=False, encoding="utf-8")
print("✅ Cleaning complete! Data saved in 'cleaned_sentences.csv'")
