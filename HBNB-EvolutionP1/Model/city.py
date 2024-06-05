import uuid

class city:
    def __init__(self,name, country):
        self.id = uuid.uuid4()
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        self.places.append(place)
