import os
import shutil
from tqdm import tqdm

# Define the source directory
source_dir = '/mnt/nas/Test_folder/fas_dataset/data-voucher/dataV_test_img'

# Create the destination directories if they don't exist
real_folder = '/mnt/nas/Test_folder/fas_dataset/total_new/images/test/real'
spoof_folder = '/mnt/nas/Test_folder/fas_dataset/total_new/images/test/spoof'
os.makedirs(real_folder, exist_ok=True)
os.makedirs(spoof_folder, exist_ok=True)

# Initialize counters for naming
current_digit = 0
current_count = 1

# Create a list of folders to process
folders = sorted(os.listdir(source_dir))

# Create a tqdm progress bar for iterating through folders
for folder_name in tqdm(folders, desc="Copying Folders"):
    # Check if the folder name ends with '1'
    if folder_name.endswith('1'):
        current_digit = 1
        destination_dir = real_folder
    else:
        current_digit = 2  # You can adjust this for other cases
        destination_dir = spoof_folder

    # Create the new folder name
    new_folder_name = f'V_{current_count}_{current_digit}'

    # Build the full paths
    source_path = os.path.join(source_dir, folder_name)
    destination_path = os.path.join(destination_dir, new_folder_name)

    # Copy the folder to the appropriate destination
    shutil.copytree(source_path, destination_path)

    # Increment the current_count for the next folder
    current_count += 1

print("Folders copied with new names.")
