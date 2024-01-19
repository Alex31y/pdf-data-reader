# PDF-to-Text Extractor

## Overview

Welcome to the PDF-to-Text Extractor repository! This application is designed to efficiently extract text from PDF files and to be run locally, without the need for hyperscalers or cloud services.


1. **Convert PDF to Image**: PDF files often have messy structures, making direct text extraction challenging. To overcome this, we convert the PDF into images, simplifying the data representation.
2. 

3. **Text Extraction from Image**: Leveraging the power of Tesseract OCR, the application then extracts text from the generated images. Tesseract is an optical character recognition engine that is adept at recognizing text from images.
4. https://github.com/tesseract-ocr/tesseract

5. **Language Model Invocation**: The extracted text is passed through a Language Model (LLM) to retrieve relevant information. This step enhances the accuracy and usefulness of the extracted data.
6. https://huggingface.co/timpal0l/mdeberta-v3-base-squad2

