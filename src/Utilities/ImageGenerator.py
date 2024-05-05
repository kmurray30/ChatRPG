import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
import webbrowser

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def generate_image_url(prompt):
    response = client.images.generate(
        model="dall-e-3", # options: dall-e-3, dall-e-2
        prompt=prompt,
        size="1024x1024", # options: 1024x1024, 1024x1792 or 1792x1024
        quality="standard", # options: standard, hd
        n=1,
    )

    image_url = response.data[0].url
    return image_url

def main():
    print("Welcome to the Image Generator!")
    while True:
        user_input = input("\nTell me what you would like to see (type 'exit' to quit):\n")
        if user_input.lower() == "exit":
            break
        if user_input:
          image_url = generate_image_url(user_input)
          webbrowser.open(image_url)

if __name__ == "__main__":
    main()