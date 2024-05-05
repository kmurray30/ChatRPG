import json
import time

import requests

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

API_ENDPOINT = "http://localhost:3000/" # Set Suno API Endpoint. Setup instructions: https://suno.gcui.art/

def generate_music(prompt, isInstrumental=True):
    payload = {'prompt': prompt, 'make_instrumental': 'true', 'wait_audio': 'true'}
    r = requests.post(API_ENDPOINT + "api/generate", data=json.dumps(payload))
    print(r.status_code, r.reason)
    print(r.text)

    if (r.status_code == 200):
        # Get the id of the generated music
        id = r.json()['id']
        get_music(id)
        return id
    else:
        print("Failed to generate music, status code: ", r.status_code)

def get_music(id):
    r = requests.get(API_ENDPOINT + "api/get?ids=" + id)
    print(r.status_code, r.reason)
    print(r.text)

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if user_input:
            includeVocals = "with vocals" in user_input or "include vocals" in user_input
            instrumentalOnly = not includeVocals
            id = generate_music(user_input, instrumentalOnly)
            # Try to get the music every 2 seconds
            while True:
                get_music(id)
                time.sleep(2)

if __name__ == "__main__":
    main()