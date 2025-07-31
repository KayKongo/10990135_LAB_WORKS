"""
Color Space Converter with Histogram Analysis

This script loads a color image and converts it to multiple color spaces:
- Grayscale
- HSV (Hue, Saturation, Value)
- LAB (L*a*b* color space)

The script displays all converted images, saves them with descriptive filenames,
and plots a histogram for the grayscale image.

Requirements:
- opencv-python (cv2)
- matplotlib
- numpy

Usage:
    python task2.py
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
        
    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If image cannot be loaded
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
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def convert_to_hsv(image):
    """
    Convert a color image from BGR to HSV color space.
    
    Args:
        image (numpy.ndarray): Input color image in BGR format
        
    Returns:
        numpy.ndarray: Image in HSV color space
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image

def convert_to_lab(image):
    """
    Convert a color image from BGR to LAB color space.
    
    Args:
        image (numpy.ndarray): Input color image in BGR format
        
    Returns:
        numpy.ndarray: Image in LAB color space
    """
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return lab_image

def display_images(original, grayscale, hsv, lab):
    """
    Display original and all converted images in a 2x2 grid.
    
    Args:
        original (numpy.ndarray): Original color image in BGR format
        grayscale (numpy.ndarray): Grayscale image
        hsv (numpy.ndarray): HSV image
        lab (numpy.ndarray): LAB image
    """
    # Convert BGR to RGB for proper display in matplotlib
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)  # Convert HSV to RGB for display
    lab_rgb = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)  # Convert LAB to RGB for display
    
    # Create subplot with 2 rows, 2 columns
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Display original image
    axes[0, 0].imshow(original_rgb)
    axes[0, 0].set_title('Original Image (RGB)', fontsize=14, fontweight='bold')
    axes[0, 0].axis('off')
    
    # Display grayscale image
    axes[0, 1].imshow(grayscale, cmap='gray')
    axes[0, 1].set_title('Grayscale Image', fontsize=14, fontweight='bold')
    axes[0, 1].axis('off')
    
    # Display HSV image
    axes[1, 0].imshow(hsv_rgb)
    axes[1, 0].set_title('HSV Color Space', fontsize=14, fontweight='bold')
    axes[1, 0].axis('off')
    
    # Display LAB image
    axes[1, 1].imshow(lab_rgb)
    axes[1, 1].set_title('LAB Color Space', fontsize=14, fontweight='bold')
    axes[1, 1].axis('off')
    
    # Adjust layout and display
    plt.tight_layout()
    plt.suptitle('Color Space Conversions', fontsize=16, fontweight='bold', y=0.98)
    plt.show()

def plot_grayscale_histogram(grayscale_image):
    """
    Plot and display histogram of the grayscale image.
    
    Args:
        grayscale_image (numpy.ndarray): Grayscale image
    """
    # Calculate histogram
    # bins=256 for 256 possible pixel values (0-255)
    # range=[0, 256] specifies the range of pixel values
    histogram = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    
    # Plot histogram
    plt.plot(histogram, color='black', linewidth=2)
    plt.fill_between(range(256), histogram.flatten(), alpha=0.3, color='gray')
    
    # Customize the plot
    plt.title('Grayscale Image Histogram', fontsize=16, fontweight='bold')
    plt.xlabel('Pixel Intensity Value', fontsize=12)
    plt.ylabel('Number of Pixels', fontsize=12)
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    # Add some statistics as text on the plot
    mean_intensity = np.mean(grayscale_image)
    std_intensity = np.std(grayscale_image)
    plt.text(0.7, 0.9, f'Mean: {mean_intensity:.2f}\\nStd: {std_intensity:.2f}', 
             transform=plt.gca().transAxes, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=10)
    
    plt.tight_layout()
    plt.show()

def save_image(image, output_path, image_type):
    """
    Save an image to specified path with error handling.
    
    Args:
        image (numpy.ndarray): Image to save
        output_path (str): Path where to save the image
        image_type (str): Type of image for logging purposes
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    # Save the image
    success = cv2.imwrite(output_path, image)
    
    if success:
        print(f"{image_type} image successfully saved to: {output_path}")
    else:
        print(f"Failed to save {image_type} image to: {output_path}")

def save_all_images(grayscale, hsv, lab, src_dir):
    """
    Save all converted images with appropriate filenames.
    
    Args:
        grayscale (numpy.ndarray): Grayscale image
        hsv (numpy.ndarray): HSV image
        lab (numpy.ndarray): LAB image
        src_dir (str): Source directory path
    """
    # Define output paths
    grayscale_path = os.path.join(src_dir, 'images', 'saved', 'photo_grayscale.jpg')
    hsv_path = os.path.join(src_dir, 'images', 'saved', 'photo_hsv.jpg')
    lab_path = os.path.join(src_dir, 'images', 'saved', 'photo_lab.jpg')
    
    # Save each image
    print("Saving converted images...")
    save_image(grayscale, grayscale_path, "Grayscale")
    save_image(hsv, hsv_path, "HSV")
    save_image(lab, lab_path, "LAB")

def main():
    """
    Main function to execute the color space conversion pipeline.
    """
    # Get the directory paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(script_dir)  # Go up one level to the 'src' directory
    
    # Define input image path
    input_image_path = os.path.join(src_dir, 'images', 'original', 'photo.jpg')
    
    # Debug: Print directory information
    print("=" * 60)
    print("COLOR SPACE CONVERSION PIPELINE")
    print("=" * 60)
    print(f"Script directory: {script_dir}")
    print(f"Source directory: {src_dir}")
    print(f"Input image path: {input_image_path}")
    print("-" * 60)
    
    try:
        # Step 1: Load the original image
        print("Step 1: Loading original image...")
        original_image = load_image(input_image_path)
        print(f"✓ Image loaded successfully. Shape: {original_image.shape}")
        print(f"  Image dimensions: {original_image.shape[1]}x{original_image.shape[0]} pixels")
        print(f"  Color channels: {original_image.shape[2]}")
        
        # Step 2: Convert to different color spaces
        print("\\nStep 2: Converting to different color spaces...")
        
        print("  Converting to Grayscale...")
        grayscale_image = convert_to_grayscale(original_image)
        print(f"  ✓ Grayscale conversion complete. Shape: {grayscale_image.shape}")
        
        print("  Converting to HSV...")
        hsv_image = convert_to_hsv(original_image)
        print(f"  ✓ HSV conversion complete. Shape: {hsv_image.shape}")
        
        print("  Converting to LAB...")
        lab_image = convert_to_lab(original_image)
        print(f"  ✓ LAB conversion complete. Shape: {lab_image.shape}")
        
        # Step 3: Display all images
        print("\\nStep 3: Displaying converted images...")
        display_images(original_image, grayscale_image, hsv_image, lab_image)
        print("✓ All images displayed successfully")
        
        # Step 4: Save all converted images
        print("\\nStep 4: Saving converted images...")
        save_all_images(grayscale_image, hsv_image, lab_image, src_dir)
        print("✓ All images saved successfully")
        
        # Step 5: Plot and display grayscale histogram
        print("\\nStep 5: Generating grayscale histogram...")
        plot_grayscale_histogram(grayscale_image)
        print("✓ Histogram displayed successfully")
        
        print("\\n" + "=" * 60)
        print("COLOR SPACE CONVERSION PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please ensure the image file exists in the 'images/original/' directory.")
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("Please check if the image file is valid.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()