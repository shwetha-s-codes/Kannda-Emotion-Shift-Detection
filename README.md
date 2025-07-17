#  Emotion Shift Prediction in Manually Annotated Kannada Text

##  Objective  
To detect **emotion shifts** within a **single sentence** written in the Kannada language using traditional machine learning models.

---

## 📜 Description  

This project involves the **manual annotation of Kannada sentences** that exhibit emotional transitions. Each sentence contains a shift from one emotion to another — such as from *positive to negative* — and includes common Kannada conjunctions like:  
**ಆದರೆ**, **ಆದ್ದರಿಂದ**, **ಅಥವಾ**, **ಒಂದು ವೇಳೆ**, etc., which often signal a change in sentiment.

The sentences were labeled using three emotions:
- `Positive`
- `Negative`
- `Neutral`

The sentence-level data was then transformed into a binary classification task where the model predicts:
- `Yes` → if there's an emotion shift
- `No` → if the emotion remains consistent

---

## 🛠️ Steps

### 🧹 Preprocessing
- Removed unwanted characters such as `'`, `"`, `;`, `:` (retained `!`, `?` as they contribute to emotional tone).
- **Normalized** Kannada text using the [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library).
- Removed **duplicate sentences**.
- Handled inconsistent spacing and punctuation.

### 🔍 Feature Extraction
- Applied **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization for textual feature representation.

### 🧪 Model Training
Trained the following ML models to classify emotion shift:
- Logistic Regression
- Support Vector Machine (SVM)
- Naive Bayes

---

## 📈 Accuracy Results

| Model              | Accuracy |
|-------------------|----------|
| Logistic Regression | 68%      |
| SVM                | 72%      |
| Naive Bayes        | **78%** *(though biased toward predicting "Yes")*  

> ⚠️ Note: Due to class imbalance (`Yes`: 177, `No`: 69), metrics such as precision/recall should be considered in addition to accuracy.

---

## 📁 Dataset Structure (Post-processing)

Each sentence is labeled with:
- `Original Sentence`
- `Part 1` + `Sentiment 1`
- `Part 2` + `Sentiment 2`
- `Transition Word`
- `Shift_Label`: Yes/No

---

## 📂 Data Source

> The base text corpus used for manual annotation was extracted from the following publicly available Kaggle dataset:  
> 🔗 [CC100-CCNet Kannada Dataset by Darshan Adiga](https://www.kaggle.com/datasets/darshanadiga/cc100ccnetkannada)  
>  
> The dataset was unannotated and web-scraped; only **emotion-shifting sentences were extracted using python script  and labeled manually** from it for the purpose of this research project.

---

## 📚 Libraries Used

- `pandas`
- `scikit-learn`
- `re` (for regex-based preprocessing)
- [`Indic NLP Library`](https://github.com/anoopkunchukuttan/indic_nlp_library) (for Kannada normalization)

---

## 🔄 Status / Update

> 🚧 **Project Paused at Traditional ML Stage**  
> This project currently uses **Logistic Regression, SVM, and Naive Bayes**. The goal is to eventually improve sentiment shift prediction using **Deep Learning models** such as BiLSTM or Transformer-based architectures.

---

## 🧷 Citation

This project uses the [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library).  
**Citation**:  
Anoop Kunchukuttan, *The Indic NLP Library*  
GitHub: [https://github.com/anoopkunchukuttan/indic_nlp_library](https://github.com/anoopkunchukuttan/indic_nlp_library)

---

## 👤 Author

*This project was created as an academic exploration into Kannada NLP. Manual annotation, data preprocessing, and modeling were done individually to gain experience in real-world NLP pipeline development.*

---

