"""
Image Grayscale Converter

This script loads an image from the images directory, converts it to grayscale,
displays both original and grayscale versions, and saves the grayscale image.

Requirements:
- opencv-python (cv2)
- matplotlib
- numpy

Usage:
    python task1.py
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def load_image(image_path):
    """
    Load an image from the specified path.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        numpy.ndarray: Loaded image in BGR format (OpenCV default)
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from: {image_path}")
    
    return image

def convert_to_grayscale(image):
    """
    Convert a color image to grayscale.
    
    Args:
        image (numpy.ndarray): Input color image in BGR format
        
    Returns:
        numpy.ndarray: Grayscale image
    """
    # Convert BGR to grayscale using OpenCV
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def display_images(original, grayscale):
    """
    Display original and grayscale images side by side.
    
    Args:
        original (numpy.ndarray): Original color image in BGR format
        grayscale (numpy.ndarray): Grayscale image
    """
    # Convert BGR to RGB for proper display in matplotlib
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    # Create subplot with 1 row, 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    axes[0].imshow(original_rgb)
    axes[0].set_title('Original Image', fontsize=14)
    axes[0].axis('off')  # Remove axis ticks and labels
    
    # Display grayscale image
    axes[1].imshow(grayscale, cmap='gray')
    axes[1].set_title('Grayscale Image', fontsize=14)
    axes[1].axis('off')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def save_grayscale_image(grayscale_image, output_path):
    """
    Save the grayscale image to specified path.
    
    Args:
        grayscale_image (numpy.ndarray): Grayscale image to save
        output_path (str): Path where to save the image
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the grayscale image
    success = cv2.imwrite(output_path, grayscale_image)
    
    if success:
        print(f"Grayscale image successfully saved to: {output_path}")
    else:
        print(f"Failed to save image to: {output_path}")

def main():
    """
    Main function to execute the image processing pipeline.
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the src directory, then into images
    src_dir = os.path.dirname(script_dir)  # This gets us to the 'src' directory
    
    # Define file paths relative to the src directory
    input_image_path = os.path.join(src_dir, 'images', 'original', 'photo.jpg')
    output_image_path = os.path.join(src_dir, 'images', 'saved', 'photo_gray.jpg')
    
    # Debug: Print current working directory and paths
    print(f"Current working directory: {os.getcwd()}")
    print(f"Script directory: {script_dir}")
    print(f"Source directory: {src_dir}")
    print(f"Looking for image at: {input_image_path}")
    print(f"Will save grayscale image to: {output_image_path}")
    print("-" * 50)
    
    try:
        # Step 1: Load the original image
        print("Loading image...")
        original_image = load_image(input_image_path)
        print(f"Image loaded successfully. Shape: {original_image.shape}")
        
        # Step 2: Convert to grayscale
        print("Converting to grayscale...")
        grayscale_image = convert_to_grayscale(original_image)
        print(f"Conversion complete. Grayscale shape: {grayscale_image.shape}")
        
        # Step 3: Display both images
        print("Displaying images...")
        display_images(original_image, grayscale_image)
        
        # Step 4: Save the grayscale image
        print("Saving grayscale image...")
        save_grayscale_image(grayscale_image, output_image_path)
        
        print("Image processing pipeline completed successfully!")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the image file exists in the 'images/original/' directory.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please check if the image file is valid.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()