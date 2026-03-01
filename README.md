# 🔐 Cybersecurity AI Chatbot

A Cybersecurity Question–Answer Chatbot built using **Python, Machine Learning (TF-IDF)** and **Telegram Bot API**.  
This chatbot answers cybersecurity-related questions like **password attacks, malware, firewall, phishing**, etc.

The bot can be:
- Run on a **local system**
- Used directly on **Telegram**
- Deployed **24/7 online using Railway (Free Tier)**

---

## 📌 Features

- 🤖 AI-based question matching using **TF-IDF + Cosine Similarity**
- 📚 CSV-based dataset (easy to expand to 500–1000+ questions)
- 🔐 Focused on cybersecurity concepts
- 💬 Works on **Telegram**
- ☁️ Can run online even when laptop is OFF
- 🆓 Uses only free tools

---

## 🛠️ Technologies Used

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- python-telegram-bot
- Railway (Cloud Deployment)

---

## 📁 Project Structure
CyberSecurityChatbot/
│
├── dataset.csv # Cybersecurity Q&A dataset
├── telegram.py # Telegram bot code
├── requirements.txt # Required Python libraries
├── README.md # Project documentation


---

## 📄 Dataset Format (`dataset.csv`)

Your dataset must follow this exact format:

```csv
question,answer,category,level
what is firewall,"A firewall monitors and filters network traffic.",Network Security,Beginner
ways hackers steal passwords,"Hackers use phishing, malware, brute force, and spyware.",Passwords,Beginner
what is malware,"Malware is malicious software designed to harm systems.",Malware,Beginner

requirements.txt

pandas
numpy
scikit-learn
python-telegram-bot==13.15

Run Bot Locally (Testing)
python telegram.py