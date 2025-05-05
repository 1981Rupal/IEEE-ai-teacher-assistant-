# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# import cv2
# import os
# import tempfile
# import tkinter as tk
# from tkinter import filedialog

# def pdf_to_text(pdf_path):
#     """
#     Extracts text from a PDF file, handling various scenarios and improving robustness.

#     Args:
#         pdf_path (str): The path to the PDF file.

#     Returns:
#         str: The extracted text, or None if an error occurs.
#     """

#     try:
#         # 1. PDF Handling: Convert PDF to images
#         with tempfile.TemporaryDirectory() as temp_dir:  # Create a temporary directory
#             images = convert_from_path(pdf_path, output_folder=temp_dir)
            
#             full_text = ""

#             for i, image in enumerate(images):
#                 # Save each page as an image in the temporary directory
#                 image_path = os.path.join(temp_dir, f"page_{i}.png")
#                 image.save(image_path, "PNG")

#                 # 2. Image Preprocessing (more robust)
#                 img = cv2.imread(image_path)
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 # Apply adaptive thresholding to handle varying lighting
#                 thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#                                             cv2.THRESH_BINARY_INV, 11, 2)

#                 # 3, 4, 5. Text Localization, Character Segmentation, and Recognition
#                 try:
#                     text = pytesseract.image_to_string(thresh)
#                     full_text += text + "\n"
#                 except pytesseract.TesseractError as e:
#                     print(f"Tesseract error on page {i + 1}: {e}")
#                     full_text += f" [Error on page {i + 1}] \n"  # Indicate error in output
            
#             return full_text

#     except Exception as e:
#         print(f"An error occurred processing {pdf_path}: {e}")
#         return None  # Return None to indicate failure

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window

#     pdf_file = filedialog.askopenfilename(title="Select a PDF file", 
#                                             filetypes=[("PDF files", "*.pdf")])

#     if pdf_file:
#         extracted_text = pdf_to_text(pdf_file)
#         if extracted_text:
#             print("--- Extracted Text ---")
#             print(extracted_text)
#         else:
#             print("Text extraction failed.")
#     else:
#         print("No file selected.")

# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# import cv2
# import os
# import tempfile
# import tkinter as tk  # Keep the import, but use it conditionally
# from tkinter import filedialog

# def pdf_to_text(pdf_path):
#     """
#     Extracts text from a PDF file, handling various scenarios and improving robustness.

#     Args:
#         pdf_path (str): The path to the PDF file.

#     Returns:
#         str: The extracted text, or None if an error occurs.
#     """

#     try:
#         # 1. PDF Handling: Convert PDF to images
#         with tempfile.TemporaryDirectory() as temp_dir:  # Create a temporary directory
#             images = convert_from_path(pdf_path, output_folder=temp_dir)
            
#             full_text = ""

#             for i, image in enumerate(images):
#                 # Save each page as an image in the temporary directory
#                 image_path = os.path.join(temp_dir, f"page_{i}.png")
#                 image.save(image_path, "PNG")

#                 # 2. Image Preprocessing (more robust)
#                 img = cv2.imread(image_path)
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 # Apply adaptive thresholding to handle varying lighting
#                 thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#                                             cv2.THRESH_BINARY_INV, 11, 2)

#                 # 3, 4, 5. Text Localization, Character Segmentation, and Recognition
#                 try:
#                     text = pytesseract.image_to_string(thresh)
#                     full_text += text + "\n"
#                 except pytesseract.TesseractError as e:
#                     print(f"Tesseract error on page {i + 1}: {e}")
#                     full_text += f" [Error on page {i + 1}] \n"  # Indicate error in output
                
#             return full_text

#     except Exception as e:
#         print(f"An error occurred processing {pdf_path}: {e}")
#         return None  # Return None to indicate failure

# if __name__ == '__main__':
#     try:
#         root = tk.Tk()
#         root.withdraw()  # Hide the main window

#         pdf_file = filedialog.askopenfilename(title="Select a PDF file", 
#                                             filetypes=[("PDF files", "*.pdf")])
#     except tk.TclError:
#         # Handle the case where tkinter fails (headless environment)
#         print("Unable to open file dialog. Please enter the PDF file path manually.")
#         pdf_file = input("Enter the path to your PDF file: ")

#     if pdf_file:
#         extracted_text = pdf_to_text(pdf_file)
#         if extracted_text:
#             print("--- Extracted Text ---")
#             print(extracted_text)
#         else:
#             print("Text extraction failed.")
#     else:
#         print("No file selected.")

import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import os
import tempfile

def pdf_to_text(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text, or None if an error occurs.
    """

    try:
        # 1. PDF Handling: Convert PDF to images
        with tempfile.TemporaryDirectory() as temp_dir:  # Create a temporary directory
            images = convert_from_path(pdf_path, output_folder=temp_dir)
            
            full_text = ""

            for i, image in enumerate(images):
                # Save each page as an image in the temporary directory
                image_path = os.path.join(temp_dir, f"page_{i}.png")
                image.save(image_path, "PNG")

                # 2. Image Preprocessing (more robust)
                img = cv2.imread(image_path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # Apply adaptive thresholding to handle varying lighting
                thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY_INV, 11, 2)

                # 3, 4, 5. Text Localization, Character Segmentation, and Recognition
                try:
                    text = pytesseract.image_to_string(thresh)
                    full_text += text + "\n"
                except pytesseract.TesseractError as e:
                    print(f"Tesseract error on page {i + 1}: {e}")
                    full_text += f" [Error on page {i + 1}] \n"  # Indicate error in output
            
            return full_text

    except Exception as e:
        print(f"An error occurred processing {pdf_path}: {e}")
        return None  # Return None to indicate failure

if __name__ == '__main__':
    pdf_file = ""  # Initialize pdf_file

    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        pdf_file = filedialog.askopenfilename(title="Select a PDF file from your local system", 
                                                filetypes=[("PDF files", "*.pdf")])
    except ImportError:
        print("tkinter is not available. Please provide the PDF file path manually.")
        pdf_file = input("Enter the path to your PDF file: ")
    except tk.TclError:
        print("Unable to open file dialog. Please provide the PDF file path manually.")
        pdf_file = input("Enter the path to your PDF file: ")

    if pdf_file:
        if os.path.exists(pdf_file):
            extracted_text = pdf_to_text(pdf_file)
            if extracted_text:
                print("--- Extracted Text ---")
                print(extracted_text)
            else:
                print("Text extraction failed.")
        else:
            print(f"Error: File not found at {pdf_file}")
    else:
        print("No file selected.")