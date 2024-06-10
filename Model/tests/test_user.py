import unittest
import sys
import os

# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

# Now you can import the User class.
from Model.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """This method is called before each test"""
        User._users = []  # Reset the list of users

    def test_create_user(self):
        """Test that a user can be created"""
        user = User("test@example.com", "Test", "User", "password")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.password, "password")

    def test_email_uniqueness(self):
        """Test that a user cannot be created with an email that's already in use"""
        User("test@example.com", "Test", "User", "password")
        with self.assertRaises(ValueError):
            User("test@example.com", "Another", "User", "password")

    def test_add_review(self):
        """Test that a review can be added to a user"""
        user = User("test@example.com", "Test", "User", "password")
        review = "This is a review."
        user.reviews.append(review)
        self.assertIn(review, user.reviews)


if __name__ == "__main__":
    unittest.main()
