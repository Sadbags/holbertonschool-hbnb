import uuid

class Amenity:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.places = []

        def add_place(self, place):
            if place not in self.places:
                self.places.append(place)
