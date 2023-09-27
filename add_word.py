import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/home/suger01/Desktop/CDCN_suger/Val.csv', header=None)

# Define a function to modify the path
def modify_path(path):
    if path != '0':
        return path.replace('.jpg', '_depth.jpg')
    else:
        return path

# Apply the function to the 3rd column
df[2] = df[2].apply(modify_path)

# Save the modified DataFrame back to a CSV file
df.to_csv('./finaval.csv', index=False, header=False)
