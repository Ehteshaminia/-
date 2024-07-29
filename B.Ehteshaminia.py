import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload an image
uploaded = files.upload()

 
# Read the uploaded image
if uploaded:
    image_path = list(uploaded.keys())[0]
    original_image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if original_image is not None:
        # Define the rotation angle
        angle = 30

        # Rotate the image
        height, width = original_image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))

        # Display the original and rotated images
        print("Original Image:")
        cv2_imshow(original_image)

        print("Rotated Image (30 degrees):")
        cv2_imshow(rotated_image)
    else:
        print("Error: Unable to read the image file.")
