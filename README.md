# 🛡️ SafeUPI - AI-Powered UPI Fraud Detection & Prevention System

SafeUPI is an intelligent, real-time UPI transaction simulator and security shield built with **Streamlit** and **Machine Learning**. It evaluates transaction parameters, analyzes behavioral biometrics, and scans transaction remarks for fraudulent keywords to protect users from financial scams and unauthorized deductions.

---

## 🌟 Table of Contents
- [Key Features](#-key-features)
- [Project Architecture & Workflow](#-project-architecture--workflow)
- [Tech Stack & Libraries](#-tech-stack--libraries)
- [Project Directory Structure](#-project-directory-structure)
- [Getting Started Locally](#-getting-started-locally)
- [How It Works (Logic Flow)](#-how-it-works-logic-flow)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## ✨ Key Features

- **🤖 AI-Driven Behavioral Analysis:** Evaluates key transaction metrics such as amount, transaction hour, daily frequency, and distance from home to detect anomalous patterns.
- **🔍 Smart Remark Keyword Filtering:** Instantly overrides and blocks transactions containing high-risk scam keywords (e.g., *"lottery"*, *"prize"*, *"urgent"*, *"win"*, *"gift"*, *"kbc"*, *"job"*).
- **🔊 Conditional Voice Alerts:** Provides instant auditory feedback using synthesized voice alerts for both successful transactions and blocked security threats.
- **⚡ Interactive Streamlit Dashboard:** A clean, responsive, and user-friendly interface designed for seamless transaction simulation.

---

## 📊 Project Architecture & Workflow

```text
[ User Input (Amount, UPI ID, Remark) ]
                 │
                 ▼
     [ Click: "Pay Securely" ]
                 │
                 ▼
   [ AI Model (Behavioral Check) ]
                 │
                 ▼
[ Remark Keyword Filter (Override Logic) ]
        │                       │
        ▼                       ▼
    (Fraud Found)          (Safe Transaction)
        │                       │
        ▼                       ▼
 🚨 Block + Voice Alert    ✅ Success + Ballons

 
📂 project directory structure
safe-upi-demo/
│
├── app.py                 # Main Streamlit application script
├── train.py               # Model training / extra script (Aapki nayi file)
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation

🚀 Getting Started Locally
Follow these steps to set up and run the project on your local machine:
1. Clone the Repository
git clone [https://github.com/your-username/safe-upi-demo.git](https://github.com/your-username/safe-upi-demo.git)
cd safe-upi-demo
2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Streamlit App
streamlit run app.py
💡 How It Works (Logic Flow)
Input Parameters: The user fills in the recipient UPI ID, transaction amount, transaction hour, frequency, distance, and custom remark notes.

AI Shield Verification: Upon clicking "Pay Securely via UPI", the system runs an initial machine learning prediction based on behavioral metrics.

Keyword Override: The application scans the transaction remark for social engineering and scam keywords. If a match is found, the is_fraud flag is overridden to True.

Action & Feedback:

If flagged as fraudulent, the payment is blocked (st.error), the risk factor is displayed, and an alert voice is triggered.

If safe, a success message appears (st.success) with celebratory elements and confirmation audio.

🚀 Future Enhancements
Real-time Bank API Integration: Connecting with sandbox UPI gateways for live status checks.

Advanced NLP Sentiment Analysis: Moving beyond keyword matching to contextual threat detection in remarks using transformer models.

Multi-language Voice Support: Adding regional voice alerts (Hindi, Bengali, Tamil, etc.) for broader accessibility.

🛡️ License
This project is open-source and developed for educational, cybersecurity awareness, and hackathon purposes.
