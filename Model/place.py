import uuid
from datetime import datetime

class Place:
    def __init__(self, name, location, owner):
        self.id = uuid.uuid4()
        self.name = name
        self.location = location
        self.owner = owner
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()

    def add_amenities(self, amenity):
        self.amenities.append(amenity)
        self.updated_at = datetime.now()
