#Using tf-idf for feature extraction

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Load the split dataset
df = pd.read_csv("../dataset_split_with_transition.csv")  # Update filename if needed

# Flatten into one column for text, one for label
df_part1 = df[['part1_sentence', 'Part1 Sentiment']].rename(columns={'part1_sentence': 'text', 'Part1 Sentiment': 'label'})
df_part2 = df[['part2_sentence', 'Part2 Sentiment']].rename(columns={'part2_sentence': 'text', 'Part2 Sentiment': 'label'})
df_flat = pd.concat([df_part1, df_part2], ignore_index=True)

# Clean just in case
df_flat['text'] = df_flat['text'].astype(str).str.strip()
df_flat['label'] = df_flat['label'].astype(str).str.strip()

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df_flat['text'], df_flat['label'], test_size=0.2, random_state=42)

# Apply TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("✅ Feature extraction complete.")
print("🔢 Shape of training data:", X_train_vec.shape)
