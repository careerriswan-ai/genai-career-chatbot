# app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from backend.groq_client import GroqClient
from backend.conversation_manager import ConversationManager
from prompts.prompt_builder import build_prompt


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Career Advisor Chatbot")
st.markdown("Get structured, realistic, and personalized career guidance.")


# -----------------------------
# Initialize Session State
# -----------------------------
if "conversation" not in st.session_state:
    st.session_state.conversation = ConversationManager()

if "gemini_client" not in st.session_state:
    st.session_state.groq_client = GroqClient()


# -----------------------------
# Sidebar Controls
# -----------------------------
with st.sidebar:
    st.header("⚙ Settings")

    st.markdown("**Model:** Groq ")

    if st.button("🗑 Clear Chat History"):
        st.session_state.conversation = ConversationManager()
        st.success("Chat history cleared.")

    st.markdown("---")
    st.markdown("### 📌 Tips")
    st.markdown("""
    - Mention your education background  
    - Include years of experience  
    - Specify your career goal  
    - Mention your location for salary guidance  
    """)


# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.conversation.get_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Ask about your career...")

if user_input:

    # Add user message to history
    st.session_state.conversation.add_user_message(user_input)

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.spinner("Analyzing your career path..."):

        prompt = build_prompt(
            user_input=user_input,
            chat_history=st.session_state.conversation.get_history()
        )

        response = st.session_state.groq_client.generate_response(prompt)

    # Add assistant response to history
    st.session_state.conversation.add_assistant_message(response)

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response)