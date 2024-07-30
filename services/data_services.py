# data_services.py

from data import companies_services_products

class DataService:
    def fetch_data(self, identifier):
        results = [item for item in companies_services_products if identifier.lower() in item["name"].lower()]
        return results[0] if results else None
