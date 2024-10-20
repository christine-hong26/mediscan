import os
from flask import Flask, request, jsonify
from google.cloud import vision
from google.generativeai import GenerativeModel
from gtts import gTTS
import pygame

# Set up the environment for Google Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/fernandabarraza/Desktop/mediscan-439109-6622ef5bbc56.json" 

# Initialize the Generative AI model
model = GenerativeModel(model_name="gemini-pro")

# Configure the API key for Google Generative AI
model.configure(api_key="AIzaSyBaFUWQqp1qISn8pZOE2A06GUar5Bg8XAs")

app = Flask(__name__)

@app.route('/detect_text', methods=['POST'])
def detect_text_route():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image_file = request.files['image']
    image_path = os.path.join('/tmp', image_file.filename)
    image_file.save(image_path)

    detected_text = detect_text(image_path)
    return jsonify({"text": detected_text})

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

# Function to convert text to speech
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

    # Example image file for text detection
    medication_text = detect_text("/Users/fernandabarraza/Documents/images (1).jpeg")

    # Use the Generative AI model to generate content based on the detected text
    response = model.generate_content("After reading this text: " + medication_text + 
                                      " what medication is it and how many milligrams is it? "
                                      "If it doesn't include milligrams, specify if syrup, gummy, etc. "
                                      "Else don’t include.")

    geminiResponse = model.generate_content("After reading this text: " + medication_text + 
                                            " what medication is it and how many milligrams is it? "
                                            "Also give a brief description of its usages and any possible side effects. "
                                            "Please make sure to shorten the responses as much as possible so it is easy for "
                                            "someone who isn't knowledgeable to digest. "
                                            "Explain everything in a short, conversational paragraph as if you are talking to an elder.")

    # Output the generated response and convert it to speech
    print(geminiResponse.text)
    text_to_speech(geminiResponse.text)
