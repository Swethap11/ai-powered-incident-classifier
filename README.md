# ⚙️ AI-Powered Incident Classifier for DevOps Teams

A smart, ML-driven system to automatically classify DevOps system logs (e.g., crash, auth, memory) and trigger alerts or actions like Slack notifications. Built to support scalable, automated incident response in production environments.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

---

## 🚀 Features

- 🔍 **Log Simulation**: Generate realistic logs (auth issues, crashes, memory leaks, etc.)
- 🤖 **NLP/ML Classification**: Identify incident types using keyword-based or machine learning models
- 🔗 **Integration-Ready**: Supports Slack API integration for incident workflows
- ☁️ **Cloud Deployable**: Docker-ready, runs on AWS Lambda, EC2, or local
- 📊 **Dashboard Hooks**: JSON/API outputs for frontend dashboard integration

---

## 🛠️ Tech Stack

| Layer         | Technology |
|---------------|------------|
| Language      | Python     |
| ML Model      | Logistic Regression / BERT (planned) |
| APIs          | Slack      |
| Deployment    | AWS Lambda / EC2 / Docker |
| Visualization | (Optional) React-based dashboard |

---

## 📂 Project Structure

devops-incident-classifier/
├── simulate_logs.py # Generates mock logs
├── classify_logs.py # Classifies logs (rule-based or ML)
├── integrations/
│ └── slack.py # Slack notifications (optional)
├── models/ # Trained ML models (joblib/pickle)
├── logs/ # Sample log files
├── Dockerfile # For containerization
├── README.md
└── requirements.txt



---

## 📦 Installation

```bash
git clone https://github.com/swethap11/ai-powered-incident-classifier.git
cd ai-powered-incident-classifier
pip install -r requirements.txt
python simulate_logs.py
python classify_logs.py

--- 

##  🧠 Planned Enhancements
 Replace rule-based logic with ML model (BERT or fine-tuned classifier)

 Auto-create tickets for critical incidents

 Dashboard to display live classified stats

 Deploy on AWS Lambda with CI/CD