from Model.basemodel import BaseModel
from database import db

class Country(BaseModel):
    name = db.Column(db.String(128), nullable=False)
    country_code = db.Column(db.String(2), unique=True, nullable=False)

    """ Country class that represents a country with a name and an area code. """
    def __init__(self, name, country_code, **kwargs):
        """ Initializes the Country with attributes id, name, and area code. """
        super().__init__(**kwargs)
        self.name = name
        self.country_code = country_code

    def __str__(self):
        return f"[Country] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_code': self.country_code,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            }
