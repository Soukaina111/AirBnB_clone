#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        self.storage.delete_all()

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(self.model.__class__.__name__ + "." + self.model.id, all_objs)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(new_model, self.storage._FileStorage__objects.values())

    def test_save(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        with open(file_path, 'r') as file:
            file_content = file.read()
            self.assertIn(new_model.__class__.__name__ + "." + new_model.id, file_content)

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(self.model.__class__.__name__ + "." + self.model.id, all_objs)

    def test_delete(self):
        model_id = self.model.id
        self.storage.delete(self.model)
        all_objs = self.storage.all()
        self.assertNotIn(self.model.__class__.__name__ + "." + model_id, all_objs)

    def test_delete_all(self):
        self.storage.delete_all()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
