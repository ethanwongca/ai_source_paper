import transformers as ts
import torch 
import os 
from dotenv import load_dotenv

def initialize_llama(token: str):
    try:
        model_id = "meta-llama/Meta-Llama-3-8B"
        pipe = ts.pipeline(
            "text-generation",
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            use_auth_token=token,
            device="cuda" if torch.cuda.is_available() else "cpu",
        )
        return pipe
    except Exception as e:
        print("Error in initializing the model")
        return None

if __name__ == "__main__":
    initialize_llama()
