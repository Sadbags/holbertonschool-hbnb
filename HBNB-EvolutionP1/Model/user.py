import uuid
from datetime import datetime
from place import Place
from review import Review

class User:
    def __init__(self, email, first_name, last_name):
        self.id = uuid.uuid4()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
        self.reviews = []

    def create_place(self, name, location):
        place = Place(name, location, self)
        self.places.append(place)
        return place

    def create_review(self, rating, content, place):
        review = Review(rating, content, self, place)
        self.reviews.append(review)
        return review