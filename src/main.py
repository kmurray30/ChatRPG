import sys
import os
import concurrent.futures
import webbrowser

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utilities import ChatBot
from Utilities import ImageGenerator
from Utilities import TextToSpeech
chatGptMessages = [
        {"role": "system", "content": "You are a table top role playing game dungeon master."}
    ]

# Art styles
medieval_tavern = "medieval tavern"
realistic_office = "realistic office"
animated_show = "animated tv show"

# Function to summarize and speak the user input
def summarize_and_speak(prompt):
    summary = ChatBot.call_openai_simple("Please summarize this, and add some opinionated flavor onto it to make it longer. Refer to the user as the player: " + prompt)
    executor.submit(TextToSpeech.convert_play_delete_text_to_speech_file(summary, summary_as_filename=True, delete=False))

# Function to generate a speech file from the scene description
def generate_speech_file(scene_description):
    speech_file_path = TextToSpeech.create_file_path(scene_description, summary_as_filename=True, delete=False)
    TextToSpeech.convert_text_to_speech_file(scene_description, speech_file_path)
    return speech_file_path

initial_run = True
intro = "Welcome to the Chat RPG interface! Here, you can interact with an interactive fantasy world by simply typing out your actions. The game will dynamically generate images and audio in response to your input, enriching your experience. Let's begin by establishing an initial scene to set the stage for your adventure."
prompt = "Please set up an initial scene in a medieval tavern."
while(True):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # For the first iteration, introduce the game to the user via speech
        if initial_run:
            summary_future = executor.submit(TextToSpeech.convert_play_delete_text_to_speech_file, intro, summary_as_filename=False, delete=True)
            initial_run = False

        # Get GPT scene description (blocking)
        gtp_scene_description = ChatBot.call_openai_and_update_chat_messages(prompt, chatGptMessages)

        # Generate the image from the scene description (non-blocking)
        image_url_future = executor.submit(ImageGenerator.generate_image_url, f"Generate the following scene in the a {medieval_tavern} style: {gtp_scene_description}")

        # Generate the speech file from the scene description (non-blocking)
        speech_file_future = executor.submit(generate_speech_file, gtp_scene_description)

        # Generate the music for the scene
        # TODO: implement this

        # Wait for the summary speech, image gen, and speech gen (and music gen) to all finish
        concurrent.futures.wait([summary_future, speech_file_future, image_url_future])

        # Display the image and play the speech
        webbrowser.open(image_url_future.result())
        TextToSpeech.play_audio_file(speech_file_future.result())

        # Get user input
        prompt = input("What do you want to do next?\n")

        # Summarize and speak the user input (non-blocking)
        summary_future = executor.submit(summarize_and_speak, prompt)
