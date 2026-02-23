# backend/conversation_manager.py

from config.settings import MAX_HISTORY


class ConversationManager:
    """
    Manages structured chat history for multi-turn conversations.
    """

    def __init__(self):
        self.max_history = MAX_HISTORY
        self.chat_history = []

    # -----------------------------
    # Add Messages
    # -----------------------------
    def add_user_message(self, message: str):
        self.chat_history.append({
            "role": "user",
            "content": message.strip()
        })
        self._trim_history()

    def add_assistant_message(self, message: str):
        self.chat_history.append({
            "role": "assistant",
            "content": message.strip()
        })
        self._trim_history()

    # -----------------------------
    # Get Chat History
    # -----------------------------
    def get_history(self):
        return self.chat_history

    # -----------------------------
    # Clear Chat History
    # -----------------------------
    def clear_history(self):
        self.chat_history = []

    # -----------------------------
    # Trim History (Token Control)
    # -----------------------------
    def _trim_history(self):
        """
        Keeps only the most recent MAX_HISTORY messages
        to prevent excessive token usage.
        """
        if len(self.chat_history) > self.max_history:
            self.chat_history = self.chat_history[-self.max_history:]