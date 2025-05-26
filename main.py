import os
import datetime
from modules.intent_handler import detect_intent
from modules.match_engine import find_best_answer
from modules.response_generator import generate_response

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_message(user, message, bot_reply):
    with open("logs/chat_history.txt", "a") as log_file:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{time}] {user}: {message}\n")
        log_file.write(f"[{time}] ChatBot: {bot_reply}\n\n")

def main():
    print("🤖 ChatBot: Hello! Welcome to the Smart Console Chatbot.")
    name = input("🤖 ChatBot: May I know your name? \nYou: ")
    print(f"🤖 ChatBot: Nice to meet you, {name}! You can ask me anything about customer support, loan, education etc. (type 'exit' to quit)\n")

    while True:
        user_input = input(f"{name}: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 ChatBot: Thank you for chatting. Goodbye!")
            break

        # Step 1: Detect intent/domain
        domain = detect_intent(user_input)

        # Step 2: Find best matching answer
        answer = find_best_answer(user_input, domain)

        # Step 3: Generate final response
        final_response = generate_response(user_input, answer)

        # Display and log response
        print(f"🤖 ChatBot: {final_response}")
        log_message(name, user_input, final_response)

if __name__ == "__main__":
    main()
