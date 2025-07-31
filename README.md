# 10990135_LAB_WORKS

This repository contains lab works for the **DCIT 412 (Computer Vision)** practical assignment. The project demonstrates fundamental computer vision techniques including image loading, color space conversions, grayscale conversion, and binary thresholding concepts.

## Repository Structure

```
10990135_LAB_WORKS/
├── src/
│   ├── images/
│   │   ├── original/
│   │   │   └── photo.jpg          # Source image for processing
│   │   └── saved/                 # Output directory for processed images
│   │       ├── photo_gray.jpg     # Task 1 output
│   │       ├── photo_grayscale.jpg # Task 2 outputs
│   │       ├── photo_hsv.jpg
│   │       └── photo_lab.jpg
│   ├── Task_1/
│   │   └── task1.py               # Image loading and grayscale conversion
│   └── Task_2/
│       └── task2.py               # Color space conversion and histogram analysis
├── requirements.txt               # Python dependencies
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore rules
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation and Setup

### For New Users

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd 10990135_LAB_WORKS
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Ensure you have an image file:**
   - Place your test image as `photo.jpg` in the `src/images/original/` directory

### For Other Developers

When others clone this repository, they should run:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows (use source venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
```

## Running the Tasks

### Task 1: Image Loading and Grayscale Conversion

Navigate to the Task_1 directory and run:

```bash
cd src/Task_1
python task1.py
```

**What it does:**

- Loads an image file from `../images/original/photo.jpg`
- Converts the image to grayscale
- Displays both original and grayscale images side-by-side
- Saves the grayscale image as `../images/saved/photo_gray.jpg`

### Task 2: Color Space Conversion and Histogram Analysis

Navigate to the Task_2 directory and run:

```bash
cd src/Task_2
python task2.py
```

**What it does:**

- Loads the original color image
- Converts the image to multiple color spaces:
  - Grayscale
  - HSV (Hue, Saturation, Value)
  - LAB (L*a*b\* color space)
- Displays all converted images in a 2×2 grid
- Saves each converted image with descriptive filenames
- Generates and displays a histogram for the grayscale image with statistical analysis

### Task 3: Binary Thresholding (Theoretical)

**Problem:** A pixel in a grayscale image has a value of 180. If the threshold for binary thresholding is set to 150, what is the new pixel value after applying binary thresholding?

**Answer:** 255

**Explanation:** Since 180 ≥ 150 (pixel value is above threshold), the output value is 255 (white). Binary thresholding assigns 255 to pixels above the threshold and 0 to pixels below the threshold.

## Dependencies

The project requires the following Python packages (listed in `requirements.txt`):

```
opencv-python>=4.5.0
matplotlib>=3.5.0
numpy>=1.21.0
```

## Key Features

- **Modular Design:** Each task is organized in separate directories with independent scripts
- **Error Handling:** Comprehensive error handling for file operations and image processing
- **Visual Output:** All tasks include visual displays of results using matplotlib
- **Automatic Directory Creation:** Scripts automatically create output directories if they don't exist
- **Detailed Logging:** Informative console output showing processing steps and results
- **Documentation:** Well-commented code with docstrings for all functions

## Tasks Overview

### Task 1: Image Loading and Grayscale Conversion

- **File:** `src/Task_1/task1.py`
- **Purpose:** Demonstrates basic image I/O and grayscale conversion
- **Output:** Grayscale version of the input image
- **Key Techniques:** OpenCV image loading, color space conversion, matplotlib visualization

### Task 2: Color Space Conversion and Histogram Analysis

- **File:** `src/Task_2/task2.py`
- **Purpose:** Explores multiple color spaces and histogram analysis
- **Output:** Images in Grayscale, HSV, and LAB color spaces + histogram plot
- **Key Techniques:** Multiple color space conversions, histogram calculation, statistical analysis

### Task 3: Binary Thresholding

- **Type:** Theoretical question
- **Purpose:** Understanding binary thresholding concepts
- **Focus:** Pixel-level thresholding operations

## Development Notes

- All scripts use relative paths and are designed to work regardless of the current working directory
- Images are processed using OpenCV (cv2) for optimal performance
- Matplotlib is used for visualization and plotting
- The project follows Python best practices with proper error handling and documentation
- Each task maintains independence while following consistent coding standards

## Troubleshooting

### Common Issues

1. **"Image file not found" error:**

   - Ensure `photo.jpg` exists in `src/images/original/`
   - Check that you're running the script from the correct directory

2. **Import errors:**

   - Make sure you've activated your virtual environment
   - Verify all dependencies are installed: `pip install -r requirements.txt`

3. **Display issues:**
   - Ensure you have a GUI environment if running on a server
   - For headless environments, consider modifying scripts to save plots instead of displaying them

## Contributing

This is an academic project. For suggestions or improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commit messages
4. Submit a pull request

## License

This project is for educational purposes as part of DCIT 412 - COMPUTER VISION coursework.

---

**Maintained by:** 10990135 - Kongo Prince Kweku  
**Course:** DCIT 412 - Computer Vision  
**Institution:** University of Ghana, Legon  
**Last Updated:** July 2025
