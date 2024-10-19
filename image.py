import requests
import google.generativeai as genai
import os
from google.cloud import vision
import hume
from hume import HumeClient
import httpx
import base64
from websocket import create_connection

# Read keys from environment variables
HUME_API_KEY = os.getenv('HUME_API_KEY')
HUME_SECRET_KEY = os.getenv('HUME_SECRET_KEY')

print(f"HUME_API_KEY: {HUME_API_KEY}")
print(f"HUME_SECRET_KEY: {HUME_SECRET_KEY}")

# Generate the Basic Auth header
auth = f"{HUME_API_KEY}:{HUME_SECRET_KEY}"
encoded_auth = base64.b64encode(auth.encode()).decode()
print(f"Encoded Auth: {encoded_auth}")

# Request access token
resp = httpx.post(
    url="https://api.hume.ai/oauth2-cc/token",
    headers={"Authorization": f"Basic {encoded_auth}"},
    data={"grant_type": "client_credentials"},
)

# Request access token
resp = httpx.post(
    url="https://api.hume.ai/oauth2-cc/token",
    headers={"Authorization": f"Basic {encoded_auth}"},
    data={"grant_type": "client_credentials"},
)

# Check if the request was successful
if resp.status_code == 200:
    access_token = resp.json().get('access_token')
    if access_token is None:
        print("Access token not found in response.")
else:
    print(f"Error fetching access token: {resp.status_code} - {resp.text}")

# Use access_token in your Hume API requests

model = genai.GenerativeModel(model_name="gemini-pro")

# Replace with your actual API key and the path to your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/myliv/.credentials/mediscan-439109-8223eeadd93a.json" 
os.environ["YOUR_API_KEY"] = "AIzaSyAcEenTGOFtOB_i3PVRIFjo_SVFxnXfMoc"

genai.configure(api_key=os.environ["YOUR_API_KEY"])

hume_api_key = "Az7bYQTLSRqBND3ZOGArnPvVySTx6jJRs14RGBqShhaoC6HY"
# Initialize Hume API directly with API key (no access token request)
hume_client = HumeClient(api_key=HUME_API_KEY)



class HumeAPI:
    def __init__(self, access_token, base_url):
        self.hume_client = hume_client

    def send_message(self, message_data):
        url = f"{self.base_url}/messages"  # Ensure this URL is correct for your use case
        headers = {
            "Authorization": f"Bearer {self.hume_client.api_key}",  # Use the API key directly
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=message_data, headers=headers)
        return response.json()
    hume_api = HumeAPI(hume_client=hume_client, base_url="https://api.hume.ai/v0/evi/tools")


class ChatSession:
    def __init__(self):
        self.session_id = None

    def start_new_session(self):
        self.session_id = "unique_session_id"  # Replace with actual session ID generation

def start_conversation():
    # Send the welcome message at the start
    welcome_message = {
        "text": "Welcome! I will now process your medication details.",
        "session_id": current_session_id
    }

def start_conversation(current_session_id, gemini_response):
    # Step 1: Send the welcome message
    welcome_message = {
        "text": "Welcome! I will now process your medication details.",
        "session_id": current_session_id
    }
    
    try:
        response = hume_api.send_message(welcome_message)
        print("Welcome Message Response:", response)  # Log the welcome message response
    except Exception as e:
        print(f"Error sending welcome message: {e}")

    # Step 2: Send the dynamic response with the patient's medical report
    dynamic_response = {
        "text": gemini_response.text,
        "session_id": current_session_id
    }

    try:
        response = hume_api.send_message(dynamic_response)
        print("Dynamic Response:", response)  # Log the dynamic response
    except Exception as e:
        print(f"Error sending dynamic response: {e}")


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
    medication_text = detect_text("/Users/myliv/Pictures/simpleibu.png")

    geminiResponse = model.generate_content("After reading this text: " + medication_text + " what medication is it and how many miligrams is it? Also give a brief description of its usages and any possible side effects. Please make sure to shorten the responses as much as possible so it is easy for someone who isn't knowledgable to digest. Explain everything in a short, conversational paragraph as if you are talking to an elder.")

    print(geminiResponse.text)

    # Event messages configuration
    event_messages_config = {
        "on_new_chat": {
            "enabled": True,
            "text": f"Here are the details of your medication: {geminiResponse.text}"
        }
    }

    # Initialize Hume API directly with API key
    hume_client = HumeClient(api_key=HUME_API_KEY)
    hume_api = HumeAPI(hume_client=hume_client, base_url="https://api.hume.ai/v0/evi/tools")
    chat_session = ChatSession()
    chat_session.start_new_session()
    current_session_id = chat_session.session_id

    # Start the conversation with the welcome message and dynamic report
    start_conversation(current_session_id, geminiResponse)


