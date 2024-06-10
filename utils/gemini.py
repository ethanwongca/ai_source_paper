import os 
from dotenv import load_dotenv
import google.generativeai as genai #Genai model 

#checks models available via Gemini API 
class Gemini:
    def __init__(self):
        self.model = self.initialize_model()
    #initialize the model
    def intialize_model(self):
        try:
            #loading the environment from the .env file 
            load_dotenv()
            gemini_api_key = os.getenv("API_KEY")
            #we still need to get the variables as well
            if not gemini_api_key:
                print("API key missing, add it to .env")
                return None
            #intializing the model
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel('gemini-pro')
            return model
        
        except Exception as e:
            print("Error in intializing the model")
            return None

    #prompts the model
    def prompt_model(self, prompt: str) -> str:
        try:
            response = self.generate_content(prompt)
            return response.text
        except Exception as e:
            print("error in prompting model")
            return None
