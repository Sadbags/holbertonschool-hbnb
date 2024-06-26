from Model.basemodel import BaseModel


class Country(BaseModel):
    """ Country class that represents a country with a name and an area code. """
    def __init__(self, name, code, **kwargs):
        """ Initializes the Country with attributes id, name, and area code. """
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    def __str__(self):
        return f"[Country] ({self.id}) {self.to_dict()}"
