import glob
import os
import pandas as pd

path = "/mnt/suger/OULU_WorkSpace/test_img_flod/"
file_list = glob.glob(path + "*/*/*.jpg")

labels = []

for i in file_list:
    if "real" in i:
        depth_path = i.replace("Val_img/real_faces", "Val_img_depth").replace(".jpg", "_depth.jpg")
        labels.append((i, 1))
    else:
        labels.append((i, 0))  # Use a placeholder for fake images

# Create a DataFrame from the labels list
df = pd.DataFrame(labels, columns=['img', 'label'])

# Shuffle the rows
df = df.sample(frac=1).reset_index(drop=True)

# Save the shuffled dataset as a single CSV file
df.to_csv("./Val.csv", header=False, index=False, columns=['img', 'label'])
