from Model.basemodel import BaseModel
from database import db

class Country(BaseModel):
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(2), nullable=False)

    """ Country class that represents a country with a name and an area code. """
    def __init__(self, name, code, **kwargs):
        """ Initializes the Country with attributes id, name, and area code. """
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    def __str__(self):
        return f"[Country] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            }
