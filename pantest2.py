import cv2
import pytesseract
import re
from PIL import Image

# Load the image and pre-process it
img = cv2.imread('pandhanesh.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Extract text using OCR
text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')

# Define regular expressions for each field
pan_regex = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')
name_regex = re.compile(r'Name\n(.+)\n')
dob_regex = re.compile(r'Date of Birth / Date of Incorporation(.+)')
father_name_regex = re.compile(r'FATHER.*\n(.+)\n')
address_regex = re.compile(r'Address\n(.+)')

# Extract PAN number
pan_number = pan_regex.search(text)
if pan_number:
    pan_number = pan_number.group()
print('PAN number:', pan_number)

# Extract name
name = name_regex.search(text)
if name:
    name = name.group(1).strip()
print('Name:', name)

# Extract date of birth or incorporation
dob = dob_regex.search(text)
if dob:
    dob = dob.group(1).strip().replace(' ', '')
print('Date of Birth / Incorporation:', dob)

# Extract father's name
father_name = father_name_regex.search(text)
if father_name:
    father_name = father_name.group(1).strip()
print("Father's Name:", father_name)

# Extract address
address = address_regex.search(text)
if address:
    address = address.group(1).strip()
print('Address:', address)

# Validate the extracted fields
if pan_number and not pan_regex.match(pan_number):
    print('Invalid PAN number')
if dob and len(dob) != 10:
    print('Invalid date of birth')
if address and not address_regex.match(address):
    print('Invalid address')