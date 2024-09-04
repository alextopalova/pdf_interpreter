# Use the official Python 3.12 image as the base image
FROM python:3.12-slim

# Set the working directory to the root of the container
WORKDIR /

# Install system dependencies required for pdf2image and pytesseract
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install pytesseract pdf2image PyPDF2 deep-translator langdetect fpdf

# Copy the Python script to the container
COPY process_docs.py /process_docs.py

# Set the entrypoint for the container
ENTRYPOINT ["python", "process_docs.py"]
