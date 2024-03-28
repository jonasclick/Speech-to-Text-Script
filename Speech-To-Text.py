from openai import OpenAI
from dotenv import load_dotenv, dotenv_values, set_key
import os


def use_whisper():
   if os.path.exists('audio.wav'):
        load_dotenv('.env')
        client = OpenAI()
        
        audio_file = open("audio.wav", "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
       )
        print(transcription.text)
   else:
       print("No audio file 'audio.wav' found. Please add your audio as 'audio.wav' into the directory and retry.")


env_values = dotenv_values('.env') # Load the values from the .env file into a dictionary
api_key = env_values.get('OPENAI_API_KEY') # Get the value corresponding to the specified key

# Check if the user has already setup his API Key in the .env
if api_key is not None:
    use_whisper()
else:
    user_input = input("Welcome to this script! Please enter your OpenAI API Key: ")
    set_key('.env', 'OPENAI_API_KEY', user_input) # Write or update the key-value pair in the .env file
    print('Thank you. The transcription will now be executed. Please stand by.')
    use_whisper()