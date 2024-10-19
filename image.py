import requests

#Scanning image into text using Google Vision API
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

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

def get_drug_info(drug_name):
    api_url = "https://api.gemini.example.com/drug"  # Replace with actual API endpoint
    params = {
        "name": drug_name
    }
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"  # Include your API key if required
    }
    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()  # Parse the JSON response
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

