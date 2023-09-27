import os
import cv2
import numpy as np
from tqdm import tqdm

# Function to generate bbox and save it as a text file
def generate_bbox(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Get image dimensions
    h, w, _ = img.shape

    # Calculate bbox coordinates (assuming the entire image is the bbox)
    y1, x1, y2, x2 = 0, 0, h, w

    # Create a text file with the same name as the image but with a .txt extension
    bbox_file_path = os.path.splitext(image_path)[0] + ".txt"

    # Save bbox coordinates to the text file
    with open(bbox_file_path, "w") as f:
        f.write(f"{y1} {x1} {y2-y1} {x2-x1}")

# Specify the path to the parent directory containing subdirectories with images
parent_directory = "/mnt/suger/Azizbek/FAS_merged_datasets/OULU-NPU/OULU-NPU_depth_maps"

# Use tqdm to track progress while processing images
for root, _, files in tqdm(os.walk(parent_directory), desc="Generating Bounding Boxes"):
    for filename in files:
        if filename.endswith((".jpg", ".png")):  # You can add more supported image extensions
            image_path = os.path.join(root, filename)
            generate_bbox(image_path)

print("Bounding box annotations generated and saved.")





