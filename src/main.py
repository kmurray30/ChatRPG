import sys
import os
import concurrent.futures
import webbrowser

filename = os.path.splitext(os.path.basename(__file__))[0]
if __name__ == "__main__" or __name__ == filename: # If the script is being run directly
    from Utilities.Utilities import get_path_from_project_root
else: # If the script is being imported
    from .Utilities.Utilities import get_path_from_project_root

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
    summary = ChatBot.call_openai_without_context("Summarize this, but make it a bit longer (convert first person to second person and second person to third person): " + prompt)
    executor.submit(TextToSpeech.convert_play_delete_text_to_speech_file(summary, summary_as_filename=True, delete=False))

# Function to generate a speech file from the scene description
def generate_speech_file(scene_description):
    speech_file_path = TextToSpeech.create_file_path(scene_description, summary_as_filename=True, delete=False)
    TextToSpeech.convert_text_to_speech_file(scene_description, speech_file_path)
    return speech_file_path

initial_run = True
intro = "Welcome to the epic adventure that awaits you in Chat RPG. From mystical forests to ancient, bustling cities, explore an infinitely unfolding world shaped by your actions and decisions. With deep and complex NPCs, beautifully generated art, and epic narration, an exciting journey awaits you, if you are ready. Your adventure begins in an unassuming tavern."
prompt = "Please set up an initial scene in a medieval tavern."

title_screen_path = get_path_from_project_root("assets/title_screen.png")
webbrowser.open(f"file:///{title_screen_path}")
while(True):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # For the first iteration, introduce the game to the user via speech
        if initial_run:
            summary_future = executor.submit(TextToSpeech.convert_play_delete_text_to_speech_file, intro, summary_as_filename=False, delete=True)
            initial_run = False

        # Get GPT scene description (blocking)
        gtp_scene_description = ChatBot.call_openai_and_update_chat_messages(prompt, chatGptMessages)

        # Generate the image from the scene description (non-blocking)
        image_url_future = executor.submit(ImageGenerator.generate_image_url, f"Generate the following scene in the a {medieval_tavern} style, making sure to include a character that looks like aragorn from TLOTR, and don't include any text: {gtp_scene_description}")

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
