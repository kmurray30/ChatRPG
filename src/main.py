import sys
import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utilities import ChatBot
from Utilities import ImageGenerator
from Utilities import TextToSpeech
chatGptMessages = [
        {"role": "system", "content": "You are a DnD dungeon master."}
    ]

prompt = "Please set up an initial scene in a tavern"
while(True):
    gtp_scene_description = ChatBot.call_openai_and_update_chat_messages(prompt, chatGptMessages)

    ImageGenerator.generate_and_display_image(gtp_scene_description)

    TextToSpeech.convert_play_delete_text_to_speech_file(gtp_scene_description, summary_as_filename=True, delete=False)

    prompt = input("What do you want to do next?\n")
    summary = ChatBot.call_openai_simple("Please summarize this (elaborate if short, shorten if long: " + prompt)
    TextToSpeech.convert_play_delete_text_to_speech_file(summary, summary_as_filename=True, delete=False)

# TODO: loading dots, parallel calls, better summary of user action, open not in browser, output the text, consistent images, more images per round, UI
# Feedback: It does too much (will continue scene too far each round), it takes everything the user says as gospel