import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env")

genai.configure(api_key=GOOGLE_API_KEY)

# ✅ use supported model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_weather(city: str):
    from dotenv import load_dotenv
    import os, requests

    load_dotenv()
    api_key = os.getenv("OPENWEATHER_KEY")
    if not api_key:
        raise ValueError("OPENWEATHER_KEY not set")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        # Provide clear error if city not found
        raise ValueError(f"OpenWeather API failed ({res.status_code}): {res.json().get('message', 'Unknown error')}")

    return res.json()

def get_advisory(query: str, crop: str | None, city: str | None, language: str = "English"):
    prompt = f"""
    You are an experienced agricultural advisor. 
    Always give realistic, clear, and practical advice to farmers.

    Context:
    - Crop: {crop or "Not specified"}
    - Farmer's Question: {query}

    Instructions:
    1. Answer in **{language}** only.
    2. If the farmer asks about a crop, provide real-world agronomy advice (planting, irrigation, fertilizers, diseases, harvesting).  
    3. If the crop is not mentioned, suggest general but useful advice about farming.  
    4. Keep tone supportive and easy to understand for rural farmers.  
    5. Answer in **2–3 short paragraphs**, not just one line.  
    """

    response = model.generate_content(prompt)
    return response.text.strip()