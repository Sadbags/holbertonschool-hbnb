import unittest
import json
from app import app, db, bcrypt
from Model.user import User
from flask_jwt_extended import create_access_token

class UserEndpointsTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()
            self.create_admin_user()

    def tearDown(self):
        """Tear down the test environment."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def create_admin_user(self):
        """Create an admin user for testing."""
        admin_password = bcrypt.generate_password_hash('adminpass').decode('utf-8')
        admin = User(email='admin@example.com', password=admin_password, is_admin=True)
        db.session.add(admin)
        db.session.commit()

    def get_access_token(self, email='admin@example.com', password='adminpass'):
        """Get an access token for the test user."""
        user = User.query.filter_by(email=email).first()
        return create_access_token(identity=user.id, additional_claims={'is_admin': user.is_admin})

    def test_create_user(self):
        """Test creating a new user."""
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'test@example.com')

    def test_create_user_existing_email(self):
        """Test creating a user with an existing email."""
        self.client.post('/users', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 409)

    def test_promote_user(self):
        """Test promoting a user to admin."""
        response = self.client.post('/users', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        data = json.loads(response.data)
        user_id = data['id']

        access_token = self.get_access_token()
        response = self.client.post(f'/users/{user_id}/promote', headers={
            'Authorization': f'Bearer {access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['is_admin'])

    def test_get_users(self):
        """Test retrieving all users."""
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_user(self):
        """Test retrieving a specific user."""
        response = self.client.post('/users', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        data = json.loads(response.data)
        user_id = data['id']

        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'testuser@example.com')

    def test_update_user(self):
        """Test updating a user."""
        response = self.client.post('/users', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        data = json.loads(response.data)
        user_id = data['id']

        access_token = self.get_access_token()
        response = self.client.put(f'/users/{user_id}', headers={
            'Authorization': f'Bearer {access_token}'
        }, json={
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'updated@example.com')

    def test_delete_user(self):
        """Test deleting a user."""
        response = self.client.post('/users', json={
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        data = json.loads(response.data)
        user_id = data['id']

        access_token = self.get_access_token()
        response = self.client.delete(f'/users/{user_id}', headers={
            'Authorization': f'Bearer {access_token}'
        })
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
