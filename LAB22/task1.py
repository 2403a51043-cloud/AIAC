
def get_response(language, message):
    responses = {
        "en": {
            "hi": "Hello! 👋 How can I help you today?",
            "problem": "Please describe your problem, and I’ll try to assist you.",
            "thanks": "You’re welcome! Have a nice day!",
            "default": "I'm sorry, I didn't understand. Could you repeat that?"
        },
        "hi": {
            "hi": "नमस्ते! 👋 मैं आपकी कैसे मदद कर सकता हूँ?",
            "problem": "कृपया अपनी समस्या बताइए, मैं मदद करने की कोशिश करूँगा।",
            "thanks": "आपका स्वागत है! आपका दिन शुभ हो!",
            "default": "माफ़ कीजिए, मैं समझ नहीं पाया। कृपया दोहराएँ।"
        },
        "es": {
            "hi": "¡Hola! 👋 ¿En qué puedo ayudarte hoy?",
            "problem": "Por favor, describe tu problema y trataré de ayudarte.",
            "thanks": "¡De nada! ¡Que tengas un buen día!",
            "default": "Lo siento, no entendí. ¿Puedes repetirlo?"
        }
    }

    lang_responses = responses.get(language, responses["en"])
    message = message.lower()

    if "hi" in message or "hello" in message or "hola" in message or "नमस्ते" in message:
        return lang_responses["hi"]
    elif "problem" in message or "issue" in message or "समस्या" in message:
        return lang_responses["problem"]
    elif "thank" in message or "thanks" in message or "धन्यवाद" in message:
        return lang_responses["thanks"]
    else:
        return lang_responses["default"]


# -------------------------------
# Main Chatbot Interaction
# -------------------------------
print("🤖 Welcome to the AI Customer Support Chatbot!")
print("Languages supported: English (en), Hindi (hi), Spanish (es)")
language = input("Please choose your language (en / hi / es): ").strip().lower()

if language not in ["en", "hi", "es"]:
    print("Language not recognized. Defaulting to English.\n")
    language = "en"

print("\nChatbot is ready! Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: 👋 Goodbye! Have a nice day!")
        break
    response = get_response(language, user_input)
    print("Bot:", response)
