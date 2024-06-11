from place import Place
from review import Review
from basemodel import BaseModel

class User(BaseModel):
    """ Represents a user in the system """

    _users = []  # List of users

    def __init__(self, email, first_name="", last_name="", password="", **kwargs):
        """ Initializes a new instance of the User class """
        if any(existing_user.email == email for existing_user in User._users):
            raise ValueError("This email is already in use")

        super().__init__(**kwargs)  # Initialize the BaseModel attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.reviews = []  # List of reviews made by the user
        self.places = []  # List of places owned by the user
        User._users.append(self)  # Add user to list of users

    def create_place(self, name, location):
        """Creates a new place owned by the user."""
        place = Place(name=name, location=location, owner=self)
        self.places.append(place)
        return place

    def create_review(self, title, content, rating, place):
        """Creates a new review written by the user."""
        review = Review(title=title, content=content, rating=rating, author=self, place=place)
        self.reviews.append(review)
        place.add_review(review)
        return review
