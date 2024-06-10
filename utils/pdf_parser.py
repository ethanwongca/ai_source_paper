from grobid_client.grobid_client import GrobidClient
import os

class Grobid:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        print(f"Config path: {config_path}")  # Debugging line to verify path
        self.client = GrobidClient(config_path=config_path)
        
    def parse(self, pdf_path):
        response = self.client.process("processFulltextDocument", pdf_path)
        return response['text']
