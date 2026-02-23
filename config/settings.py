# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# -----------------------------
# Gemini Configuration
# -----------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3-70b-8192")


# -----------------------------
# Application Configuration
# -----------------------------
APP_TITLE = "AI Career Advisor Chatbot"
APP_ICON = "🎯"


# -----------------------------
# Conversation Settings
# -----------------------------
# Maximum number of messages stored in memory
# (Helps control token usage)
MAX_HISTORY = int(os.getenv("MAX_HISTORY", 6))


# -----------------------------
# Logging Settings
# -----------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = "logs"


# -----------------------------
# Validation Check
# -----------------------------
if not GROQ_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please set it in your .env file."
    )