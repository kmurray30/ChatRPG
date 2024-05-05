import os
import webbrowser

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Read more at: https://platform.openai.com/docs/guides/images/usage
# Please read the costs here, of all the tools this one can be the most expensive, so stick to dalle3+standard and 1024x1024 for most calls: https://openai.com/api/pricing

print("Welcome to the Image Generator!")
while True:
        user_input = input("\nTell me what you would like to see (type 'exit' to quit):\n")
        if user_input.lower() == "exit":
            break
        if user_input:
          response = client.images.generate(
            model="dall-e-3", # options: dall-e-3, dall-e-2
            prompt=user_input,
            size="1024x1024", # options: 1024x1024, 1024x1792 or 1792x1024
            quality="standard", # options: standard, hd
            n=1,
          )

          image_url = response.data[0].url
          webbrowser.open(image_url)
