from tkinter import *
from tkinter import PhotoImage, Label
import os

from PIL import Image, ImageTk

import ChatBot

filename = os.path.splitext(os.path.basename(__file__))[0]
if __name__ == "__main__" or __name__ == filename: # If the script is being run directly
    from Utilities import get_path_from_project_root
else: # If the script is being imported
    from .Utilities import get_path_from_project_root

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_BLACK = "#000000"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

chatGptMessages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

def create_image_widget(root, file_path):
    # Open the image file
    img = Image.open(file_path)

    # Create a PhotoImage object from the image
    photo = ImageTk.PhotoImage(img)

    # Create a Label widget to display the image
    image_widget = Label(root, image=photo)

    # Keep a reference to the image object to prevent it from being garbage collected
    image_widget.image = photo

    # Keep a reference to the original image to allow resizing
    image_widget.original = img

    return image_widget

def add_text_to_chat_window(text, role):
    txt.config(state=NORMAL)
    txt.insert(END, role + " -> " + text + "\n", role)
    txt.config(state=DISABLED)

def call_chatgpt(user):
    # Call ChatGPT
	response = ChatBot.call_openai_and_update_chat_messages(user, chatGptMessages)
	
    # Display the response, color this text green
	add_text_to_chat_window(response, "ChatGPT")

	e.delete(0, END)
	
# Send function
def send():
	send = "" + e.get()
	
    # Display the user input
	add_text_to_chat_window(send, "You")

	user = e.get().lower()
	e.delete(0, END) # Clear the input field
	
    # Call ChatGPT in a future thread
	root.after(100, call_chatgpt, user)

def enforce_aspect_ratio(event):
    new_height = root.winfo_height() - 10
    new_width = new_height

    # Resize the original image while maintaining its aspect ratio
    img = image_widget.original.copy()
    img.thumbnail((new_width, new_height))

    # Create a PhotoImage object from the resized image
    photo = ImageTk.PhotoImage(img)

    # Update the image displayed by the Label widget
    image_widget.config(image=photo)
    image_widget.image = photo  # Keep a reference to the image object to prevent it from being garbage collected

# Root config
root.grid_rowconfigure(0, weight=1)  # Allocate extra space to row 0
root.grid_columnconfigure(0, weight=1)  # Allocate extra space to column 0
root.grid_columnconfigure(1, weight=1)  # Allocate extra space to column 1
root.minsize(500, 500)
root.config(bg=BG_BLACK)
root.attributes('-fullscreen', True)

# Create a Frame
chat_frame = Frame(root)
chat_frame.grid(row=0, column=0, sticky='NWSE', columnspan=1, rowspan=1)  # Add the Frame to the root window and make it stick to the left
chat_frame.grid_rowconfigure(0, weight=1)  # Allocate extra space to row 0
chat_frame.grid_columnconfigure(0, weight=1)  # Allocate extra space to column 0

# Create image widget
title_screen_path = get_path_from_project_root("assets/title_screen.png")
image_widget = create_image_widget(root, title_screen_path)
image_widget.grid(row=0, column=1, sticky="W")

# Create Main Chat Area
txt = Text(chat_frame, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=0, column=0, columnspan=2, sticky='NSWE')

# Set chat window settings
txt.tag_config("You", foreground="white") # Set the user text color to white
txt.tag_config("ChatGPT", foreground="green") # Set the ChatGPT text color to green
txt.config(state=DISABLED) # Disable the chat window for typing

# Create a scrollbar
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

# Create the text input field
e = Entry(chat_frame, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
e.grid(row=1, column=0, columnspan=1, sticky='WSE', padx=0)

# Start the cursor in the input field
e.focus_set()

# Create a send button
send_button = Button(chat_frame, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send)
send_button.grid(row=1, column=1, sticky='WS', padx=0)

# Bind the Enter key to the send function
root.bind('<Return>', lambda event: send())
# Bind the function to the <Configure> event
root.bind('<Configure>', enforce_aspect_ratio)

# Start the GUI
root.mainloop()

