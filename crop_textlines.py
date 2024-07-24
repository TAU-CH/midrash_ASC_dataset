import json
import os
from PIL import Image

# Load the JSON file
with open('textline_detections.json', 'r') as f:
    textline_data = json.load(f)

# Define the directories
input_dir = 'cropped_main_text_regions'
output_base_dir = 'cropped_text_lines'

# Iterate over each image and its text lines
for image_name, image_data in textline_data.items():
    # Open the image
    image_path = os.path.join(input_dir, image_name)
    if not os.path.exists(image_path):
        print(f"Image {image_path} does not exist. Skipping...")
        continue
    
    image = Image.open(image_path)
    image_basename = os.path.splitext(image_name)[0]

    # Create a directory for each region
    region_dir = os.path.join(output_base_dir, image_basename)
    os.makedirs(region_dir, exist_ok=True)
    
    # Iterate over each text line and crop the image
    for idx, bbox in enumerate(image_data['text_lines']):
        x, y, width, height = bbox
        cropped_line = image.crop((x, y, x + width, y + height))
        
        # Save the cropped text line image
        cropped_line_name = f"line_{idx}.jpg"
        cropped_line_path = os.path.join(region_dir, cropped_line_name)
        cropped_line.save(cropped_line_path)

print("Text line cropping completed.")
