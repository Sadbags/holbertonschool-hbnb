from basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, Description, Type, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.Description = Description
        self.Type = Type

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
