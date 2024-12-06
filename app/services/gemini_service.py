import os 
import google.generativeai as genai
from app.core.config import settings
import re

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-') # Selected a free model

def gemini_response(text, token_limit=1000, page_size=500):
    # Eliminate the markdowns from the text
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove markdown links
    text = re.sub(r'[#\*`]', '', text)  # Remove markdown symbols

    # Ensure there is a limit for the input tokens
    if len(text) > token_limit:
        text = text[:token_limit]

    # Generate content
    response = model.generate_content(text)

    # Implement pagination for the output
    output = response.text
    pages = [output[i:i + page_size] for i in range(0, len(output), page_size)]

    return pages