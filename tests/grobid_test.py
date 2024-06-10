import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from grobid import Grobid

def test_grobid():
    grobid_handler = Grobid()
    pdf_path = 'tests/data/sample.pdf'
    extracted_text = grobid_handler.parse(pdf_path)
    print("Extracted Text:", extracted_text)

if __name__ == "__main__":
    test_grobid()
