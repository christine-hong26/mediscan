import os
import hume

hume_api_key = "Az7bYQTLSRqBND3ZOGArnPvVySTx6jJRs14RGBqShhaoC6HY"
hume_client = hume.Client(api_key=hume_api_key)

def read_aloud(text):
    # Call the Hume AI Text-to-Speech API
    try:
        response = hume_client.text_to_speech(text=text, voice='en-US-Wavenet-D')  # Choose your preferred voice
        audio_data = response['audio_data']

        # Save the audio data to a file
        audio_file_path = 'output.mp3'
        with open(audio_file_path, 'wb') as audio_file:
            audio_file.write(audio_data)

        # Play the audio file
        os.system(f'start {audio_file_path}')  # For Windows
        # os.system(f'open {audio_file_path}')  # For macOS
        # os.system(f'aplay {audio_file_path}')  # For Linux

    except Exception as e:
        print(f"An error occurred while reading text aloud: {e}")

# Example response from Gemini AI
gemini_response = "Here are the details about ibuprofen: It's a common medication used to reduce fever, pain, and inflammation."

# Read the response aloud
read_aloud(gemini_response)