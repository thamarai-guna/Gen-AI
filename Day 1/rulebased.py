from textwrap import indent


def input_validation(text):
    return text.strip().lower()
def intent_detection(text):
    if "price" in text:
        return "price"
    elif "hello" in text:
        return "greet"
    elif "bye" in text:
        return "exit"
    else:
        return "unknown"
def knowledge_base(text):
    data={
        "price": "product price is 999",
        "greet": "how cna i help you",
        "exit": "goodbye",
        "unknown": "i am sorry, i don't understand"
    }
    return data[text]
def ai_pprocessing(response):       #layer simulation
        return f" AI Module is response(response)"
def chatbot_response(user_input):
        step1= input_validation(user_input)
        step2= intent_detection(step1)
        step3= knowledge_base(step2)
        step4= ai_pprocessing(step3)
        return step4    
#chatloop
while True:
    user= input("you: ")
    bot= chatbot_response(user)
    print("bot:", bot)
    if "bye" in user.lower():
        break