from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Chess is a board game for two players, each controlling a set of chess pieces, with the objective to checkmate the opponent's king, i.e. threaten it with inescapable capture"
)

response.stream_to_file(speech_file_path)