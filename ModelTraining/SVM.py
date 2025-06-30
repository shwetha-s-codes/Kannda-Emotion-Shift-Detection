import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load your cleaned, split dataset
df = pd.read_csv("../DataSets/dataset_split_with_transition.csv")  # Update if needed

# Flatten part1 and part2 into one dataset
df_part1 = df[['part1_sentence', 'Part1 Sentiment']].rename(columns={'part1_sentence': 'text', 'Part1 Sentiment': 'label'})
df_part2 = df[['part2_sentence', 'Part2 Sentiment']].rename(columns={'part2_sentence': 'text', 'Part2 Sentiment': 'label'})
df_flat = pd.concat([df_part1, df_part2], ignore_index=True)

# Clean the text and labels
df_flat['text'] = df_flat['text'].astype(str).str.strip()
df_flat['label'] = df_flat['label'].astype(str).str.lower().str.strip()

# Optional: print class distribution
print("🧾 Class distribution:\n", df_flat['label'].value_counts(), "\n")

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    df_flat['text'], df_flat['label'], test_size=0.2, random_state=42)

# TF-IDF feature extraction
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Compute class weights manually for SVM
classes = np.unique(y_train)
weights = compute_class_weight(class_weight='balanced', classes=classes, y=y_train)
class_weights = dict(zip(classes, weights))

# Train the SVM model
model = LinearSVC(class_weight=class_weights, max_iter=1000)
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)

print("✅ Classification Report:\n")
print(classification_report(y_test, y_pred))

print("\n🧮 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n🎯 Accuracy:", model.score(X_test_vec, y_test))
