import os
import cv2
import numpy as np

# Define the main directory containing subfolders with images
main_directory = '/mnt/suger/Azizbek/FAS_merged_datasets/OULU-NPU/OULU-NPU_depth_maps/t_train_crop_img_depth/fake'

# Define the target size
target_size = (224, 224)

# Iterate through the subfolders in the main directory
for folder_name in os.listdir(main_directory):
    folder_path = os.path.join(main_directory, folder_name)

    # Check if the item in the main directory is a subfolder
    if os.path.isdir(folder_path):
        # Iterate through the files in the subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                # Load the image using OpenCV
                image_path = os.path.join(folder_path, filename)
                img = cv2.imread(image_path)

                # Calculate the aspect ratio of the original image
                aspect_ratio = float(img.shape[1]) / float(img.shape[0])

                # Resize the image while maintaining the aspect ratio
                if aspect_ratio > 1:
                    new_width = target_size[0]
                    new_height = int(target_size[0] / aspect_ratio)
                else:
                    new_width = int(target_size[1] * aspect_ratio)
                    new_height = target_size[1]

                resized_img = cv2.resize(img, (new_width, new_height))

                # Create a black background image of the target size
                result = np.zeros((target_size[0], target_size[1], 3), dtype=np.uint8)
                result.fill(0)  # Fill with black color

                # Calculate the position to paste the resized image in the center
                x_offset = (target_size[1] - new_width) // 2
                y_offset = (target_size[0] - new_height) // 2

                # Paste the resized image onto the black background
                result[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_img

                # Save the resized image with the original name in the same folder
                output_path = os.path.join(folder_path, filename)
                cv2.imwrite(output_path, result)

print('All images in their original folders have been resized to 224x224 with a black background while maintaining aspect ratio.')
































# import cv2
# import glob
# import os

# # define your main directory path
# main_directory = '/mnt/suger/Azizbek/FAS_merged_datasets/OULU-NPU/OULU-NPU_depth_maps/t_train_crop_img_depth/fake'



# # use glob to get all the jpg images recursively from all folders and subfolders
# for img_path in glob.glob(main_directory + '/*.jpg', recursive=True):
#     # Load the depth map image
#     depth_map = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
#     # Resize the depth map to 32x32
#     resized_depth_map = cv2.resize(depth_map, (224, 224))
    
#     # Save the resized depth map to the original location, overwriting the original image
#     cv2.imwrite(img_path, resized_depth_map)
