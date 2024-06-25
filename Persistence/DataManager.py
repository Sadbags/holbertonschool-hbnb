import uuid

class DataManager:
    def __init__(self, directory=None):
        self.directory = directory
        self.storage = {'objects': {}}

    def save(self, obj):
        if not obj.id:
            obj.id = str(uuid.uuid4())
        self.storage['objects'][obj.id] = obj

    def get(self, obj_id, obj_type):
        obj = self.storage['objects'].get(obj_id)
        return obj if isinstance(obj, obj_type) else None

    def delete(self, obj_id, obj_type):
        obj = self.storage['objects'].get(obj_id)
        if obj and isinstance(obj, obj_type):
            del self.storage['objects'][obj_id]
            return True
        return False

    def update(self, obj):
        self.storage['objects'][obj.id] = obj
