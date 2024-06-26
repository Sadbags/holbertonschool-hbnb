from Model.basemodel import BaseModel

class Place(BaseModel):
    """  Place class that inherits from BaseModel. Represents a rental place with various attributes. """

    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, amenity_ids=[], **kwargs):
        """ Initializes the Place with the given attributes. """
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.price_per_night = price_per_night


    def get_city_id(self):
        return self.city_id

    def __str__(self):
        return f"[Place] ({self.id}) {self.to_dict()}"
