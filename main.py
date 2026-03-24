from fastapi import FastAPI
import pickle
from transformers import pipeline

app = FastAPI()   # ⭐ VERY IMPORTANT

# Load models
model = pickle.load(open("department_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))
sentiment_model = pipeline("sentiment-analysis")

def predict_department(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]

@app.post("/predict")
def predict(data: dict):

    text = data["complaint"]

    dept = predict_department(text)

    sentiment = sentiment_model(text[:512])[0]['label']

    if sentiment == "NEGATIVE":
        priority = "High"
    else:
        priority = "Low"

    return {
        "Department": dept,
        "Sentiment": sentiment,
        "Priority": priority
    }