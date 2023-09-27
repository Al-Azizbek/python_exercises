import glob
import os
import pandas as pd


def remove_one_depth(row):
    if row[1] == 1:
        return row[2].replace("_depth", "", 1)  # only replace the first occurrence
    else:
        return row[2]

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/home/suger01/Desktop/CDCN_suger/val_files.csv', header=None)

# Apply the function to every row
df[2] = df.apply(remove_one_depth, axis=1)

# Save the modified DataFrame back to a CSV file
df.to_csv('/home/suger01/Desktop/CDCN_suger/val_files.csv', index=False, header=False)
