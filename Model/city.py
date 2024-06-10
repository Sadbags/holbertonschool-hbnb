from basemodel import BaseModel


class City(BaseModel):
    def __init__(self, name, country, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        self.places.append(place)
