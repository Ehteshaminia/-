import numpy as np


 # importing cv2
    import cv2
    
    


 # path
    path = r'moon.png'

    # Reading an image in default mode
    src = cv2.imread(path)

 # Read the image is displayed 
image = cv2.imdecode(np.frombuffer(src, np.uint8), -1)



 # Display the original image
print("Original Image:")
cv2_imshow(image)



 # Apply the average filter
filtered_image = cv2.blur(image, (5, 5))  # Using a 5x5 average filter here
 # Display the filtered image
print("filtered image with average filter:")
cv2_imshow(filtered_image)



