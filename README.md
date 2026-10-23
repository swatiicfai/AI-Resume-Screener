# 🤖 AI Resume Screener

> Built at **MLH Hacktoberfest Hack Day Bengaluru × AWS Student Builder Group** at Atria Institute of Technology

An AI-powered resume screener that matches resumes against job descriptions using **AWS Bedrock (Claude)**. Upload a resume → get a match score, strengths, gaps, and improvement tips instantly.

![Demo](https://img.shields.io/badge/AWS-Bedrock-orange?logo=amazonaws) ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?logo=fastapi) ![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2024-purple)

---

## ✨ Features

- 📄 Upload PDF or TXT resume
- 📋 Paste any job description
- 🎯 Get a **match score (0–100)**
- ✅ Top 3 **strengths** matched
- ⚠️ Top 3 **skill gaps** identified
- 💡 Top 3 **improvement tips**
- ⚡ Powered by **AWS Bedrock (Claude 3 Haiku)**

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10+
- AWS account with **Bedrock access** enabled
- AWS credentials configured (`aws configure` or env vars)

### 2. Enable AWS Bedrock Model Access

1. Go to [AWS Console → Bedrock](https://console.aws.amazon.com/bedrock)
2. Click **Model access** → **Manage model access**
3. Enable **Anthropic Claude 3 Haiku**
4. Click **Save changes**

### 3. Install & Run

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/ai-resume-screener
cd ai-resume-screener

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials (if not already done)
aws configure

# Run the app
python app.py
```

4. Open **http://localhost:8000** in your browser

---

## 🏗️ Architecture

```
Browser (index.html)
    │
    ▼
FastAPI (app.py) ── pdfplumber ──► Extract text from PDF
    │
    ▼
AWS Bedrock (Claude 3 Haiku)
    │
    ▼
JSON: { match_score, strengths, gaps, verdict, tips }
    │
    ▼
Browser renders results
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| AI Model | AWS Bedrock (Claude 3 Haiku) |
| PDF Parsing | pdfplumber |
| Frontend | Vanilla HTML/CSS/JS |

---

## 🌍 Environment Variables

| Variable | Description |
|----------|-------------|
| `AWS_ACCESS_KEY_ID` | Your AWS access key |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key |
| `AWS_DEFAULT_REGION` | AWS region (default: `us-east-1`) |

---

## 📄 License

MIT License — open source for Hacktoberfest 🎃

---

## 🙌 Contributing

PRs welcome! This project is Hacktoberfest-friendly.
1. Fork the repo
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit & push
4. Open a Pull Request
