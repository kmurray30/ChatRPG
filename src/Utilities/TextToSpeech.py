import os
from pathlib import Path

import openai
from dotenv import load_dotenv
from openai import OpenAI

from ChatBot import call_openai_simple

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

from playsound import playsound

def play_audio_file(file_path):
    playsound(file_path)

def delete_audio_file(file_path):
    # only delete audio files in the audio directory
    if os.path.exists(file_path) and "/audio/" in file_path and Path(file_path).suffix == ".mp3":
        os.remove(file_path)
    else:
        print("The file does not exist")

def convert_text_to_speech_file(prompt, file_path):
    with (client.audio.speech.with_streaming_response.create(
      model="tts-1",
      voice="alloy",
      input=prompt
    )) as response:
        response.stream_to_file(file_path)

def main():
    print("Welcome to the Text to Speech Converter!")
    while True:
        user_input = input("\nEnter the text you would like to convert to speech (type 'exit' to quit):\n")
        if user_input.lower() == "exit":
            break
        if user_input:
            # Generate a file name based on the user input
            summary = call_openai_simple("Summarize the following into 1-4 words (and no special characters): " + user_input).rstrip('.')
            speech_file_name = f"{summary}.mp3"
            speech_file_path = "../../audio/temp/" + speech_file_name

            # Generate the speech file
            convert_text_to_speech_file(user_input, speech_file_path)

            # Play the speech file
            play_audio_file(speech_file_path)

            # Delete the speech file
            delete_audio_file(speech_file_path)

if __name__ == "__main__":
    main()