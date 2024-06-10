import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

from Model.amenity import Amenity
from Model.place import Place  # Assuming Place is defined similarly as before

class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        # Test creating a new amenity
        amenity = Amenity(name='Pool', Description='Swimming Pool', type='Indoor')
        self.assertEqual(amenity.name, 'Pool')
        self.assertEqual(amenity.Description, 'Swimming Pool')
        self.assertEqual(amenity.type, 'Indoor')
        self.assertEqual(amenity.places, [])

    def test_add_place(self):
        # Test adding a place to the amenity
        amenity = Amenity(name='Pool', Description='Swimming Pool', type='Indoor')
        place = Place(name='El Beach House', location='Condado', owner='Glori')
        amenity.add_place(place)
        self.assertIn(place, amenity.places)
        self.assertEqual(len(amenity.places), 1)

if __name__ == '__main__':
    unittest.main()
