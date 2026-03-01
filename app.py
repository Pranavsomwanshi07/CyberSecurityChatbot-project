from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

print("🔐 Cybersecurity AI Assistant Initialized")

# Load dataset
data = pd.read_csv("dataset.csv")

questions = data["question"].astype(str).tolist()
answers = data["answer"].astype(str).tolist()

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data_json = request.get_json()
    user_question = data_json.get("message", "").lower()

    user_vec = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vec, X)
    best = np.argmax(similarity)
    score = similarity[0][best]

    if score < 0.2:
        return jsonify({
            "answer": "❌ I don’t know this yet.",
            "confidence": 0
        })

    return jsonify({
        "answer": answers[best],
        "confidence": round(score * 100, 2)
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)