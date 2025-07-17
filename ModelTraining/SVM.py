# SVM_ShiftDetection.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset with shift labels
df = pd.read_csv("../DataSets/dataset_with_shift_label.csv")

# Clean data
df['Sentence'] = df['Sentence'].astype(str).str.strip()
df['Shift_Label'] = df['Shift_Label'].astype(str).str.strip()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['Sentence'], df['Shift_Label'], test_size=0.2, random_state=42
)

# Feature extraction
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train SVM
model = SVC(kernel='linear', class_weight='balanced')
model.fit(X_train_vec, y_train)

# Predict & evaluate
y_pred = model.predict(X_test_vec)

print("✅ SVM Classification Report:\n", classification_report(y_test, y_pred))
print("🧮 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("🎯 Accuracy:", model.score(X_test_vec, y_test))
