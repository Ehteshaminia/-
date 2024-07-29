import cv2
from google.colab.patches import cv2_imshow
import ipywidgets as widgets
from IPython.display import display

from google.colab import files
uploaded = files.upload()

 saving '1.png' to '1.png'(1)


# Function to handle grayscale conversion and saving
def process_image(b):
    # Check if the image exists
    if 'img' not in globals():
        print("Error: Image not found.")
        return

    # Check if the button press was for grayscale conversion
    if b.description == 'Convert to Grayscale':
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Display the grayscale image
        cv2_imshow(gray_img)
        # Save the grayscale image
        cv2.imwrite('output_gray.jpg', gray_img)
        print("Grayscale image saved as output_gray.jpg")
    elif b.description == 'Finish':
        print("Finish")
        # Close the window
        cv2.destroyAllWindows()

def main():
    # Read the image
    global img
    img = cv2.imread('1.png')

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Unable to read the image file.")
        return

    # Display the image
    cv2_imshow(img)

    # Create buttons for grayscale conversion and finishing
    grayscale_button = widgets.Button(description="Convert to Grayscale")
    finish_button = widgets.Button(description="Finish")

    # Register button click events
    grayscale_button.on_click(process_image)
    finish_button.on_click(process_image)

    # Display buttons
    display(widgets.HBox([grayscale_button, finish_button]))

if __name__ == "__main__":
    main()

