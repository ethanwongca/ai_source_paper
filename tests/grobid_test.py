import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from pdf_parser import Grobid

def test_grobid():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils', 'config.json'))
    if not os.path.exists(config_path):
        print(f"Config file does not exist: {config_path}")
        return
    grobid_handler = Grobid()  # No need to pass config_path as it is handled inside the class
    pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'sample.pdf'))
    extracted_text = grobid_handler.parse(pdf_path)
    print("Extracted Text:", extracted_text)

if __name__ == "__main__":
    test_grobid()
