# Speech-to-Text-Script

This simple script converts spoken text into written text using OpenAI's Whisper model.

## Requirements  

1. **OpenAI Plus Account:** To use this script, you need an OpenAI Plus account, which costs $20 per month.
2. **Available Balance:** Ensure you have a sufficient balance in your OpenAI Plus account. You can check your balance [here](https://platform.openai.com/account/billing/overview).
   - Your OpenAI Plus account operates similarly to a phone plan with both a monthly subscription and a prepaid balance. Make sure you have funds in your prepaid balance.

## How to Use  

1. **API Key:** Generate a personal API key for yourself [here](https://platform.openai.com/api-keys). Do not share this key with anyone.
2. **Download the Script:** Download the script to your local machine.
3. **Install Dependencies:** Make sure you have the following dependencies installed:

```bash
pip install python-dotenv
pip install --upgrade openai
```

4. **Prepare Audio File:** Place the audio file you want to transcribe in the same folder as the script. Rename it to 'audio.wav'.
5. **Run the Script:** Execute the script. On first execution you will be asked to provide your API Key. Your key will then be stored in an .env file locally in the same folder as the script. Your key will not be shared. Do not share your key.
