import transformers as tf
import torch

class Llama:
    def __init__(self):
        self.model_id = 'meta-llama/Meta-Llama-3-8B'
        self.pipeline = tf.pipeline(
            "text-generation", model=self.model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
        )
    def prompt(self, prompt: str) -> str:
        return self.pipeline(prompt)