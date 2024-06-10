import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

from Model.review import Review # Import the Review class from your review file

class TestReview(unittest.TestCase):
    def test_create_review(self):
        # Test creating a new review
        review = Review(title='Great experience', content='The place was amazing!', rating=5, author='John Doe', place='Beach House')
        self.assertEqual(review.title, 'Great experience')
        self.assertEqual(review.content, 'The place was amazing!')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.author, 'John Doe')
        self.assertEqual(review.place, 'Beach House')

    def test_update_review(self):
        # Test updating review information
        review = Review(title='Great experience', content='The place was amazing!', rating=5, author='John Doe', place='Beach House')
        review.title = 'Awesome place'
        review.rating = 4
        self.assertEqual(review.title, 'Awesome place')
        self.assertEqual(review.rating, 4)

if __name__ == '__main__':
    unittest.main()
