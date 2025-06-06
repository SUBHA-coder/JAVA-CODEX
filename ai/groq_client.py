# ai/gemini_client.py

import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([
            {"text": "You are an expert Java teacher. Explain Java DSA code clearly."},
            {"text": prompt}
        ])
        return response.text
    except Exception as e:
        return f"Error explaining code: {str(e)}"
