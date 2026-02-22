from google import genai
import config
from prompts.bioinfo_prompt import SYSTEM_PROMPT
from utils.logger import logger

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(chat_history):
    try:
        full_prompt = SYSTEM_PROMPT + "\n\n"

        for message in chat_history:
            full_prompt += f"{message['role']}: {message['content']}\n"

        response = client.models.generate_content(
            model="models/gemini-3-flash-preview",
            contents=full_prompt,
        )

        logger.info("Gemini API call successful")

        return response.text

    except Exception as e:
        logger.error(f"Gemini API Error: {str(e)}")
        return f"⚠️ Gemini Error: {str(e)}"
