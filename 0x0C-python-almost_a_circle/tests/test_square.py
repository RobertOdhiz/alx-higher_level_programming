import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_attributes(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 5)

    def test_size_setter_valid(self):
        square = Square(2, 3, 4, 5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.area(), 49)

    def test_size_setter_invalid_type(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_size_setter_invalid_value(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(ValueError):
            square.size = -1

    def test_x_setter_valid(self):
        square = Square(2, 3, 4, 5)
        square.x = 7
        self.assertEqual(square.x, 7)

    def test_x_setter_invalid_type(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            square.x = "invalid"

    def test_x_setter_invalid_value(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(ValueError):
            square.x = -1

    def test_y_setter_valid(self):
        square = Square(2, 3, 4, 5)
        square.y = 7
        self.assertEqual(square.y, 7)

    def test_y_setter_invalid_type(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            square.y = "invalid"

    def test_y_setter_invalid_value(self):
        square = Square(2, 3, 4, 5)
        with self.assertRaises(ValueError):
            square.y = -1

    def test_area(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(square.area(), 4)

    def test_display(self):
        square = Square(2, 3, 4, 5)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch(
                        'sys.stdout', new_callable=io.StringIO
                         ) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        square = Square(2, 3, 4, 5)
        square.update(7, 8, 9, 10)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 9)
        self.assertEqual(square.y, 10)

    def test_str(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (5) 4/5 - 2")

    def test_to_dictionary(self):
        square = Square(2, 3, 4, 5)
        expected_output = {'id': 5, 'size': 2, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
