from basemodel import BaseModel

class Place(BaseModel):
    """  Place class that inherits from BaseModel. Represents a rental place with various attributes. """
    _places_hosts = {}

    def __init__(self, name, location, owner, description="", address="", city=None, latitude="", longitude="", price_per_night=0, **kwargs):
        """ Initializes the Place with the given attributes. """
        super().__init__(**kwargs)
        if self.__class__._places_hosts.get(name):
            raise ValueError("This place already has a host assigned.")
        
        self.name = name
        self.location = location
        self.owner = owner
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_night = price_per_night
        self.reviews = []
        self.amenities = []

        #Asignar el anfitrión al lugar
        self.__class__._places_hosts[name] = owner

    def add_review(self, review):
        """  Adds a review to the list of reviews for the place. """
        self.reviews.append(review)

    def add_amenities(self, amenity):
        """ Adds an amenity to the list of amenities for the place. """
        self.amenities.append(amenity)

    @classmethod
    def clear_places_hosts(cls):
        """ Clears the places hosts mapping. Useful for testing. """
        cls._places_hosts.clear()
