from Model.basemodel import BaseModel

class Review(BaseModel):
    def __init__(self, place_id, user_id, rating, comment, **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.user_id = user_id

    def __str__(self):
        return f"[Review] ({self.id}) {self.to_dict()}"
