import os
import sys
import json
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URI = os.getenv('MONGO_URI')
mongo_client = MongoClient(MONGO_URI)

def get_mongo_collection():
    client = mongo_client
    db = client["cv_candidats"]
    collection = db["cv"]
    return client, collection

def fetch_document_by_id(collection, document_id: str):
    if not ObjectId.is_valid(document_id):
        raise ValueError(f"ID MongoDB invalide : {document_id}")
    object_id = ObjectId(document_id)
    document = collection.find_one({"_id": object_id})
    return document

def sauvegarder_profil_mongodb(profile_data):
    try:
        client = mongo_client
        db = client['cv_candidats']
        collection = db['cv']
        insertion_result = collection.insert_one(profile_data)
        print(f"Profil sauvegardé avec l'ID : {insertion_result.inserted_id}")
        client.close()
    except Exception as e:
        print(f"Erreur MongoDB : {e}")

def creation_profil(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            candidat_data = json.load(f)
            if 'candidat' in candidat_data:
                sauvegarder_profil_mongodb(candidat_data['candidat'])
            else:
                print("Erreur : Le JSON ne contient pas les clés 'profile' ou 'candidat' attendues.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier JSON '{json_path}' n'a pas été trouvé.")
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la décodage JSON du fichier '{json_path}': {e}")