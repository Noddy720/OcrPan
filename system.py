import json
import os
from pan_utils import extract_aadhar_info

# Set the path to the directory containing the Aadhar card images
image_dir = "imagespan"

# Create an empty list to store the extracted information for each image
pan_info_list = []

# Loop over all the image files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Build the path to the image file
        image_path = os.path.join(image_dir, filename)
        
        # Extract the information from the image
        aadhar_info = extract_aadhar_info(image_path)
        
        # Append the extracted information to the list
        pan_info_list.append(aadhar_info)

# Write the list of dictionaries to a JSON file
with open("aadhar_info.json", "w") as f:
    json.dump(pan_info_list, f, indent=4)