from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt

# Load environment variables from .env
load_dotenv()

# Initialize Groq model with Qwen 32B
model = ChatGroq(model_name="qwen-qwq-32b")

st.title("Dhairya Research Paper Explainer")

# Dropdowns for input
paper_input = st.selectbox(
    " Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "🎨 Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "📏 Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load custom prompt
template = load_prompt("template.json")

if st.button("Summarize"):
    chain = template | model
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(response.content)
