def get_recovery_tip(goal):
    tips = {
        "Weight Loss": "Stay hydrated, prioritize balanced meals, and allow adequate recovery between demanding sessions.",
        "Muscle Gain": "Include protein-rich foods in balanced meals and prioritize adequate sleep and recovery.",
        "General Wellness": "Focus on balanced nutrition, hydration, regular movement, and consistent sleep.",
        "Flexibility": "Stay hydrated and combine mobility work with gentle recovery sessions.",
        "Endurance": "Pay attention to hydration, balanced meals, and sufficient recovery after longer sessions."
    }

    return tips.get(
        goal,
        "Stay hydrated, eat balanced meals, and give your body enough time to recover."
    )
