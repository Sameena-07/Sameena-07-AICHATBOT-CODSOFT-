from datetime import datetime

print("===================================")
print(" Welcome to Sameena's Simple ChatBot ")
print("===================================")
while True:

    user_input = input("\nYou: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("ChatBot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("ChatBot: I am doing well. Thank you for asking.")

    elif user_input == "what is your name":
        print("ChatBot: My name is Simple ChatBot.")

    elif user_input == "what language are you written in":
        print("ChatBot: I am written in Python.")

    elif user_input == "what is your purpose":
        print("ChatBot: My purpose is to answer questions and provide information.")

    elif user_input == "how can you help me":
        print("ChatBot: I can answer simple questions and provide basic information.")

    elif user_input == "what can you do":
        print("ChatBot: I can answer questions related to technology and general topics.")

    elif user_input == "can you help me":
        print("ChatBot: Yes, I will try my best to help you.")

    elif user_input == "what is the time":
        print("ChatBot:", datetime.now().strftime("%I:%M %p"))

    elif user_input == "what is the date":
        print("ChatBot:", datetime.now().strftime("%d-%m-%Y"))

    elif user_input == "how is the weather":
        print("ChatBot: Sorry, I cannot access live weather information.")

    elif user_input == "help":
        print("ChatBot: You can ask me about AI, Python, Programming, or Computer Science.")

    elif user_input == "what is ai":
        print("ChatBot: AI stands for Artificial Intelligence.")

    elif user_input == "what is machine learning":
        print("ChatBot: Machine Learning is a branch of AI that helps computers learn from data.")

    elif user_input == "what is python":
        print("ChatBot: Python is a popular programming language used for many applications.")

    elif user_input == "what is programming":
        print("ChatBot: Programming is the process of writing instructions for a computer.")

    elif user_input == "what is computer science":
        print("ChatBot: Computer Science is the study of computers, software, and algorithms.")

    elif user_input == "what is a chatbot":
        print("ChatBot: A chatbot is a program that can interact with users through conversation.")

    elif user_input == "what is nlp":
        print("ChatBot: NLP stands for Natural Language Processing.")

    elif user_input == "what is data science":
        print("ChatBot: Data Science is the field of analyzing and interpreting data.")

    elif user_input == "what is cyber security":
        print("ChatBot: Cyber Security is the practice of protecting systems and data from attacks.")

    elif user_input == "what is cloud computing":
        print("ChatBot: Cloud Computing provides computing services over the internet.")

    elif user_input == "what is an algorithm":
        print("ChatBot: An algorithm is a step-by-step procedure used to solve a problem.")

    elif user_input == "what is software development":
        print("ChatBot: Software Development is the process of designing and building software applications.")

    elif user_input == "thank you":
        print("ChatBot: You are welcome.")

    elif user_input == "thanks":
        print("ChatBot: Happy to help.")

    elif user_input == "nice to meet you":
        print("ChatBot: Nice to meet you too.")

    elif user_input == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I do not understand that question.")
    