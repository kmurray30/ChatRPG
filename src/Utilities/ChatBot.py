import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

# Load the OpenAI API key from the .env file and initialize the OpenAI client
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
chatGptClient = OpenAI()
chatGptMessages = []

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

def call_openai_without_context(prompt, custom_system_context = "You are a helpful assistant."):
    chatGptMessages = [
        {"role": "system", "content": custom_system_context}
    ]
    return call_openai_and_update_chat_messages(prompt, chatGptMessages)

def get_default_rules():
    return [
        "You are a helpful assistant.",
        "You will be a role playing master"] # TODO: will update more rules later -mugdha

def call_openai_with_context(prompt, message_history, rules, debug = False):
    # Create the full context for the ChatGPT - this includes the rules, message history, and latest user prompt
    full_context_for_chatagent = [
        {"role": "system", "content": "".join(rules)}
    ]
    
    # Append the user prompt to the message history
    message_history.append({"role": "user", "content": prompt})
    
    # Append the message history to the full context
    full_context_for_chatagent += message_history

    # Call ChatGPT with the full context
    response = call_openai(full_context_for_chatagent)

    # Append the response to the message history
    message_history.append({"role": "assistant", "content": response})

    if (debug == True):
        print("DEBUG INFO: " + str(message_history))
    return response

def main():
    print("Welcome to the ChatBot!")
    message_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            response = call_openai_with_context(user_input, message_history, get_default_rules(), True)
            print("ChatGPT: ", response)

if __name__ == "__main__":
    main()