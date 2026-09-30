import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)

# Fast models first
MODELS = [
    "gemini-flash-lite-latest",
    "gemini-flash-latest",
]

def ask_gemini(prompt: str) -> str:
    last_error = None

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                print(f"Gemini response generated using {model}")
                return response.text

        except errors.APIError as e:
            last_error = e
            print(f"Gemini model {model} failed: {e}")

    raise RuntimeError(
        f"Gemini is temporarily unavailable. Last error: {last_error}"
    )


def generate_workout_gemini(name, age, weight, goal, intensity):

    prompt = f"""
You are FitBuddy, an AI fitness planning assistant.

Create a personalized 7-day fitness plan for:

Name: {name}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Workout intensity: {intensity}

Include:
- Day 1 to Day 7
- Warm-up
- Main exercises
- Sets and repetitions or duration
- Rest periods
- Cool-down
- One recovery suggestion

Make the plan practical, clear, and easy to follow.

Do not provide medical diagnosis or medical treatment.
"""

    return ask_gemini(prompt)