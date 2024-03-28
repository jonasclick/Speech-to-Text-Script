from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')

client = OpenAI()

audio_file= open("audio.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)