# # this is where we'll scan the images
# import pytesseract
# from PIL import Image

# def extract_text_from_image(image_path):
#     # Open the image file
#     img = Image.open(image_path)
    
#     # Use pytesseract to extract text
#     extracted_text = pytesseract.image_to_string(img)
    
#     # Return the extracted text
#     return extracted_text

# if __name__ == "__main__":
#     text = extract_text_from_image("/Users/fernandabarraza/Documents/labels_01.jpg")
#     print("Extracted Text: ", text)

import cv2
import pytesseract

def preprocess_and_extract_text(image_path):
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize the image for better recognition
    # resized_img = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    
    # Apply GaussianBlur to reduce noise
    blurred_img = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply thresholding to get a binary image
    thresh_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # Use Tesseract to extract text from the preprocessed image
    extracted_text = pytesseract.image_to_string(thresh_img)
    
    return extracted_text

if __name__ == "__main__":
     text = preprocess_and_extract_text("/Users/fernandabarraza/Documents/labels_01.jpg")
     print("Extracted Text: ", text)

