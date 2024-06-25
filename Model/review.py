from Model.basemodel import BaseModel

class Review(BaseModel):
    def __init__(self, rating, content, author, place, **kwargs):
        super().__init__(**kwargs)
        if author == place.owner:
            raise ValueError("The host cannot review their own place")
        self.rating = rating
        self.content = content
        self.author = author
        self.place = place
        place.add_review(self)
