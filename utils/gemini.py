import os 
from dotenv import load_dotenv
import google.generativeai as genai #Genai model 

#keeping ythe data modular
def intialize_model():
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
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    
    except Exception as e:
        print("Error in intializing the model")
        return None

if __name__ == "__main__":
    intialize_model() 