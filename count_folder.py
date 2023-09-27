import os


# Specify the directory path where you want to perform the operation
directory_path = '/mnt/suger/Azizbek/beta'

# Iterate through the folders in the specified directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)
    
    # Check if the folder name ends with "_2"
    if folder_name.endswith("_2") and os.path.isdir(folder_path):
        # Delete the folder and its contents
        try:
            os.rmdir(folder_path)
            print(f"Deleted folder: {folder_path}")
        except OSError as e:
            print(f"Error deleting folder {folder_path}: {e}")

print("Operation complete.")
