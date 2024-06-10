from basemodel import BaseModel


class City(BaseModel):
    def __init__(self, name, country, places, city, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.country = country
        self.city = city
        self.places = places

    def add_place(self, place):
        self.places.append(place)
