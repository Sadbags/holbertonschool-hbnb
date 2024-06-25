import unittest
import json
from flask import Flask
from API.review_endpoints import review_bp
from Model.user import User
from Model.place import Place
from Model.review import Review
from Persistence.DataManager import DataManager

class ReviewAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(review_bp, url_prefix='/reviews')
        cls.client = cls.app.test_client()
        cls.data_manager = DataManager()
        cls.data_manager.storage.objects = {}

    def setUp(self):
        self.data_manager.storage.objects.clear()
        self.user = User(email='test_user@example.com', first_name='Test', last_name='User', password='password')
        self.place = Place(name='Test Place', location='Test Location', owner=self.user)
        self.data_manager.save(self.user)
        self.data_manager.save(self.place)

    def test_create_review(self):
        review_data = {
            'author_id': str(self.user.id),
            'place_id': str(self.place.id),
            'rating': 5,
            'content': 'Great place!'
        }
        response = self.client.post('/reviews/', data=json.dumps(review_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_reviews(self):
        review = Review(rating=5, content='Great place!', author=self.user, place=self.place)
        self.data_manager.save(review)
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['content'], 'Great place!')

    def test_get_review(self):
        review = Review(rating=5, content='Great place!', author=self.user, place=self.place)
        self.data_manager.save(review)
        response = self.client.get(f'/reviews/{review.id}')
        self.assertEqual(response.status_code, 200)
        review_data = json.loads(response.data)
        self.assertEqual(review_data['content'], 'Great place!')

    def test_update_review(self):
        review = Review(rating=5, content='Great place!', author=self.user, place=self.place)
        self.data_manager.save(review)
        updated_data = {
            'rating': 4,
            'content': 'Good place!'
        }
        response = self.client.put(f'/reviews/{review.id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_review = self.data_manager.get(review.id, Review)
        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.content, 'Good place!')

    def test_delete_review(self):
        review = Review(rating=5, content='Great place!', author=self.user, place=self.place)
        self.data_manager.save(review)
        response = self.client.delete(f'/reviews/{review.id}')
        self.assertEqual(response.status_code, 204)
        deleted_review = self.data_manager.get(review.id, Review)
        self.assertIsNone(deleted_review)

if __name__ == '__main__':
    unittest.main()
