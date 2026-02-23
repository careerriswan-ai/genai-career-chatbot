from prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(user_input: str, chat_history: list) -> str:
    """
    Combines system prompt, conversation history, and current user input
    into a single formatted prompt for Gemini.
    """

    formatted_history = ""

    for message in chat_history:
        role = message["role"]
        content = message["content"]

        if role == "user":
            formatted_history += f"User: {content}\n"
        elif role == "assistant":
            formatted_history += f"Career Advisor: {content}\n"

    final_prompt = f"""
{SYSTEM_PROMPT}

-----------------------------
CONVERSATION HISTORY
-----------------------------
{formatted_history}

-----------------------------
CURRENT USER QUERY
-----------------------------
User: {user_input}

Provide a structured response as per the mandatory format.
"""

    return final_prompt