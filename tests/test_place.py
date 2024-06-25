import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

from Model.place import Place  # Import the Place class from your place file

class TestPlace(unittest.TestCase):
    def test_create_place(self):
        # Test creating a new place
        place = Place(name='El Beach House', location='Condado', owner='Glori', description='Una bella casa frente a la playa con una vista espectacular', address='2168 Park Blvd', city='San Juan', price_per_night=150)
        self.assertEqual(place.name, 'El Beach House')
        self.assertEqual(place.location, 'Condado')
        self.assertEqual(place.owner, 'Glori')
        self.assertEqual(place.description, 'Una bella casa frente a la playa con una vista espectacular')
        self.assertEqual(place.address, '2168 Park Blvd')
        self.assertEqual(place.city, 'San Juan')
        self.assertEqual(place.latitude, "")
        self.assertEqual(place.longitude, "")
        self.assertEqual(place.price_per_night, 150)
        self.assertEqual(place.reviews, [])
        self.assertEqual(place.amenities, [])

    def test_add_review(self):
        # Test adding a review to the place
        place = Place(name='El Beach House', location='Condado', owner='Glori')
        review = "Beautiful view and great amenities!"
        place.add_review(review)
        self.assertIn(review, place.reviews)

    def test_add_amenities(self):
        # Test adding amenities to the place
        place = Place(name='EL Beach House', location='Condado', owner='Glori')
        amenity = "Wi-Fi"
        place.add_amenities(amenity)
        self.assertIn(amenity, place.amenities)

if __name__ == '__main__':
    unittest.main()
