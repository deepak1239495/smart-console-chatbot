# modules/intent_handler.py

def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["loan", "interest", "emi", "repay"]):
        return "loan"
    elif any(word in user_input for word in ["account", "balance", "statement", "deposit", "withdraw"]):
        return "banking"
    elif any(word in user_input for word in ["insurance", "claim", "premium", "policy"]):
        return "insurance"
    elif any(word in user_input for word in ["support", "help", "issue", "problem"]):
        return "support"
    else:
        return "general"
