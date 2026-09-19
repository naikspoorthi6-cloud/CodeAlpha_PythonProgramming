"""Task 4: Basic Rule-Based Chatbot - CodeAlpha Python Internship"""

RESPONSES = {
    "hello": "Hi!",
    "hi": "Hello there!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I'm PyBot, a simple chatbot.",
    "help": "Try: hello, how are you, what is your name, bye",
    "bye": "Goodbye!",
}


def get_response(message):
    message = message.lower().strip().rstrip("?!.")
    if message in RESPONSES:
        return RESPONSES[message]
    for key, reply in RESPONSES.items():
        if key in message:
            return reply
    return "Sorry, I didn't understand that. Type 'help' for options."


def main():
    print("PyBot: Hi! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print(f"PyBot: {reply}")
        if "bye" in user.lower():
            break


if __name__ == "__main__":
    main()
