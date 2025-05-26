# modules/match_engine.py

import json
import difflib

def load_faqs(domain):
    try:
        with open("data/faqs.json", "r") as file:
            data = json.load(file)
        return data.get(domain, [])
    except FileNotFoundError:
        return []

def find_best_answer(user_input, domain):
    faqs = load_faqs(domain)
    if not faqs:
        return "I'm sorry, I couldn't find anything related to your question."

    questions = [item["question"] for item in faqs]
    matches = difflib.get_close_matches(user_input.lower(), questions, n=1, cutoff=0.4)

    if matches:
        for item in faqs:
            if item["question"] == matches[0]:
                return item["answer"]
    return "I'm not sure about that. Could you rephrase your question?"
