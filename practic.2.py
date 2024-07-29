image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mean_kernel = np.ones((3, 3)) / 9

filtered_image = filters.convolve2d(image, mean_kernel)

print(filtered_image)
from skimage import filters

image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

filtered_image = filters.blur(image, sigma=1)

print(filtered_image)