# backend/groq_client.py

import os
from groq import Groq
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger()


class GroqClient:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        model_name = os.getenv(
            "MODEL_NAME",
            "llama-3.3-70b-versatile"
        )

        if not api_key:

            logger.error("GROQ_API_KEY not found")

            raise ValueError(
                "GROQ_API_KEY not found in environment variables"
            )

        self.client = Groq(api_key=api_key)

        self.model = model_name

        logger.info(
            f"Groq model initialized: {model_name}"
        )



    def generate_response(self, prompt: str) -> str:

        try:

            logger.info("Sending request to Groq API")

            chat_completion = self.client.chat.completions.create(

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

                model=self.model,

                temperature=0.7,

                max_tokens=800,

            )


            response = chat_completion.choices[0].message.content


            logger.info("Response received from Groq")


            return response


        except Exception as e:

            logger.error(f"Groq API error: {str(e)}")

            return (
                "An internal error occurred while generating your career advice. "
                "Please try again later."
            )