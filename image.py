import requests
import google.generativeai as genai
import os
from google.cloud import vision
model = genai.GenerativeModel(model_name="gemini-pro")

# Replace with your actual API key and the path to your service account key
os.environ["GOOGLE_APPLICATION_CRE"] = "/Users/fernandabarraza/Desktop/mediscan-439109-6622ef5bbc56.json" 
os.environ["YOUR_API_KEY"] = "AIzaSyBaFUWQqp1qISn8pZOE2A06GUar5Bg8XAs"

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
    
if __name__ == "__main__":
    medication_text = detect_text("/Users/fernandabarraza/Documents/images (1).jpeg")

    response = model.generate_content("After reading this text: " + medication_text + " what medication is it and how many miligrams is it? If it doesn't include miligrams, specify if syrup, gummy, etc. Else dont include.")

    print(response.text)


