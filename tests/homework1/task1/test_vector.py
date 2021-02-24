import unittest
from homework.homework1.task1.vector import Vector


class VectorTestCase(unittest.TestCase):
    def test_constructor_zero_length(self):
        with self.assertRaises(ValueError) as context:
            Vector()

        self.assertTrue("The vector must contain at least one element." in str(context.exception))

    def test_dot_same_dimensions(self):
        v1 = Vector(5, 2, 7, 9)
        v2 = Vector(4, 2, 1, 7)

        self.assertEqual(v1.dot(v2), 94)

    def test_dot_different_dimensions(self):
        v1 = Vector(1, 2, 42)
        v2 = Vector(6, 6)

        with self.assertRaises(ValueError) as context:
            v1.dot(v2)

        self.assertTrue("The dimensions of the vectors do not match." in str(context.exception))

    def test_norm(self):
        v = Vector(6, 10, 15)

        self.assertAlmostEqual(v.norm(), 19)

    def test_angle_same_dimensions_1(self):
        v1 = Vector(1, 0)
        v2 = Vector(0, 1)

        self.assertAlmostEqual(v1.angle(v2), 90)

    def test_angle_same_dimensions_2(self):
        v1 = Vector(24, 1, 88)
        v2 = Vector(2, 4, 35)

        self.assertAlmostEqual(v1.angle(v2), 13.3242, 4)

    def test_angle_same_dimensions_3(self):
        v1 = Vector(24, 1, 88)
        v2 = Vector(2, 4, 35)

        self.assertAlmostEqual(v1.angle(v2), v2.angle(v1))

    def test_angle_different_dimensions(self):
        v1 = Vector(1, 2, 3, 4, 5, 6, 7, 8)
        v2 = Vector(9, 0)

        with self.assertRaises(ValueError) as context:
            v1.angle(v2)

        self.assertTrue("The dimensions of the vectors do not match." in str(context.exception))
