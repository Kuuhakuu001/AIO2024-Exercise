import numpy as np
import cv2

def resize_images(bg1_path, ob_path, bg2_path, size=(678, 381)):
    # Load and resize images
    bg1_image = cv2.imread(bg1_path)
    bg1_image = cv2.resize(bg1_image, size)

    ob_image = cv2.imread(ob_path)
    ob_image = cv2.resize(ob_image, size)

    bg2_image = cv2.imread(bg2_path)
    bg2_image = cv2.resize(bg2_image, size)

    return bg1_image, ob_image, bg2_image

def compute_difference(bg_img, input_img):
    difference = cv2.absdiff(bg_img, input_img)
    difference_single_channel = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    return difference_single_channel

def compute_binary_mask(difference_single_channel):
    _, difference_binary = cv2.threshold(difference_single_channel, 30, 255, cv2.THRESH_BINARY)
    return difference_binary

def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)

    # Ensure mask has 3 channels
    binary_mask_3c = cv2.cvtColor(binary_mask, cv2.COLOR_GRAY2BGR)

    # Blend the images based on the mask
    output = np.where(binary_mask_3c == 255, ob_image, bg2_image)
    return output

def main():
    # Paths to images
    bg1_path = './data/GreenBackground.png'
    ob_path = './data/Object.png'
    bg2_path = './data/NewBackground.jpg'

    # Resize images
    bg1_image, ob_image, bg2_image = resize_images(bg1_path, ob_path, bg2_path)

    # Display resized images
    cv2.imshow('Original Background', bg1_image)
    cv2.imshow('Object Image', ob_image)
    cv2.imshow('Target Background', bg2_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Compute difference and display
    difference_single_channel = compute_difference(bg1_image, ob_image)
    cv2.imshow('Difference', difference_single_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Compute binary mask and display
    binary_mask = compute_binary_mask(difference_single_channel)
    cv2.imshow('Binary Mask', binary_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Replace background and display final output
    output = replace_background(bg1_image, bg2_image, ob_image)
    cv2.imshow('Final Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
