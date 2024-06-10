from grobid_client.grobid_client import GrobidClient 

class grobid:
    def __init__(self):
        self.client = GrobidClient(config_path='config.json')
        
    def parse(self, pdf_path):
        response = self.client.process(pdf_path, 'processFulltextDocument')
        return response['text']