# modules/response_generator.py

import random

FALLBACK_RESPONSES = [
    "Hmm... I’m not sure about that. Could you ask it differently?",
    "That's a great question, but I don't have the answer right now.",
    "Sorry, I didn’t get that. Maybe try rephrasing?",
    "I’ll try to learn about that soon. Anything else I can help with?"
]

def generate_response(user_input, answer):
    if "not sure" in answer or "couldn't find" in answer:
        return random.choice(FALLBACK_RESPONSES)
    
    friendly_prefixes = [
        "Here's what I found:",
        "Sure! Here's the info:",
        "Got it!",
        "Of course, here's the answer:"
    ]
    return f"{random.choice(friendly_prefixes)} {answer}"
