import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Read more at: https://platform.openai.com/docs/quickstart

# Load the OpenAI API key from the .env file and initialize the OpenAI client
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
chatGptClient = OpenAI()

# Initialize the chat messages
chatGptMessages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Function to call the OpenAI API
def call_openai(prompt):
    chatGptMessages.append({"role": "user", "content": prompt})
    completion = chatGptClient.chat.completions.create(
        model="gpt-3.5-turbo",
        # model="gpt-4-turbo-preview",
        # model="gpt-4-0125-preview",
        messages=chatGptMessages
    )
    response = completion.choices[0].message.content
    chatGptMessages.append({"role": "assistant", "content": response})
    return response

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            response = call_openai(user_input)
            print("ChatGPT: ", response)

if __name__ == "__main__":
    main()