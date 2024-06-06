

class Country():
    def __init__(self, name, area_code):
        self.name = name
        self.area_code = area_code
        self.places = []


    def add_place(self, place):
        self.places.append(place)
