import os
import sys
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator
from langdetect import detect
from fpdf import FPDF

# Function to create a new folder
def create_processed_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    new_folder_name = f"processed_{folder_name}"
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path

# Function to translate text to English
def translate_text(text, target_language='en'):
    try:
        detected_language = detect(text)
    except:
        detected_language = 'unknown'
    if detected_language != target_language:
        
        translation = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(translation)
        return translation
    return text

# Function to extract and process text and images from a PDF
def process_pdf(pdf_path, output_folder):
    pdf_reader = PdfReader(pdf_path)
    output_pdf_path = os.path.join(output_folder, os.path.basename(pdf_path))
    pdf_writer = FPDF()

    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text() or ""
        translated_text = translate_text(text)

        # Extract text from images using Tesseract
        pages = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1)
        for img_page in pages:
            image_text = pytesseract.image_to_string(img_page)
            translated_image_text = translate_text(image_text)
            translated_text += f"\n{translated_image_text}"

        # Handle encoding to ensure compatibility with PDF generation
        translated_text = translated_text.encode('latin-1', 'replace').decode('latin-1')
        # Create a PDF page with the translated content
        pdf_writer.add_page()
        pdf_writer.set_font("Arial", size=12)
        pdf_writer.multi_cell(0, 10, translated_text)

    # Save the translated PDF
    pdf_writer.output(output_pdf_path)

def process_folder(folder_path):
    output_folder = create_processed_folder(folder_path)
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            process_pdf(pdf_path, output_folder)
    print(f"Processing complete. Translated PDFs saved in: {output_folder}")

# Main function to start processing
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please provide a valid folder path.")
        sys.exit(1)

    process_folder(folder_path)
