import uuid

class Amenity:
    def __init__(self, name, Description, Type):
        self.id = uuid.uuid4()
        self.name = name
        self.Description = Description
        self.Type = Type

    def add_place(self, place):
        if place not in self.places:
            self.places.append(place)
