import uuid
from datetime import datetime

class User:

    def __init__(self, email, first_name="", last_name="", password=""):
        if any(existing_user.email == email for existing_user in User._users):
            raise ValueError("This email is already in use")
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.places = []
        User._users.append(self)
