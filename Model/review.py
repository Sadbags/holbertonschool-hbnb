import uuid
from datetime import datetime

class Review:
    def __init__(self, rating, content, author, place):
        sel.id = uuid.uuid4()
        self.rating = rating
        self.content = content
        self.author = author
        self.place = place
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
