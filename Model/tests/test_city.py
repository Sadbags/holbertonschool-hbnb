import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

from Model.city import City  # Import the City class from your city file
from Model.place import Place  # Assuming Place is defined similarly as before

class TestCity(unittest.TestCase):
    def test_create_city(self):
        # Test creating a new city
        city = City(name='San Juan', country='Puerto Rico')
        self.assertEqual(city.name, 'San Juan')
        self.assertEqual(city.country, 'Puerto Rico')
        self.assertEqual(city.places, [])

    def test_add_place(self):
        # Test adding a place to the city
        city = City(name='San Juan', country='Puerto Rico')
        place = Place(name='El Beach House', location='Condado', owner='Glori')
        city.add_place(place)
        self.assertIn(place, city.places)
        self.assertEqual(len(city.places), 1)

if __name__ == '__main__':
    unittest.main()
