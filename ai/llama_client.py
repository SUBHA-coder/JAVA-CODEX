# ai/llama_client.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Correctly initialize Groq client with just the API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llama(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Java DSA teacher. Explain Java code clearly."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
        )

        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
        return full_response

    except Exception as e:
        return f"Error explaining code: {str(e)}"
