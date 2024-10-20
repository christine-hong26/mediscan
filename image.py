import requests
import google.generativeai as genai
import os
from google.cloud import vision
from gtts import gTTS
import pygame

model = genai.GenerativeModel(model_name="gemini-pro")

# Replace with your actual API key and the path to your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/myliv/.credentials/mediscan-439109-8223eeadd93a.json" 
os.environ["YOUR_API_KEY"] = "AIzaSyAcEenTGOFtOB_i3PVRIFjo_SVFxnXfMoc"

genai.configure(api_key=os.environ["YOUR_API_KEY"])

#Scanning image into text using Google Vision API
def detect_text(path):
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:  # Check if any text was detected
        extracted_text = " ".join(text.description for text in texts)
        return extracted_text
    else:
        return ""  # Return an empty string if no text is detected
    
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = "medical_report.mp3"
    tts.save(audio_file)
    
    # Initialize pygame mixer and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Wait for the music to finish
        pygame.time.Clock().tick(10)
    
if __name__ == "__main__":
    medication_text = detect_text("/Users/myliv/Pictures/simpleibu.png")

    geminiResponse = model.generate_content("After reading this text: " + medication_text + " what medication is it and how many miligrams is it? Also give a brief description of its usages and any possible side effects. Please make sure to shorten the responses as much as possible so it is easy for someone who isn't knowledgable to digest. Explain everything in a short, conversational paragraph as if you are talking to an elder.")

    print(geminiResponse.text)
    text_to_speech(geminiResponse.text)



