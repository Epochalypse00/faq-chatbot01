# bot.py

faq_data = {
    "hi": "Hello! How can I help you today?",
    "what is your name": "I’m a simple FAQ bot.",
    "how can i contact support": "You can contact support at support@example.com",
    "what is your return policy": "Our return policy allows returns within 30 days.",
    "bye": "Goodbye! Have a great day.",
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    return faq_data.get(user_input, "Sorry, I don’t understand that. Please ask something else.")

def main():
    print("Welcome to the FAQ Bot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

