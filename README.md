# 🤖 AI-Resume-Screener

> **Built at MLH Hacktoberfest Hack Day Bengaluru × AWS Student Builder Group at Atria Institute of Technology**

Upload a resume, paste a job description — get an AI match score instantly using **AWS Bedrock (Claude 3 Haiku)**.

[![Best Open-Source AI Project](https://img.shields.io/badge/DigitalOcean-Best%20Open--Source%20AI%20Project-0080FF?logo=digitalocean)](https://github.com/swatiicfai/AI-Resume-Screener)
[![Best Use of AWS](https://img.shields.io/badge/AWS-Best%20Use%20of%20AWS-FF9900?logo=amazonaws)](https://github.com/swatiicfai/AI-Resume-Screener)
[![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2026-purple)](https://github.com/swatiicfai/AI-Resume-Screener)
[![Demo](https://img.shields.io/badge/Demo-YouTube-red?logo=youtube)](https://youtu.be/zarAvd-Su30)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?logo=fastapi)](https://fastapi.tiangolo.com)

---

## 🎬 Demo Video

[![Watch Demo](https://img.shields.io/badge/Watch%20Demo-YouTube-red?logo=youtube&style=for-the-badge)](https://youtu.be/zarAvd-Su30)

> Click above to watch the full demo with AI voiceover explanation

---

## ✨ What It Does

AI Resume Screener uses **AWS Bedrock (Claude 3 Haiku)** to automatically screen resumes against job descriptions.

1. 📄 Upload your **resume** (PDF or TXT)
2. 📋 Paste any **job description**
3. 🎯 Get instant AI analysis:
   - **Match Score** (0–100)
   - ✅ Top 3 **Strengths** matched
   - ⚠️ Top 3 **Skill Gaps** identified
   - 💡 Top 3 **Improvement Tips**

---

## 🏗️ Architecture

```
Browser (index.html)
    │
    ▼
FastAPI (app.py) ── pdfplumber ──► Extract text from PDF
    │
    ▼
AWS Bedrock (Claude 3 Haiku) via boto3
    │
    ▼
JSON: { match_score, strengths, gaps, verdict, tips }
    │
    ▼
Browser renders results
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- AWS account with **Bedrock access** enabled for Claude 3 Haiku

### 1. Enable AWS Bedrock Model Access

1. Go to [AWS Console → Bedrock → Model access](https://console.aws.amazon.com/bedrock/home#/modelaccess)
2. Enable **Anthropic Claude 3 Haiku**
3. Save changes

### 2. Install & Run

```bash
git clone https://github.com/swatiicfai/AI-Resume-Screener
cd AI-Resume-Screener

pip install -r requirements.txt

# Configure AWS credentials
aws configure

python app.py
```

Open **http://localhost:8000** 🚀

### Environment Variables (alternative to `aws configure`)

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| AI Model | **AWS Bedrock** (Claude 3 Haiku) |
| PDF Parsing | pdfplumber |
| Frontend | Vanilla HTML/CSS/JS |
| AI Integration | boto3 |

---

## 🏆 Prize Categories

- 🥇 **Best Use of AWS** — Core AI inference runs on AWS Bedrock using Claude 3 Haiku via boto3. No third-party AI API — AWS is the sole AI backbone.
- 🌊 **Best Open-Source AI Project** (DigitalOcean) — Fully open-source under MIT License, Hacktoberfest-ready. Fork, contribute, and self-host in minutes.

---

## 🌍 Contributing

This project is **Hacktoberfest-friendly**! PRs welcome.

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'Add some feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request 🎉

---

## 📄 License

[MIT](LICENSE) — free and open source.
