import os
import sys
from langchain_community.document_loaders import PyPDFLoader
import json
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from models.crew.crew_pool import analyse_cv
from mongo_utils import creation_profil
#############################################################

def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    cv_text = ""
    for page in pages:
        cv_text += page.page_content + "\n\n"
    return cv_text

pdf_path = r'data\CV-test.pdf'
json_path = r'data\cv_profile.json'
cv_text = load_pdf(pdf_path)


if __name__ == "__main__":
    chemin_cv = pdf_path 
    cv_text_content = load_pdf(chemin_cv)
    analyse_cv(cv_text_content)
    cv_json = json_path 
    creation_profil(cv_json)
    print("Le traitement du CV est terminé.")
