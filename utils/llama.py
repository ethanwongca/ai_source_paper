import subprocess
import os

def initialize_llama():
    # No need to clone or compile every time, assume it's done
    print("LLaMA model initialized successfully.")

def generate_prompt(prompt):
    # Run the llama.cpp binary from the project directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    llama_cpp_path = os.path.join(script_dir, 'llama.cpp', 'main')
    model_path = os.path.join(script_dir, 'llama.cpp', 'models', 'llama-7B', 'ggml-model.bin')
    
    result = subprocess.run(
        [llama_cpp_path, '-m', model_path, '-p', prompt],
        capture_output=True, text=True
    )
    return result.stdout

if __name__ == "__main__":
    initialize_llama()
    response = generate_prompt("Can you tell me a joke?")
    print(response)
