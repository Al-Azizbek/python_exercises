import os
import glob

# Specify the path to the parent folder containing all the images
path = "/mnt/suger/Azizbek/CDCNpp/face_depth_map_val/"

# Iterate over all .jpg files in the directory and its subdirectories
for filename in glob.iglob(path + '**/*.jpg', recursive=True):
    # Construct the new filename by replacing ".jpg_depth.jpg" with "_depth.jpg"
    new_filename = filename.replace(".jpg_depth.jpg", "_depth.jpg")
    
    # Rename the file
    os.rename(filename, new_filename)
