import requests
import os

class Grobid:
    def __init__(self):
        self.server_url = "http://localhost:8070"
        self.is_alive_url = f"{self.server_url}/api/isalive"
        self.process_url = f"{self.server_url}/api/processFulltextDocument"
        self.test_server_connection()

    def test_server_connection(self):
        try:
            response = requests.get(self.is_alive_url, proxies={"http": None, "https": None})
            if response.status_code == 200:
                print("GROBID server is up and running.")
            else:
                print(f"Unexpected status code: {response.status_code}")
                raise Exception("GROBID server is not responding correctly.")
        except Exception as e:
            print(f"Error connecting to GROBID server: {e}")
            raise Exception("GROBID server connection failed.")

    def parse(self, pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            files = {'input': pdf_file}
            try:
                response = requests.post(self.process_url, files=files, proxies={"http": None, "https": None})
                if response.status_code == 200:
                    return response.text
                else:
                    print(f"Unexpected status code: {response.status_code}")
                    return None
            except Exception as e:
                print(f"Error in parsing PDF: {e}")
                return None

