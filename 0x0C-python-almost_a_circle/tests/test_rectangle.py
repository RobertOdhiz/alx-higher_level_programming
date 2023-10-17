import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 6)

    def test_width_setter_valid(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r.width = 7
        self.assertEqual(r.width, 7)
        self.assertEqual(r.area(), 21)

    def test_width_setter_invalid_type(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_width_setter_invalid_value(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            r.width = -1

    def test_height_setter_valid(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r.height = 7
        self.assertEqual(r.height, 7)
        self.assertEqual(r.area(), 14)

    def test_height_setter_invalid_type(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_height_setter_invalid_value(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_setter_valid(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r.x = 7
        self.assertEqual(r.x, 7)

    def test_x_setter_invalid_type(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r.x = "invalid"

    def test_x_setter_invalid_value(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter_valid(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r.y = 7
        self.assertEqual(r.y, 7)

    def test_y_setter_invalid_type(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test_y_setter_invalid_value(self):
        r = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 3, 4, 5, 6)
        expected_output = "####\n####\n####\n"
        with unittest.mock.patch(
                         'sys.stdout', new_callable=io.StringIO
                          ) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(2, 3, 4, 5, 6)
        r.update(7, 8, 9, 10, 11)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 11)

    def test_str(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_to_dictionary(self):
        r = Rectangle(2, 3, 4, 5, 6)
        expected_output = {'id': 6, 'x': 4, 'y': 5, 'width': 2, 'height': 3}
        self.assertEqual(r.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
