import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

filename = os.path.splitext(os.path.basename(__file__))[0]
if __name__ == "__main__" or __name__ == filename: # If the script is being run directly
    from Utilities import init_dotenv
else: # If the script is being imported
    from .Utilities import init_dotenv

# Load the OpenAI API key from the .env file and initialize the OpenAI client
init_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
chatGptClient = OpenAI()

# Function to call the OpenAI API
def call_openai(chatGptMessages):
    completion = chatGptClient.chat.completions.create(
        model="gpt-3.5-turbo",
        # model="gpt-4-turbo-preview",
        # model="gpt-4-0125-preview",
        messages=chatGptMessages
    )
    response = completion.choices[0].message.content
    return response

def call_openai_and_update_chat_messages(prompt, chat_messages):
    chat_messages.append({"role": "user", "content": prompt})
    response = call_openai(chat_messages)
    chat_messages.append({"role": "assistant", "content": response})
    return response

def call_openai_simple(prompt):
    chatGptMessages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    return call_openai_and_update_chat_messages(prompt, chatGptMessages)

def get_chatGptRules():
    chatGptRules = ["You are a helpful assistant.",
                     "You will be a role playing master"] # TODO: will update more rules later -mugdha
    return " ".join(chatGptRules)

def main():
    print("Welcome to the ChatBot!")
    chatGptMessages = [
        {"role": "system", "content": get_chatGptRules()}
    ]
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            response = call_openai_and_update_chat_messages(user_input, chatGptMessages)
            print("ChatGPT: ", response)

if __name__ == "__main__":
    main()