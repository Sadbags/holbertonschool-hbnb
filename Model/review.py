from basemodel import BaseModel

class Review(BaseModel):
    def __init__(self, rating, content, author, place, **kwargs):
        super().__init__(**kwargs)
        self.rating = rating
        self.content = content
        self.author = author
        self.place = place

