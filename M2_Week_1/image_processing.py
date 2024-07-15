import matplotlib.image as mpimg
import numpy as np

def convert_to_grayscale_lightness(image):
    """
    Convert a color image to grayscale using the Lightness method.
    
    Parameters:
    image (numpy.ndarray): The input color image as a NumPy array.
    
    Returns:
    numpy.ndarray: The grayscale image as a NumPy array.
    """
    # Calculate the lightness for each pixel
    gray_image = (np.max(image, axis=2) + np.min(image, axis=2)) / 2
    return gray_image


def convert_to_grayscale_average(image):
    """
    Convert a color image to grayscale using the Average method.
    
    Parameters:
    image (numpy.ndarray): The input color image as a NumPy array.
    
    Returns:
    numpy.ndarray: The grayscale image as a NumPy array.
    """
    gray_image = np.mean(image, axis=2)
    return gray_image


def convert_to_grayscale_luminosity(image):
    """
    Convert a color image to grayscale using the Luminosity method.
    
    Parameters:
    image (numpy.ndarray): The input color image as a NumPy array.
    
    Returns:
    numpy.ndarray: The grayscale image as a NumPy array.
    """
    gray_image = 0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]
    return gray_image


img = mpimg.imread('./images/dog.jpeg')
gray_img_01 = convert_to_grayscale_lightness(img)
print(gray_img_01[0, 0])
# Q12: Answer A

gray_img_02 = convert_to_grayscale_average(img)
print(gray_img_02[0, 0])

gray_img_03 = convert_to_grayscale_luminosity(img)
print(gray_img_03[0, 0])