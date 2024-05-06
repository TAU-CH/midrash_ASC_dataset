import json
import os
import random
import cv2

'''
Generate bounding box visualizations for the Ashkenazi Square Clustering (ASC) dataset using the
COCO annotations
'''

def load_coco_file(coco_file):
    with open(coco_file, 'r') as f:
        return json.load(f)

def draw_boxes(image, boxes, color):
    for box in boxes:
        x, y, w, h = box
        cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), color, 2)

def visualize_coco(image_name, coco_data, max_height):
    image_data = coco_data[image_name]
    image = cv2.imread(get_image_path(image_name))
    
    # Resize image if it exceeds max_height
    height, width = image.shape[:2]
    if height > max_height:
        ratio = max_height / height
        image = cv2.resize(image, (int(width * ratio), max_height))
        
        # Resize annotations accordingly
        for region_data in image_data.values():
            if 'bbox' in region_data:
                region_data['bbox'] = [int(x * ratio) for x in region_data['bbox']]

            if 'text_lines' in region_data:
                region_data['text_lines'] = [[int(x * ratio) for x in line] for line in region_data['text_lines']]
    
    # Draw text regions in red
    for region_data in image_data.values():
        if 'bbox' in region_data:
            draw_boxes(image, [region_data['bbox']], (0, 0, 255))  # Red color for text regions

        # Draw text lines in blue
        if 'text_lines' in region_data:
            draw_boxes(image, region_data['text_lines'], (255, 0, 0))  # Blue color for text lines


    cv2.imshow('Annotation', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_image_path(filename):
    return os.path.join(image_folder_path, filename)

def get_parent_image_id(text_region_filename):
    return text_region_filename.split('_')[0]  


image_folder = 'path to the folder containing images'
image_folder_path = os.path.abspath(image_folder)
input_image_filename = 'input file name'  
merged_coco_file = 'path to the merged annotations coco file'


coco_data = load_coco_file(merged_coco_file)


visualize_coco(input_image_filename, coco_data,max_height=1000) 
