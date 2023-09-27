import os
import shutil

# Define the main directory where the folders are located
main_directory = "/mnt/suger/Azizbek/CDCNpp_3DDFA/Train_img"

# Create 'spoof_faces' and 'real_faces' directories if they don't exist
spoof_faces_path = os.path.join(main_directory, 'spoof_faces')
real_faces_path = os.path.join(main_directory, 'real_faces')

if not os.path.exists(spoof_faces_path):
    os.mkdir(spoof_faces_path)

if not os.path.exists(real_faces_path):
    os.mkdir(real_faces_path)

# Iterate through the folders in the main directory
for folder_name in os.listdir(main_directory):
    folder_path = os.path.join(main_directory, folder_name)

    # Check if it is a directory and ends with either '_1' or another digit
    if os.path.isdir(folder_path):
        if folder_name.endswith('_1'):
            # Move to 'real_faces' directory
            shutil.move(folder_path, os.path.join(real_faces_path, folder_name))
        elif folder_name[-2:] in ['_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_0']:
            # Move to 'spoof_faces' directory
            shutil.move(folder_path, os.path.join(spoof_faces_path, folder_name))

print("Folders have been moved successfully.")




import cv2
import glob
import os

# define your main directory path
main_directory = '/mnt/nas/Test_folder/Azizbek/FAS_merged_datasets/OULU-NPU/OULU-NPU_depth_maps/t_dev_crop_img_depth'



# use glob to get all the jpg images recursively from all folders and subfolders
for img_path in glob.glob(main_directory + '/*.jpg', recursive=True):
    # Load the depth map image
    depth_map = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the depth map to 32x32
    resized_depth_map = cv2.resize(depth_map, (224, 224))
    
    # Save the resized depth map to the original location, overwriting the original image
    cv2.imwrite(img_path, resized_depth_map)
