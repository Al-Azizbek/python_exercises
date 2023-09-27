import cv2
import os

def crop_face_from_scene(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Get the image's base filename without extension
    base_filename = os.path.splitext(os.path.basename(image_path))[0]

    # Path to the corresponding bounding box text file
    bbox_file_path = os.path.join(os.path.dirname(image_path), f"{base_filename}.txt")

    if not os.path.exists(bbox_file_path):
        raise FileNotFoundError(f"Bounding box file not found: {bbox_file_path}")

    # Read the bounding box coordinates from the text file
    with open(bbox_file_path, "r") as f:
        y1, x1, h, w = [float(ele) for ele in f.readline().split()]

    y2 = y1 + h
    x2 = x1 + w

    # Ensure that the coordinates are within valid image bounds
    y1 = max(int(y1), 0)
    x1 = max(int(x1), 0)
    y2 = min(int(y2), image.shape[0])
    x2 = min(int(x2), image.shape[1])

    # Crop the region from the image
    region = image[y1:y2, x1:x2]

    return region

# Example usage:
image_path = "/home/suger01/Desktop/test_folder/0.jpg"  # Replace with the path to your image
cropped_face = crop_face_from_scene(image_path)
cv2.imwrite("./cropped_face.jpg", cropped_face)  # Save the cropped face
