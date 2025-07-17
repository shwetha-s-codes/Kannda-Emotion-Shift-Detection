import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load data
df = pd.read_csv("../DataSets/dataset_with_shift_label.csv")



# Features and label
X = df['Sentence']
y = df['Shift_Label'].str.strip()  # 'Yes' or 'No'

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train binary classifier
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)

print("\n✅ Classification Report:")
print(classification_report(y_test, y_pred))

print("\n🧮 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n🎯 Accuracy:", model.score(X_test_vec, y_test))

# Optional: Save predictions
results_df = pd.DataFrame({
    'Combined_Text': X_test,
    'True_Shift_Label': y_test,
    'Predicted_Shift_Label': y_pred
})
results_df.to_csv("shift_predictions.csv", index=False, encoding='utf-8-sig')
print(" Shift predictions saved.")
