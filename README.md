# AI-Driven Citizen Grievance & Sentiment Analysis System

## 📌 Project Overview
This project is an AI-based system that processes citizen complaints and automatically:
- Classifies them into the appropriate government department
- Performs sentiment analysis
- Assigns priority based on urgency

---

## 🎯 Objectives
- Reduce manual effort in complaint handling
- Improve response time
- Provide structured and prioritized grievance data

---

## 🛠️ Technologies Used
- Python
- Pandas, NLTK
- Scikit-learn (TF-IDF, Logistic Regression)
- FastAPI (API development)

---

## ⚙️ Features
- Text preprocessing (cleaning, tokenization, lemmatization)
- Department classification using ML model
- Sentiment analysis (Positive/Negative)
- Priority assignment (High/Low)
- REST API for real-time predictions

---

## 🚀 How to Run

### 1. Install Dependencies

### 2. Run API

### 3. Open in Browser

---
## 🔗 API Endpoint

### POST /predict

This endpoint accepts a citizen complaint and returns:
- Predicted Department
- Sentiment
- Priority level

---

---

## 📊 Example Input
```json
{
  "complaint": "Street light not working"
}


