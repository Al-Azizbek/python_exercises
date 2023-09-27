import os

# Define the main directory
main_directory = '/mnt/suger/Azizbek/FAS_merged_datasets/OULU-NPU/OULU-NPU_depth_maps'

# Define a function to delete all .txt files within a directory
def delete_txt_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f'Deleted: {file_path}')

# Iterate through the subdirectories in the main directory
for folder_name in os.listdir(main_directory):
    folder_path = os.path.join(main_directory, folder_name)

    # Check if the item in the main directory is a directory
    if os.path.isdir(folder_path):
        # Call the function to delete .txt files within this subdirectory
        delete_txt_files(folder_path)

print('All .txt files within the nested folders have been deleted.')
