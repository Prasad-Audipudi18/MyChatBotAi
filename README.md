# Personal AI Assistant for Prasad Audipudi

## 📌 Overview

This project implements a **personal AI assistant** designed specifically to answer questions about **Prasad Audipudi’s professional profile**.  
The assistant responds accurately using **only the information provided** about Prasad and avoids hallucinating or inventing details.

If a question is **outside Prasad’s profile**, the assistant responds helpfully using **general knowledge**.

---

## 🎯 Purpose

The primary goal of this assistant is to:
- Act as a **career-focused AI profile assistant**
- Provide structured, professional answers about Prasad’s background
- Maintain **accuracy, clarity, and professionalism**
- Prevent hallucinated or false personal information

---

## 🧠 Assistant Behavior Rules

The assistant follows these strict rules:

### ✅ When questions are about Prasad Audipudi
- Use **only provided information**
- Never invent education, experience, or skills
- Respond clearly and professionally

### 📄 Resume Requests
- If asked for Prasad’s resume → **return the full resume text**

### 🎓 Education Requests
- If asked about education → **return educational qualifications only**

### 🛠 Skills Requests
- If asked about skills → **list skills clearly**

### 💼 Experience Requests
- If asked about experience → **describe work experience**

### ❌ Unknown or Missing Data
- If information is not available → respond politely and ask for clarification or state that data is not provided

---

## 🌍 Non-Prasad Questions

If the user asks about topics **not related to Prasad**, such as:
- Fitness
- AI & Machine Learning
- Technology
- Programming
- Career advice

➡️ The assistant responds using **general AI knowledge** in a helpful and friendly manner.

---

## 🗣 Example Interactions

### Education
**User:** What is Prasad’s education?  
**Assistant:**  
> Prasad Audipudi has a B.Tech in Computer Science from XYZ University.

---

### Skills
**User:** Tell me about Prasad’s skills.  
**Assistant:**  
> Prasad’s skills include Python, Machine Learning, AI, Flask, Django, and SQL.

---

### General Question (Non-Profile)
**User:** How should I start working out to build muscle?  
**Assistant:**  
> To build muscle, focus on progressive resistance training, compound exercises, adequate protein intake, and proper rest.

---

## 🔒 Key Principles

- ❌ No hallucinated personal data  
- ✅ Clear, concise, professional tone  
- 🧠 Context-aware responses  
- 🔍 Profile-specific answers only when data is provided  

---

## 🚀 Use Cases

- Personal portfolio assistant
- Resume-based chatbot
- Career profile Q&A system
- Interview preparation assistant
- Profess
