import cv2
import pytesseract

def preprocess_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to enhance the text
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Apply image denoising
    denoised = cv2.fastNlMeansDenoising(thresholded, h=10)
    
    return denoised

def extract_pan_info(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Perform OCR to extract text from the preprocessed image
    extracted_text = pytesseract.image_to_string(preprocessed_image)
    
    # Extract PAN number
    pan_number = None
    if "PAN" in extracted_text:
        pan_index = extracted_text.index("PAN") + 4
        pan_number = extracted_text[pan_index:pan_index + 10]
    
    # Extract name
    name = None
    if "Name" in extracted_text:
        name_index = extracted_text.index("Name") + 4
        name_end_index = extracted_text.find("\n", name_index)
        name = extracted_text[name_index:name_end_index].strip()
    
    # Extract date of birth
    dob = None
    if "DOB" in extracted_text:
        dob_index = extracted_text.index("DOB") + 4
        dob = extracted_text[dob_index:dob_index + 10]
    
    return {
        "PAN Number": pan_number,
        "Name": name,
        "Date of Birth": dob
    }

# Provide the path to the PAN card image
image_path = "pan1.jpg"  # Replace with the actual image path

# Extract information from the PAN card image
pan_info = extract_pan_info(image_path)

# Print the extracted information
print("PAN Number:", pan_info["PAN Number"])
print("Name:", pan_info["Name"])
print("Date of Birth:", pan_info["Date of Birth"])