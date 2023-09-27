import os
import random  # Import the random module

# Define the path to the directory containing folders with different endings
base_dir = "/mnt/suger/Azizbek/beta"

# Define the output file name
output_file = "/home/suger01/Desktop/suger_codes/beta_train.txt"

# Function to check if a folder name ends with "_1," "_2," "_3," "_4," or "_5"
def get_label(folder_name):
    if folder_name.endswith("_1"):
        return "+1"
    elif folder_name.endswith("_3"):
        return "-1"
    elif folder_name.endswith("_4"):
        return "-1"
    elif folder_name.endswith("_5"):
        return "-1"
    else:
        return None

# Create a list to store the rows
rows = []

# Loop through subfolders
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    # Check if the item is a directory
    if os.path.isdir(folder_path):
        label_value = get_label(folder_name)
        if label_value is not None:
            rows.append(f"{label_value},{folder_name}")

# Shuffle the rows
random.shuffle(rows)

# Open the output file for writing
with open(output_file, 'w') as file:
    # Write the shuffled rows to the output file
    for row in rows:
        file.write(f"{row}\n")

print("Output file generated:", output_file)
