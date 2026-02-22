# bioinformatics-genai-chatbot
# 🧬 Bioinformatics GenAI Chatbot (Production-Ready)

## 📌 Project Title
Building a Production-Ready Domain-Specific Chatbot using Gemini GenAI API

---

## 🚀 Project Overview

This project demonstrates the design, development, and deployment of a production-ready domain-specific chatbot powered by the Google Gemini GenAI API.

The chatbot is specialized in **Bioinformatics and Genomics** and follows real-world AI engineering best practices including:

- Secure API integration
- Modular backend architecture
- Multi-turn conversation memory
- Advanced prompt engineering
- Token optimization
- Logging and error handling
- Public cloud deployment on AWS EC2

This system simulates a real-world GenAI SaaS architecture.

---

## 🎯 Domain Focus

The chatbot specializes in:

- Genomics workflows
- RNA-seq analysis
- Single-cell RNA-seq
- WGCNA & GSEA
- Variant calling pipelines
- Pathway enrichment analysis
- Molecular docking guidance
- Computational biology tools

---

## 🏗 System Architecture
User
↓
Streamlit UI
↓
Memory Module
↓
Prompt Engineering Module
↓
Gemini API Service
↓
Response Processing
↓
UI Rendering


---

## 🔐 Security Best Practices

- API key stored in `.env`
- No hardcoded credentials
- `.gitignore` prevents sensitive files from being uploaded
- Modular separation between UI and backend

---

## 🧠 Key Features

### ✅ Proper Gemini API Integration
- Uses `google-genai` SDK
- Structured request handling
- Error handling with retry logic
- Logging of API responses
- Token usage optimization

### ✅ Multi-Turn Conversation Memory
- Session-based memory using Streamlit session state
- Context preservation
- Recent history window for performance optimization

### ✅ Advanced Prompt Engineering
- Structured system prompt
- Domain-specific constraints
- Hallucination control
- Academic formatting rules

### ✅ Interactive UI
- Chat-style interface
- Real-time responses
- Conversation history display
- Loading spinner
- Clean user experience

### ✅ Cloud Deployment
- Deployed on AWS EC2
- Public IP accessible
- Custom security group configuration
- Streamlit served on port 8501

---

## 🛠 Installation (Local Setup)

### 1️⃣ Clone Repository
