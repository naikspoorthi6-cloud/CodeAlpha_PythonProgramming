# Task4_Chatbot

A basic rule-based chatbot built in Python as **Task 4** of the CodeAlpha Python Programming Internship.

## About the Project
PyBot replies to user messages using predefined rules. It matches what the user types against known phrases and returns a fixed reply, running in a loop until the user says "bye".

## Features
- Predefined replies for common phrases
- Case-insensitive and punctuation-tolerant matching
- Partial matching (e.g. "hey, how are you?" still works)
- Fallback message for unknown input
- `help` command lists what the bot understands

## Supported Inputs
| User says | Bot replies |
|-----------|-------------|
| hello | Hi! |
| hi | Hello there! |
| how are you | I'm fine, thanks! |
| what is your name | I'm PyBot, a simple chatbot. |
| help | Try: hello, how are you, what is your name, bye |
| bye | Goodbye! (chat ends) |

## Concepts Used
Dictionaries, functions, `while` loops, `if-elif` logic, string methods, input/output

## Requirements
- Python 3.8 or higher
- No external libraries needed

## How to Run
```bash
python chatbot.py
```

## Sample Conversation
```
PyBot: Hi! Type 'bye' to exit.
You: hello
PyBot: Hi!
You: how are you
PyBot: I'm fine, thanks!
You: bye
PyBot: Goodbye!
```

## How It Works
1. `get_response()` cleans the message (lowercase, trims spaces and trailing punctuation).
2. It checks for an exact match, then for a known phrase inside the message.
3. If nothing matches, it returns a fallback reply.
4. `main()` loops until the user types "bye".

## Project Structure
```
Task4_Chatbot/
├── chatbot.py
└── README.md
```

## Possible Improvements
- Add more responses (time, date, jokes)
- Load replies from a JSON file
- Build a GUI with Tkinter

## Author
Spoorthi M Naik, CodeAlpha Python Programming Intern
