from datetime import datetime, timedelta
import requests


JOB_OFFER_CACHE = {}

class CacheManager:
    def __init__(self, expiration_time=timedelta(hours=1)):
        self.cache = JOB_OFFER_CACHE
        self.expiration_time = expiration_time

    def get(self, key):
        cached_data = self.cache.get(key)
        if cached_data and "timestamp" in cached_data and datetime.now() - cached_data["timestamp"] < self.expiration_time:
            return cached_data["data"]
        return None

    def set(self, key, data):
        self.cache[key] = {"data": data, "timestamp": datetime.now()}

    def clear(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear_all(self):
        self.cache.clear()

job_offer_cache_manager = CacheManager()

def load_job_offer_from_api(api_offre, offre_emploi_id: str):
    cached_data = job_offer_cache_manager.get(offre_emploi_id)
    if cached_data:
        return cached_data["entreprise"], cached_data["poste"], cached_data["description"]
    else:
        api_url = f"{api_offre}{offre_emploi_id}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            entreprise = data.get("entreprise")
            poste = data.get("poste")
            description = data.get("description_poste")  # Corrected key here
            job_offer_cache_manager.set(offre_emploi_id, {"entreprise": entreprise, "poste": poste, "description": description})
            return entreprise, poste, description
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération de l'offre d'emploi depuis l'API : {e}")
            return None, None, None