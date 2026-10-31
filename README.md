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
