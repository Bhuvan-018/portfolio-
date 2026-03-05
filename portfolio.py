import streamlit as st

st.set_page_config(page_title="AI Portfolio - Bhuvanesh", layout="centered")

st.title("🚀 My AI Project Portfolio")
st.write("Here are my deployed AI projects across NLP, Computer Vision, Audio, and OCR:")

projects = [
    {
        "title": "🤖 AI Chatbot with Contextual Memory",
        "desc": "Conversational bot that remembers past queries and responds contextually.",
        "link": "https://chatbot018.streamlit.app/"
    },
    {
        "title": "😷 Face Mask Detection",
        "desc": "Computer vision model that detects whether a person is wearing a mask.",
        "link": "https://maskdetecter.streamlit.app/"
    },
    {
        "title": "🎵 AI Music Genre Classification",
        "desc": "Classifies uploaded audio tracks into genres using spectrograms + CNN.",
        "link": "https://musicgenre18.streamlit.app/"
    },
    {
        "title": "✍️ AI-Powered Handwriting Recognition",
        "desc": "OCR-style system that converts handwritten notes into digital text.",
        "link": "https://huggingface.co/spaces/bhuvan-018/handwriting-recognition"
    },
    {
        "title": "📄 Text Summarization with Transformers",
        "desc": "Summarizes long articles into concise, readable abstracts using transformer models.",
        "link": "https://textsummarizer-glw2hytorsxaz83rdggxxv.streamlit.app/"
    }
]

for p in projects:
    st.subheader(p["title"])
    st.write(p["desc"])
    st.markdown(f"[👉 Try it here]({p['link']})")
    st.markdown("---")