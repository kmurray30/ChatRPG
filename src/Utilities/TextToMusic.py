import requests
import json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

API_ENDPOINT = "http://localhost:3000/" # Set Suno API Endpoint. Setup instructions: https://suno.gcui.art/

def generate_music(prompt, isInstrumental=False):
    payload = {'prompt': prompt, 'make_instrumental': 'true', 'wait_audio': 'true'}
    r = requests.post(API_ENDPOINT + "api/generate", data=json.dumps(payload))
    print(r.status_code, r.reason)
    print(r.text)

    if (r.status_code == 200):
        # Get the id of the generated music
        id = r.json()['id']
        get_music(id)

def get_music(id):
    r = requests.get(API_ENDPOINT + "api/get?ids=" + id)
    print(r.status_code, r.reason)
    print(r.text)
