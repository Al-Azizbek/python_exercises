import os
from PIL import Image
import glob

path = "/mnt/suger/Azizbek/CDCNpp_3DDFA/Train_img/spoof_faces/"

# Iterate through all PNG files in all subdirectories of the given path
for png_file in glob.glob(path + '**/*.png', recursive=True):
    # Open the PNG file
    img = Image.open(png_file)

    # Define the corresponding JPEG file name
    jpg_file = os.path.splitext(png_file)[0] + '.jpg'

    # Save the image in JPEG format
    img.convert('RGB').save(jpg_file)

    # Optionally, delete the original PNG file
    os.remove(png_file)

print('PNG to JPEG conversion complete.')
