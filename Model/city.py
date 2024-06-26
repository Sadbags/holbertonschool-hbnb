from Model.basemodel import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel """
    def __init__(self, name, country_code, **kwargs):
        """ Initializes the city with name, country and additional attributes """
        super().__init__(**kwargs)
        self.name = name
        self.country_code = country_code

    def __str__(self):
        return f"[City] ({self.id}) {self.to_dict()}"
