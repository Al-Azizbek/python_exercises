import cv2
import numpy as np

# Load your image
image = cv2.imread('/home/suger01/Desktop/image02673.png')

# Create a 32x32 array filled with zeros
map_x = np.zeros((32, 32), dtype=np.uint8)  # Assuming you want an 8-bit grayscale image

# Specify the position where you want to overlay the zeros (e.g., top-left corner)
x_position = 10  # Adjust as needed
y_position = 10  # Adjust as needed

# Overlay the zeros on the image
image[y_position:y_position+32, x_position:x_position+32] = map_x

# Save the modified image as a JPEG file
cv2.imwrite('modified_image.jpg', image)
