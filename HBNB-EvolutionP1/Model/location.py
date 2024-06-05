import uuid

class Location:
    def __init__(self, city, state, country, latitude, longitude):
        self.id = uuid.uuid4()
        self.city = city
        self.state = state
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
