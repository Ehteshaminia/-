import cv2
import time
from google.colab.patches import cv2_imshow
import ipywidgets as widgets
from IPython.display import display

from google.colab import files
uploaded = files.upload()

def main():
    # Read the image
    img = cv2.imread('1.png')

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Unable to read the image file.")
        return

    # Display the image in a window named "Img"
    cv2_imshow(img)

    # Function to be called after 5 seconds
    def esc_button_clicked(b):
        print("esc button pressed after 5 seconds")
        # Add your code here to perform actions after pressing 'esc'

    # Create a button named 'esc'
    esc_button = widgets.Button(description="esc")

    # Register the button click event
    esc_button.on_click(esc_button_clicked)

    # Display the button
    display(esc_button)

    # Set a flag to check if 'esc' key is pressed
    esc_pressed = False

    # Start a timer
    start_time = time.time()

    # Wait for 5 seconds or until 'esc' key is pressed
    while (time.time() - start_time) < 5:
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # 27 corresponds to the esc key in OpenCV
            esc_pressed = True
            break

    # If 'esc' key is pressed, exit the program
    if esc_pressed:
        print("Window closed. 'esc' key was pressed.")
        return

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite('output_gray.jpg', gray_img)

    print("Grayscale image saved as output_gray.jpg")
    print("No key pressed within 5 seconds.")

if __name__ == "__main__":
    main()