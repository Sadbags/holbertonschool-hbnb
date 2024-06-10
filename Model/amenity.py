from basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, Description, type, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.Description = Description
        self.type = type
        self.places = []

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
