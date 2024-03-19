import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestTriangle(unittest.TestCase):

    def test_sides(self):

        self.assertEqual(get_triangle_type(10, 10, 10), 'equilateral')
        self.assertEqual(get_triangle_type(5, 10, 5), 'isosceles')
        self.assertEqual(get_triangle_type(7, 8, 9), 'nonequilateral')

        self.assertEqual(get_triangle_type(7.5, 8.2, 9.8), 'nonequilateral')
        self.assertEqual(get_triangle_type(10.5, 8.4, 10.5), 'isosceles')
        self.assertEqual(get_triangle_type(11.8, 11.8, 11.8), 'equilateral')
        self.assertEqual(get_triangle_type(4.8, 7.2, 7.7), 'nonequilateral')

    def test_zero_length_of_sides(self):
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, 0, 10, 5)

    def test_non_int_float_type_of_sides(self):
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, None, 10, 5)
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, [10], 10, 5)
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, '10', 10, 5)

    def test_negative_length_of_side(self):

        self.assertRaises(IncorrectTriangleSides, get_triangle_type, -4, 10, 5)

        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(9.2, -5, 10)

    def test_too_big_length_of_side(self):
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, 28, 10, 5)
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, 18, 34, 14)


if __name__ == '__main__':
    unittest.main()
