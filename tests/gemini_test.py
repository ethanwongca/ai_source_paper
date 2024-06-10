import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from gemini import Gemini

def test_gemini():
    gemini_handler = Gemini()
    if not gemini_handler.model:
        print("Failed to initialize Gemini model.")
        return
    response = gemini_handler.prompt_model("Create lyrics inspired by the band Queen")
    print("Gemini Response:", response)

if __name__ == "__main__":
    test_gemini()
