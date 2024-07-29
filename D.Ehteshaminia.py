import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

def resize_image(img, new_width, new_height):
    return cv2.resize(img, (new_width, new_height))

# Upload an image
uploaded = files.upload()

# Read and resize the uploaded image
if uploaded:
    image_path = list(uploaded.keys())[0]
    original_img = cv2.imread(image_path)

    if original_img is not None:
        new_width, new_height = 400, 300
        resized_img = resize_image(original_img, new_width, new_height)

        print("Original Image:")
        cv2_imshow(original_img)

        print("Resized Image:")
        cv2_imshow(resized_img)
    else:
        print("Error: Unable to read the image file.")