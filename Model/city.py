from Model.basemodel import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel """
    def __init__(self, name, country, **kwargs):
        """ Initializes the city with name, country and additional attributes """
        super().__init__(**kwargs)
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        """ Adds a place to the list of places associated with the city class """
        self.places.append(place)
