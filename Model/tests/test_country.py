import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

from Model.country import Country  # Import the Country class from your country file
from Model.place import Place  # Assuming Place is defined similarly as before

class TestCountry(unittest.TestCase):
    def test_create_country(self):
        # Test creating a new country
        country = Country(name='Puerto Rico', area_code='00913')
        self.assertEqual(country.name, 'Puerto Rico')
        self.assertEqual(country.area_code, '00913')
        self.assertEqual(country.places, [])

    def test_add_place(self):
        # Test adding a place to the country
        country = Country(name='Puerto Rico', area_code='00913')
        place = Place(name='El Beach House', location='Condado', owner='Glori')
        country.add_place(place)
        self.assertIn(place, country.places)

if __name__ == '__main__':
    unittest.main()
