import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from llama import Llama

def test_llama():
    llama_handler = Llama()
    response = llama_handler.prompt("What is the capital of France?")
    print("LLaMA Response:", response)

if __name__ == "__main__":
    test_llama()