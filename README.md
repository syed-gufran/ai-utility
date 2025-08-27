# 🧩 AI Utility (Gemini-powered)  

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)  

A **multi-purpose AI web app** built with **Streamlit** and **Google Gemini API**, designed to make experimenting with LLMs fun and easy.  
With a clean sidebar navigation, you can switch between multiple AI-powered utilities in seconds.  

---

## ✨ Features  

- 🤖 **Chatbot** – conversational AI with memory persistence  
- 🖼️ **Image Captioning** – generate natural captions for uploaded images  
- 📝 **Text Embedding** – create embeddings for ML/similarity tasks with download option  
- ❓ **Ask Me Anything** – quick Q&A powered by Gemini  

---

## 🛠️ Tech Stack  

- **[Streamlit](https://streamlit.io/)** – interactive UI  
- **[Google Gemini API](https://ai.google.dev/)** – core AI capabilities  
- **[Pillow (PIL)](https://pillow.readthedocs.io/)** – image handling  
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** – API key management  
- **streamlit-option-menu** – sidebar navigation  

---

## ⚡ Quick Start  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/ai-utility.git
   cd ai-utility
   ```

2. **(Optional) Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Key**  
   Create a `.env` file in the root directory and add your Gemini API key:  
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the app**  
   ```bash
   streamlit run app.py
   ```

---

## 🎯 How It Works  

### 🤖 Chatbot  
- Keeps track of session history  
- Supports clearing chat from sidebar  

### 🖼️ Image Captioning  
- Upload `.jpg`, `.jpeg`, `.png`  
- AI generates descriptive captions  

### 📝 Text Embedding  
- Input any text  
- Generates embeddings with dimension info  
- CSV download option for further use  

### ❓ Ask Me Anything  
- Enter your question → get instant Gemini-powered answers  

---



Install with:  
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing  

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a PR.  

---

🔥 Ready to run AI tools all in one place — start chatting, captioning, embedding, and asking with **AI Utility**!  
