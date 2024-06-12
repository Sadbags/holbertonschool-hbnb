from basemodel import BaseModel

class Place(BaseModel):
    """  Place class that inherits from BaseModel. Represents a rental place with various attributes. """
    def __init__(self, name, location, owner, description="", address="", city=None, latitude="", longitude="", price_per_night=0, **kwargs):
        """ Initializes the Place with the given attributes. """
        super().__init__(**kwargs)
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

    def add_review(self, review):
        """  Adds a review to the list of reviews for the place. """
        self.reviews.append(review)

    def add_amenities(self, amenity):
        """ Adds an amenity to the list of amenities for the place. """
        self.amenities.append(amenity)
