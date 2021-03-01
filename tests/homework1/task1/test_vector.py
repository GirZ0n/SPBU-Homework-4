import unittest
from homework.homework1.task1.vector import Vector


class IntegerVectorTestCase(unittest.TestCase):
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


class FloatVectorTestCase(unittest.TestCase):
    def test_dot_same_dimensions(self):
        v1 = Vector(-509.6974, -638.9697, -616.5371, 357.8119)
        v2 = Vector(-296.8781, 552.5954, 581.1951, 48.9870)

        self.assertAlmostEqual(v1.dot(v2), -542573.931215, 6)

    def test_dot_different_dimensions(self):
        v1 = Vector(806.7900, -100.7458, 421.5406)
        v2 = Vector(-484.7214, 679.2637)

        with self.assertRaises(ValueError) as context:
            v1.dot(v2)

        self.assertTrue("The dimensions of the vectors do not match." in str(context.exception))

    def test_norm(self):
        v = Vector(521.1092, 852.9319, 177.5268)

        self.assertAlmostEqual(v.norm(), 1015.16668044)

    def test_angle_same_dimensions_1(self):
        v1 = Vector(-661.1494, 0)
        v2 = Vector(0, -661.1494)

        self.assertAlmostEqual(v1.angle(v2), 90)

    def test_angle_same_dimensions_2(self):
        v1 = Vector(655.9491, -584.2169, -290.9577)
        v2 = Vector(-670.1347, -502.1254, 601.2806)

        self.assertAlmostEqual(v1.angle(v2), 109.675091, 6)

    def test_angle_same_dimensions_3(self):
        v1 = Vector(378.3913, -538.5130, 725.1693)
        v2 = Vector(-881.2465, -881.3062, 671.1265)

        self.assertAlmostEqual(v1.angle(v2), v2.angle(v1))

    def test_angle_different_dimensions(self):
        v1 = Vector(871.1976, 971.7544, 523.3768, 361.4904, -253.9030, 871.7992, -380.6937, -655.0334)
        v2 = Vector(-643.5042, 829.8866)

        with self.assertRaises(ValueError) as context:
            v1.angle(v2)

        self.assertTrue("The dimensions of the vectors do not match." in str(context.exception))
