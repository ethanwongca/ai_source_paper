import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from llama import LLaMA

def test_llama():
    llama_handler = LLaMA(model_path='path/to/your/llama/model')
    response = llama_handler.generate_response("What is the capital of France?")
    print("LLaMA Response:", response)

if __name__ == "__main__":
    test_llama()