from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model + vectorizer
model = joblib.load("../ModelTraining/svm_model_new.pkl")
vectorizer = joblib.load("../ModelTraining/tfidf_vectorizer_new.pkl")

# Initialize FastAPI app
app = FastAPI(title="Kannada Emotion Shift Detection API")

# Define request body
class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Kannada Emotion Shift Detection API is running!"}

@app.post("/predict")
def predict(data: InputText):
    # Vectorize input text
    X = vectorizer.transform([data.text])
    
    # Predict label
    prediction = model.predict(X)[0]

    return {"text": data.text, "prediction": prediction}
