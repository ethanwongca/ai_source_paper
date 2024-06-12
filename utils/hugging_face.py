import torch 
import transformers 

def test_model():
    model_id = 'meta-llama/Meta-Llama-3-8B'
    pipeline = transformers.pipeline(
    "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)
    response = pipeline("What is the capital of France?")   
    print(response)

if __name__ == "__main__":
    test_model()
