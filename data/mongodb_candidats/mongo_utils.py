import os
import json
from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoManager:
    def __init__(self, db_name="cv_candidats", collection_name="cv"):
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            raise ValueError("La variable d'environnement MONGO_URI n'est pas définie.")
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_document_by_id(self, document_id: str):
        if not ObjectId.is_valid(document_id):
            raise ValueError(f"ID MongoDB invalide : {document_id}")
        return self.collection.find_one({"_id": ObjectId(document_id)})

    def save_profile(self, profile_data: dict):
        try:
            result = self.collection.insert_one(profile_data)
            print(f"Profil sauvegardé avec l'ID : {result.inserted_id}")
        except Exception as e:
            print(f"Erreur MongoDB lors de l'insertion : {e}")

    def create_profile_from_json(self, json_path: str):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'candidat' in data:
                    self.save_profile(data['candidat'])
                else:
                    print("Erreur : Le JSON ne contient pas la clé 'candidat'.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier JSON '{json_path}' est introuvable.")
        except json.JSONDecodeError as e:
            print(f"Erreur JSON dans le fichier '{json_path}' : {e}")

    def close(self):
        self.client.close()
