# Smart Console Chatbot

A smart, modular, rule-based chatbot that interacts with users via the terminal to answer queries related to general inquiries, customer support, loans, and education. The chatbot uses basic intent detection, best-match selection, and generates friendly responses with an interactive user experience. It also logs all interactions for future reference.

---

## 🚀 Features

- 🧠 Intent detection for categorizing user queries  
- 🔍 Matching engine to retrieve the best response from FAQ data  
- 💬 Human-like response generation  
- 🗂️ Modular codebase for easy maintenance and extension  
- 📝 Conversation history logging  
- ✅ Unit tests for core logic using Python’s `unittest`

---

## 📁 Folder Structure

```
smart-console-chatbot/
├── data/
│   └── faqs.json                  # FAQ database with predefined Q&A
├── logs/
│   └── chat_history.txt           # Logs of all chatbot conversations
├── modules/
│   ├── intent_handler.py          # Detects user query intent
│   ├── match_engine.py            # Finds best answer match
│   └── response_generator.py      # Builds chatbot responses
├── tests/
│   ├── test_intent_handler.py     # Unit tests for intent detection
│   ├── test_match_engine.py       # Unit tests for match engine
│   └── test_response_generator.py # Unit tests for response generator
├── main.py                        # Entry point for chatbot
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── LICENSE                        # MIT License
```

---

## 🛠️ Setup

### Requirements

Ensure you have **Python 3.7+** installed.

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## 💡 Usage Instructions

To run the chatbot in your console:

```bash
python main.py
```

### Sample Prompts

You can try asking:

- `"What are your working hours?"`
- `"How can I reset my password?"`
- `"How to apply for a loan?"`
- `"Tell me about scholarship options"`

The chatbot will detect the intent, retrieve the best-matching answer, and respond accordingly.

---

## 🧪 Running Unit Tests

To run all unit tests in the `tests/` folder:

```bash
python -m unittest discover tests
```

You should see a test summary with results of all modules.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 👨‍💻 Author

**Deepak Reddy**

---

## 📤 Uploading the Project to GitHub

### Step 1: Create Repository on GitHub

1. Go to [https://github.com](https://github.com)
2. Click **New Repository**
3. Name it `smart-console-chatbot`
4. Add optional description and initialize with a README if preferred
5. Click **Create Repository**

### Step 2: Push Local Code to GitHub

Open terminal in the project folder and run:

```bash
git init
git remote add origin https://github.com/deepak1239495/smart-console-chatbot.git
git add .
git commit -m "Initial commit - Smart console chatbot with modular architecture"
git branch -M main
git push -u origin main
```

---

## 📌 Future Improvements

- Add NLP-based intent classification using pretrained models  
- Deploy as a web or desktop app  
- Include voice input/output capability  
- Add conversation memory for context tracking  

---

Feel free to contribute, fork, or raise issues to improve this project!
