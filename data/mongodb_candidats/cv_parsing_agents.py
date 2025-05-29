import os
import sys
from langchain_community.document_loaders import PyPDFLoader
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from models.crew.crew_pool import analyse_cv
from models.config import load_pdf
from data.mongodb_candidats.mongo_utils import MongoManager
manager = MongoManager()

class CvParserAgent:
    def __init__(self, pdf_path: str, json_path: str):
        self.pdf_path = pdf_path
        self.json_path = json_path

    def process(self) -> str:
        print(f"Début du traitement du CV : {self.pdf_path}")
        cv_text_content = load_pdf(self.pdf_path)
        analyse_cv(cv_text_content)
        manager.create_profile_from_json(self.json_path)
        return self.json_path

if __name__ == "__main__":
    pdf_file = r'data\CV - Quentin Loumeau.pdf'
    json_file = r'data\cv_profile.json'
    cv_agent = CvParserAgent(pdf_file, json_file)
    json_output_path = cv_agent.process()