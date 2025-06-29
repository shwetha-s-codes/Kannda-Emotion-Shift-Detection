#Using Logostic Regression for Model Training

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load preprocessed, split dataset
df = pd.read_csv("../dataset_split_without_transition.csv")  # Update path if needed

# Flatten into one list: text + label
df_part1 = df[['part1_sentence', 'Part1 Sentiment']].rename(columns={'part1_sentence': 'text', 'Part1 Sentiment': 'label'})
df_part2 = df[['part2_sentence', 'Part2 Sentiment']].rename(columns={'part2_sentence': 'text', 'Part2 Sentiment': 'label'})
df_flat = pd.concat([df_part1, df_part2], ignore_index=True)

# Clean text and labels
df_flat['text'] = df_flat['text'].astype(str).str.strip()
df_flat['label'] = df_flat['label'].astype(str).str.strip()

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df_flat['text'], df_flat['label'], test_size=0.2, random_state=42)

# Feature extraction
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train logistic regression model
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)

print("\n✅ Classification Report:")
print(classification_report(y_test, y_pred))

print("\n🧮 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n🎯 Accuracy:", model.score(X_test_vec, y_test))
