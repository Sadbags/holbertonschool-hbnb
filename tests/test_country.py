import unittest
import json
from API.countryAPI import app, data_manager
from Model.country import Country

class TestCountryEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = data_manager
        self.data_manager.storage.clear()

    def test_create_country(self):
        response = self.app.post('/countries/', json={
            'name': 'Test Country',
            'code': 'TC'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Country', str(response.data))

    def test_get_countries(self):
        country = Country(name='Test Country', code='TC')
        self.data_manager.save(country)
        response = self.app.get('/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Country', str(response.data))

    def test_get_country(self):
        country = Country(name='Test Country', code='TC')
        self.data_manager.save(country)
        response = self.app.get(f'/countries/{country.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Country', str(response.data))

    def test_update_country(self):
        country = Country(name='Test Country', code='TC')
        self.data_manager.save(country)
        response = self.app.put(f'/countries/{country.id}', json={
            'name': 'Updated Country',
            'code': 'UC'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Country', str(response.data))

    def test_delete_country(self):
        country = Country(name='Test Country', code='TC')
        self.data_manager.save(country)
        response = self.app.delete(f'/countries/{country.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get(country.id, Country))

if __name__ == "__main__":
    unittest.main()
