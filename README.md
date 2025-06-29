# 🧠 Dhairya Research Paper Explainer

This is an interactive **Streamlit-based chatbot** that uses **Groq’s Qwen 32B model** to explain landmark research papers in AI. It dynamically generates explanations based on user-selected paper, style, and length — making cutting-edge research more accessible to everyone.

🚀 Features

- 🔎 **Select from top AI research papers**
- 🎨 **Choose explanation style**: Beginner, Technical, Code-Oriented, or Mathematical
- 📏 **Control explanation length**: Short, Medium, or Long
- ⚡ Powered by **Groq's Qwen-Qwen1.5-32B LLM**
- 🌐 Live interface via **Streamlit**

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- `.env` for API key management (kept private via `.gitignore`)

📦 Setup Instructions

1. Clone the Repo

bash
git clone https://github.com/dhairyagupta22/Chatbot.git
cd Chatbot

python3 -m venv venv
source venv/bin/activate

pip install streamlit langchain langchain-groq python-dotenv

GROQ_API_KEY=your_groq_api_key_here

streamlit run Chatbot.py
