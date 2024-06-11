import json
import os
from IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _get_file_path(self, entity_id, entity_type):
        return os.path.join(self.directory, f"{entity_type}_{entity_id}.json")

    def save(self, entity):
        file_path = self._get_file_path(entity.id, type(entity).__name__)
        with open(file_path, 'w') as f:
            json.dump(entity.__dict__, f, default=str)

    def get(self, entity_id, entity_type):
        file_path = self._get_file_path(entity_id, entity_type)
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data

    def update(self, entity):
        self.save(entity)


    def delete(self, entity_id, entity_type):
        file_path = self._get_file_path(entity_id, entity_type)
        if os.path.exists(file_path):
            os.remove(file_path)
