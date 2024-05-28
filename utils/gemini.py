import os 
from dotenv import load_dotenv
import google.generativeai as genai #Genai model 

def check_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


#keeping the data modular
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

def prompt_model(model: str, prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("error in prompting model")
        return None

if __name__ == "__main__":
    #running tests since this a utils class 
    model = intialize_model() 
    response = prompt_model(model, "Create lyrics inspired by the band Queen")
    print(response)
