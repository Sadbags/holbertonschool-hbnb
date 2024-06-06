from place import Place
from review import Review
from basemodel import BaseModel

class User(BaseModel):
    def __init__(self, email, password, first_name, last_name,**kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
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
