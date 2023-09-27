import os
import cv2
from retinaface import RetinaFace

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_images(source_dir, target_dir):
    # Initialize the RetinaFace detector
    detector = RetinaFace(quality="normal")

    # loop through source directory
    for subdir, dirs, files in os.walk(source_dir):
        for file in files:
            # get full file path
            file_path = subdir + os.sep + file
            # read the image
            image = cv2.imread(file_path)

            # Check if image is read correctly
            if image is None:
                print(f"Failed to read image at {file_path}")
                continue
            
            # perform face detection
            faces = detector.predict(image)
            if faces is not None:
                # if faces are detected, crop to face and resize
                for i, face_bbox in enumerate(faces):
                    x1, y1, x2, y2 = face_bbox["x1"], face_bbox["y1"], face_bbox["x2"], face_bbox["y2"]
                    face = image[y1:y2, x1:x2]
                    face = cv2.resize(face, (256, 256))
                    
                    # save the image in the target directory
                    new_subdir = subdir.replace(source_dir, target_dir)
                    new_file_path = f"{new_subdir + os.sep + os.path.splitext(file)[0]}_{i}.jpg"
                    ensure_dir(new_file_path)
                    cv2.imwrite(new_file_path, face)
                    print(f"Saved image with detected face: {new_file_path}")

# specify source and target directories
source_dir = "/mnt/suger/OULU_WorkSpace/train_img_flod"
target_dir = '/mnt/suger/Azizbek/CDCNpp/cropped_faces_train_img'

# start processing
process_images(source_dir, target_dir)


# faces are extrected by using insideface checkpoints