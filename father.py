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

def extract_name_father_name(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Perform OCR to extract text from the preprocessed image
    extracted_text = pytesseract.image_to_string(preprocessed_image)
    
    # Find the line with the keyword "Name"
    lines = extracted_text.split('\n')
    keyword = "Name"
    name = None
    father_name = None
    for i, line in enumerate(lines):
        if keyword in line and i+1 < len(lines):
            # Extract the name from the next line
            name = lines[i+1].strip()
            
            # Check if the subsequent line contains the father's name
            if i+2 < len(lines):
                father_keyword = "Father's Name"
                if father_keyword in lines[i+2]:
                    father_name = lines[i+2].replace(father_keyword, "").strip()
            
            break
    
    return name, father_name

# Provide the path to the PAN card image
image_path = "pandhanesh.jpeg"  # Replace with the actual image path

# Extract the name and father's name from the PAN card image
name, father_name = extract_name_father_name(image_path)

# Print the extracted information
print("Name:", name)
print("Father's Name:", father_name)