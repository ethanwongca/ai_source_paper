import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from pdf_parser import Grobid

def test_grobid():
    try:
        grobid_handler = Grobid()
        pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'sample.pdf'))
        print(f"PDF path: {pdf_path}")  # Debugging line to verify path
        extracted_text = grobid_handler.parse(pdf_path)
        if extracted_text:
            print("Extracted Text:", extracted_text)
        else:
            print("Failed to extract text from PDF.")
    except Exception as e:
        print(f"Error in test_grobid: {e}")

if __name__ == "__main__":
    test_grobid()
