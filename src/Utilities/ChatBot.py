import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

# Load the OpenAI API key from the .env file and initialize the OpenAI client
load_dotenv()
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

def main():
    print("Welcome to the ChatBot!")
    chatGptMessages = [
        {"role": "system", "content": "You are a helpful assistant."}
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