import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        test_list = []
        self.assertEqual(Base.to_json_string(test_list), '[]')

    def test_to_json_string_with_data(self):
        test_list = [{'id': 1, 'width': 2, 'height': 3}]
        expected_output = '[{"id": 1, "width": 2, "height": 3}]'
        self.assertEqual(Base.to_json_string(test_list), expected_output)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, '[]')

    def test_save_to_file_empty(self):
        Rectangle.save_to_file(None)
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 2, "height": 3}]'
        expected_output = [{'id': 1, 'width': 2, 'height': 3}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_create_rectangle(self):
        dictionary = {'id': 1, 'width': 2, 'height': 3}
        obj = Rectangle.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)

    def test_create_square(self):
        dictionary = {'id': 1, 'size': 2}
        obj = Square.create(**dictionary)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)

    def test_load_from_file(self):
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5)])
        objs = Rectangle.load_from_file()
        self.assertTrue(isinstance(objs[0], Rectangle))

    def test_load_from_file_empty(self):
        Square.save_to_file(None)
        objs = Square.load_from_file()
        self.assertEqual(objs, [])


if __name__ == '__main__':
    unittest.main()
