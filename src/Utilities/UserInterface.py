from tkinter import *

import ChatBot

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

chatGptMessages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

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

# # Create Welcome Title
# lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
# 	row=0)

# Create Main Chat Area
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

# Set chat window settings
txt.tag_config("You", foreground="white") # Set the user text color to white
txt.tag_config("ChatGPT", foreground="green") # Set the ChatGPT text color to green
txt.config(state=DISABLED) # Disable the chat window for typing

# Create a scrollbar
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

# Create the text input field
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

# Start the cursor in the input field
e.focus_set()

# Create a send button
send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send)
send_button.grid(row=2, column=1)

# Bind the Enter key to the send function
root.bind('<Return>', lambda event: send())

# Start the GUI
root.mainloop()
