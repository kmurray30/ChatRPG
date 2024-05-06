from Utilities import ChatBot

def get_dungeon_master_rules():
    return [
        "You are a table top role playing game dungeon master.",
        "Craft an overall storyline for the session.",
        "Create a world for the players to explore.",
        "As the player interacts with the world, introduce the characters who live in this world. These characters can be friendly, neutral, or hostile. The player can interact with them in various ways. The player can also interact with objects in the world. When the player is interacting with other characters, pretend to be that character and have a conversation with the player",
        "The player can perform actions in the world. These actions can have consequences. You can decide what these consequences are.",
    ]

def main():
    print("Welcome to the ChatBot!")
    message_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            response = ChatBot.call_openai_with_context(user_input, message_history, get_dungeon_master_rules(), False)
            print("ChatGPT: ", response)

if __name__ == "__main__":
    main()