from Model.basemodel import BaseModel

class Amenity(BaseModel):
    """ Amenety class that inherits from BaseModel """
    def __init__(self, name, Description, type, **kwargs):
        """ Initializes the Amenety class with its attributes """
        super().__init__(**kwargs)
        self.name = name
        self.Description = Description
        self.type = type
        self.places = []

    def add_place(self, place):
        """ adds place to the list of places associated with the amenety """
        if place not in self.places:
            self.places.append(place)
