class Country():
    """ Country class that represents a country with a name and an area code. """
    def __init__(self, name, area_code):
        """ Initializes the Country with attributes name and area code. """
        self.name = name
        self.area_code = area_code
        self.places = []


    def add_place(self, place):
        """ Adds a place to the list of places associated with the country. """
        self.places.append(place)
