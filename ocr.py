import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2
import os
import tempfile

def process_image(image_path):

    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Failed to load image at path: {image_path}")
            return None
        cv2.imshow("Debug Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Check if the background is dark by sampling corner brightness
        corners = [gray[0,0], gray[0,-1], gray[-1,0], gray[-1,-1]]
        avg_corner = sum(corners) / 4

        if avg_corner < 127:
            gray = cv2.bitwise_not(gray)
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        text = pytesseract.image_to_string(binary, lang='eng')
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def pdf_to_text(pdf_path):
    """Extract text from a multi-page PDF using OCR on converted images."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            images = convert_from_path(pdf_path, output_folder=temp_dir)
            full_text = ""

            for i, image in enumerate(images):
                image_path = os.path.join(temp_dir, f"page_{i}.png")
                image.save(image_path, "PNG")

                text = process_image(image_path)
                if text:
                    full_text += text + "\n"
                else:
                    full_text += f"[Error on page {i + 1}]\n"
            return full_text
    except Exception as e:
        print(f"An error occurred processing PDF: {e}")
        return None

if __name__ == '__main__':
    file_path = ""  # Path selected by user

    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Select a PDF or Image file",
            filetypes=[("PDF files", "*.pdf"), ("Image files", "*.png;*.jpg;*.jpeg")]
        )
    except ImportError:
        print("tkinter not available. Please provide the file path manually.")
        file_path = input("Enter the path to your PDF or image file: ")
    except tk.TclError:
        print("Unable to open file dialog. Please provide the file path manually.")
        file_path = input("Enter the path to your PDF or image file: ")

    if file_path and os.path.exists(file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            extracted_text = pdf_to_text(file_path)
        elif ext in [".jpg", ".jpeg", ".png"]:
            extracted_text = process_image(file_path)
        else:
            print("Unsupported file type.")
            extracted_text = None

        if extracted_text:
            print("\n--- Extracted Text ---\n")
            print(extracted_text)
        else:
            print("Text extraction failed.")
    else:
        print("No valid file selected or file does not exist.")
