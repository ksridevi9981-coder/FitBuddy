from .gemini_generator import ask_gemini


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
You are FitBuddy, an AI fitness assistant.

Give a concise nutrition and recovery tip for this fitness goal:

Goal: {goal}

Include:
- Suitable food choices
- Hydration
- Recovery or sleep advice

Keep it practical and easy to understand.

Do not provide medical diagnosis or treatment.
"""

    return ask_gemini(prompt)