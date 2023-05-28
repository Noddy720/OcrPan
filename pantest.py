import pytesseract
from PIL import Image

def extract_pan_info(image_path):
    # Load the PAN card image
    image = Image.open(image_path)
    
    # Perform OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(image)
    
    # Extract PAN number
    pan_number = extracted_text[extracted_text.index("PAN") + 4:extracted_text.index("PAN") + 14]
    
    # Extract name
    start_index = extracted_text.index("Name") + 4
    end_index = extracted_text.index("Father") if "Father" in extracted_text else None
    name = extracted_text[start_index:end_index].strip()
    
    # Extract date of birth
    dob_index = extracted_text.index("DOB") if "DOB" in extracted_text else extracted_text.index("Date of Birth")
    dob = extracted_text[dob_index + 4:dob_index + 14]
    
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
