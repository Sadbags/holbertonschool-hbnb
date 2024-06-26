from Model.basemodel import BaseModel

class Amenity(BaseModel):
    """ Amenety class that inherits from BaseModel """
    def __init__(self, name, **kwargs):
        """ Initializes the Amenety class with its attributes """
        super().__init__(**kwargs)
        self.name = name


    def __str__(self):
    	return f"[Amenity] ({self.id}) {self.to_dict()}"
