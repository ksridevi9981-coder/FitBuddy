from .gemini_generator import ask_gemini

def update_workout_plan(
    name,
    age,
    weight,
    goal,
    intensity,
    original_plan,
    feedback
):
    prompt = f"""
You are FitBuddy, an AI fitness planning assistant.

Update an existing 7-day workout plan based on user feedback.

User:
Name: {name}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Intensity: {intensity}

Original workout plan:
{original_plan}

User feedback:
{feedback}

Create a revised 7-day workout plan.

Apply the feedback where reasonable while preserving
the user's original fitness goal and preferred intensity.

Include:
- Warm-up
- Main workout
- Sets/repetitions or duration
- Rest/recovery
- Cooldown

Keep recommendations general and wellness-oriented.
Do not diagnose medical conditions or prescribe medical treatment.

Format clearly from Day 1 through Day 7.
"""
    return ask_gemini(prompt)
