import cv2
import math

def crop_face_from_scene(image, face_name_full, scale, additional_right_space=0, additional_height=0, additional_width=0, save_path=None):
    f = open(face_name_full, 'r')
    lines = f.readlines()
    lines = lines[0].split(' ')
    y1, x1, w, h = [int(ele) for ele in lines[:4]]
    f.close()
    y2 = y1 + w
    x2 = x1 + h

    y_mid = (y1 + y2) / 2.0
    x_mid = (x1 + x2) / 2.0
    h_img, w_img = image.shape[0], image.shape[1]
    
    w_scale = scale * w
    h_scale = scale * h
    
    y1 = y_mid - (w_scale / 2.0) - (3 * additional_height / 2.0)  # Multiply by 4 for four times more height
    x1 = x_mid - (h_scale / 2.0) - (3 * additional_width / 2.0)  # Multiply by 4 for four times more width
    y2 = y_mid + (w_scale / 2.0) + (3 * additional_height / 2.0)  # Multiply by 4 for four times more height
    x2 = x_mid + (h_scale / 2.0) + (3 * additional_width / 2.0)  # Multiply by 4 for four times more width
    
    # Add more space on the right side (multiply by additional_right_space)
    additional_space = int(w_scale * (additional_right_space))  # Multiply by 4 for four times more right space
    x2 += additional_space
    
    y1 = max(math.floor(y1), 0)
    x1 = max(math.floor(x1), 0)
    y2 = min(math.floor(y2), w_img)
    x2 = min(math.floor(x2), h_img)

    region = image[x1:x2, y1:y2]

    if save_path:
        cv2.imwrite(save_path, region)

    return region

# Example usage:
image = cv2.imread("/home/suger01/Downloads/0.jpg")
# Add four times more space: 320 pixels of additional space on the right side, 160 pixels of additional height, and 160 pixels of additional width
cropped_face = crop_face_from_scene(image, "/home/suger01/Downloads/0(7).txt", scale=1.0, additional_right_space=10, additional_height=100, additional_width=50, save_path="/home/suger01/Downloads/cropped_faces.jpg")
