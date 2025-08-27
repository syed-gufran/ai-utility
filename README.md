🧩 AI Utility (Gemini-powered)
A multi-purpose AI app built with Streamlit and Google Gemini API that combines multiple AI utilities into a single, clean interface.
✨ Features include:
🤖 Chatbot – conversational AI with memory
🖼️ Image Captioning – generate detailed captions for uploaded images
📝 Text Embedding – convert text into numerical vectors for ML & similarity tasks
❓ Ask Me Anything – get quick answers to any question
🚀 Demo
Run locally and access a simple sidebar-based navigation for switching between tools.
🛠️ Tech Stack
Python
Streamlit (UI framework)
Google Gemini API (genai)
PIL (Pillow) for image handling
dotenv for secure API key management
📦 Installation & Setup
Clone the repository
git clone https://github.com/your-username/ai-utility.git
cd ai-utility
Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
Install dependencies
pip install -r requirements.txt
Set up environment variables
Create a .env file in the project root:
GOOGLE_API_KEY=your_google_gemini_api_key_here
Run the app
streamlit run app.py
🎯 Features in Detail
🤖 Chatbot
Interactive Gemini-powered chatbot with session memory
Clear chat history option in sidebar
🖼️ Image Captioning
Upload .jpg, .jpeg, or .png images
Generates a natural language caption using Gemini
📝 Text Embedding
Convert any text into embeddings
Displays embedding dimension, preview values, and CSV download option
❓ Ask Me Anything
Get direct responses from Gemini to any input question
