import requests

def extract_bibliographic_data(pdf_path, grobid_url='http://localhost:8070/api/processHeaderDocument'):
    with open(pdf_path, 'rb') as pdf_file:
        response = requests.post(
            grobid_url,
            files={'input': pdf_file},
            headers={'Accept': 'application/xml'}
        )
        
        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()

if __name__ == "__main__":
    # Path to the sample PDF file
    pdf_path = "../tests/sample.pdf"
    
    try:
        # Extract bibliographic data
        extracted_data = extract_bibliographic_data(pdf_path)
        # Print the extracted data
        print(extracted_data)
    except Exception as e:
        print(f"Error extracting bibliographic data: {e}")
