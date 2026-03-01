import os
import pandas as pd
import numpy as np
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🤖 Telegram Cybersecurity Bot Starting...")

# 🔐 Load dataset
data = pd.read_csv("dataset.csv")

questions = data["question"].astype(str).values
answers = data["answer"].astype(str).values

# Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 3)
)
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_query):
    user_query = user_query.lower().strip()

    user_vec = vectorizer.transform([user_query])
    similarity = cosine_similarity(user_vec, question_vectors)

    best_match = np.argmax(similarity)
    confidence = similarity[0][best_match]

    if confidence < 0.15:
        return "❌ I don’t have an exact answer yet. Try rephrasing."

    return answers[best_match]

# ✅ ASYNC reply (required for Railway)
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    answer = get_answer(user_msg)
    await update.message.reply_text(answer)

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("🤖 Telegram Cybersecurity Bot is LIVE")
    app.run_polling()

if __name__ == "__main__":
    main()


   

    