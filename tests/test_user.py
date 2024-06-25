import unittest
import json
from flask import Flask
from Model.user import User
from Persistence.DataManager import DataManager
from API.user import user_bp

class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up Flask test client and add user_bp blueprint
        self.app = Flask(__name__)
        self.app.register_blueprint(user_bp, url_prefix='/api/users')
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

        # Initialize DataManager and clear any existing users
        self.data_manager = DataManager()
        User._users = {}  # Ensure this matches your actual data structure

    def tearDown(self):
        User._users = {}  # Clear any users after each test

    def test_create_user(self):
        response = self.client.post('/api/users/', json={
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_create_user_invalid_email(self):
        response = self.client.post('/api/users/', json={
            'email': 'invalid-email',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.data_manager.save(user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_user(self):
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.data_manager.save(user)
        response = self.client.get(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['email'], 'test@example.com')

    def test_update_user(self):
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.data_manager.save(user)
        response = self.client.put(f'/api/users/{user.id}', json={
            'first_name': 'Jane'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['id'], str(user.id))
        self.assertEqual(user.first_name, 'Jane')

    def test_delete_user(self):
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.data_manager.save(user)
        response = self.client.delete(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get(user.id, User))

if __name__ == '__main__':
    unittest.main()
