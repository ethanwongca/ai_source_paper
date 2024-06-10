import os 
from dotenv import load_dotenv
import google.generativeai as genai

class Gemini:
    def __init__(self):
        self.model = self.initialize_model()
    
    def initialize_model(self):
        try:
            load_dotenv()
            gemini_api_key = os.getenv("API_KEY")
            if not gemini_api_key:
                print("API key missing, add it to .env")
                return None
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            print("Model initialized successfully")
            return model
        except Exception as e:
            print("Error in initializing the model:", e)
            return None

    def prompt_model(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print("Error in prompting model:", e)
            return None
