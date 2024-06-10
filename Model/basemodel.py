import uuid
from datetime import datetime


class BaseModel():
    def __init__(self, **kwargs):
        """ initializes a new instance of the BaseModel class """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """ updates the updated_at attribute with the current datetime """
        self.updated_at = datetime.now()
