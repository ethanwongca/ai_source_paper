from llama_cpp import Llama

class LLaMA:
    def __init__(self, model_path):
        self.llama = Llama(model_path=model_path)
    
    def generate_response(self, prompt):
        return self.llama(prompt)
