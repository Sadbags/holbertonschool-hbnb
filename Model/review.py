from Model.basemodel import BaseModel
from database import db

class Review(BaseModel):
    place_id = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.String(60), nullable=False)
    comment = db.Column(db.String(1024), nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    def __init__(self, place_id, user_id, rating, comment, **kwargs):
        super().__init__(**kwargs)
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.user_id = user_id

    def __str__(self):
        return f"[Review] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        return {
            'id': self.id,
            'place_id': self.place_id,
            'user_id': self.user_id,
            'comment': self.comment,
            'rating': self.rating,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
