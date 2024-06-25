import unittest
import sys
import os
import uuid
from datetime import datetime
from Model.basemodel import BaseModel
# Get the directory that contains the current script.
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory.
parent_directory = os.path.dirname(current_directory)

# Add the parent directory to the Python path.
sys.path.append(parent_directory)

class TestBaseModel(unittest.TestCase):

    def test_basemodel_instantiation(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, uuid.UUID)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)  # They should be exactly the same

    def test_save_method(self):
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_kwargs_instantiation(self):
        kwargs = {'name': 'TestName', 'number': 42}
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.name, 'TestName')
        self.assertEqual(base_model.number, 42)

if __name__ == '__main__':
    unittest.main()
