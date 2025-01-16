import nltk
import re
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure necessary NLTK datasets are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Predefined responses
responses = {
    "greetings": ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! How can I assist you?"],
    "farewell": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "wellbeing": ["I'm doing great, thank you for asking!", "I'm doing well, thanks for asking! How about you?", "I'm good, how can I help?"],
    "help": ["I'm here to help you! What do you need assistance with?", "Sure, what can I assist you with?", "I'm ready to help! Ask me anything."],
    "about_me": ["I'm a chatbot designed to help you with various tasks. How can I assist you today?", "I'm here to answer your questions and help you with anything you need!"],
    "python": ["Python is a powerful programming language that is easy to learn and widely used in software development, data science, and machine learning.", 
               "Python is a high-level programming language known for its simplicity and versatility. It's used in web development, automation, data analysis, and more."],
    "default": ["I'm sorry, I don't understand that. Could you ask something else?"]
}

# Function to preprocess text (tokenization and stopword removal)
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_words = [word.lower() for word in word_tokens if word.lower() not in stop_words and word.isalnum()]
    return filtered_words

# Function to identify the type of user input
def identify_intent(user_input):
    user_input = user_input.lower()

    # Check for greetings
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good evening', 'greetings']
    if any(greet in user_input for greet in greetings):
        return "greetings"

    # Check for farewell
    farewells = ['bye', 'goodbye', 'see you', 'take care']
    if any(farewell in user_input for farewell in farewells):
        return "farewell"

    # Check for well-being inquiries
    wellbeing_keywords = ['how are you', 'how is it going', 'how do you do']
    if any(keyword in user_input for keyword in wellbeing_keywords):
        return "wellbeing"

    # Check for help inquiries
    help_keywords = ['help', 'assist', 'can you help']
    if any(keyword in user_input for keyword in help_keywords):
        return "help"

    # Check for information about the bot
    about_keywords = ['who are you', 'what are you', 'tell me about yourself']
    if any(keyword in user_input for keyword in about_keywords):
        return "about_me"

    # Check for questions about Python
    python_keywords = ['python', 'tell me about python', 'what is python']
    if any(keyword in user_input for keyword in python_keywords):
        return "python"
    
    # Default case for unrecognized input
    return "default"

# Function to generate a response based on identified intent
def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    return random.choice(responses["default"])

# Main chat function
def chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        # Exit the chat if user says 'bye'
        if user_input.lower() == "bye":
            print("Bot:", get_response("farewell"))
            break

        # Process the input to identify intent
        intent = identify_intent(user_input)
        response = get_response(intent)
        
        print("Bot:", response)

# Start the chatbot
if __name__ == "__main__":
    chat()
