import unittest
from functools import reduce
from homework.homework2.task1.curry import curry_explicit


def const() -> int:
    return 42


class ZeroArgumentsCurryTestCase(unittest.TestCase):
    def test_const(self):
        self.assertEqual(curry_explicit(const, 0)(), 42)

    def test_const_negativity_arity(self):
        with self.assertRaises(ValueError) as context:
            curry_explicit(const, -681)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_const_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(const, 4)(1)(2)(3)(4)

        self.assertTrue("takes 0 positional arguments but 4 were given" in str(context.exception))

    def test_const_too_many_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(const, 0)()(247)(178)(751)(-33)

        self.assertTrue("object is not callable" in str(context.exception))

    def test_inc_too_many_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(const, 0)(-481, -673, -727)

        self.assertTrue("takes 0 positional arguments but 3 were given" in str(context.exception))


def inc(x: int) -> int:
    return x + 1


class OneArgumentCurryTestCase(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(curry_explicit(inc, 1)(-653), -652)

    def test_inc_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            curry_explicit(inc, -845)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_inc_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(inc, 4)(1)(2)(3)(4)

        self.assertTrue("takes 1 positional argument but 4 were given" in str(context.exception))

    def test_inc_arity_is_less_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(inc, 0)()

        self.assertTrue("missing 1 required positional argument" in str(context.exception))

    def test_inc_too_many_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(inc, 1)(-412)(247)(178)(751)(-33)

        self.assertTrue("object is not callable" in str(context.exception))

    def test_inc_too_many_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(inc, 1)(-481, -673, -727)

        self.assertTrue("takes 1 positional argument but 3 were given" in str(context.exception))

    def test_inc_too_few_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(inc, 1)()

        self.assertTrue("missing 1 required positional argument" in str(context.exception))


def mul(x: int, y: int) -> int:
    return x * y


class TwoArgumentsCurryTestCase(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(curry_explicit(mul, 2)(-653)(387), -252711)

    def test_mul_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            curry_explicit(mul, -142)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_mul_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(mul, 4)(215)(-959)(-497)(408)

        self.assertTrue("takes 2 positional arguments but 4 were given" in str(context.exception))

    def test_mul_arity_is_less_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(mul, 1)(611)

        self.assertTrue("missing 1 required positional argument" in str(context.exception))

    def test_mul_too_many_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(mul, 2)(475)(297)(-272)(-544)(327)

        self.assertTrue("object is not callable" in str(context.exception))

    def test_mul_too_many_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(mul, 2)(-481, -673, -727, 367, -594)

        self.assertTrue("takes 1 positional argument but 5 were given" in str(context.exception))

    def test_mul_too_few_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(mul, 2)()(95)

        self.assertTrue("missing 1 required positional argument" in str(context.exception))


def concat(*args: str) -> str:
    return reduce(lambda acc, x: acc + x, args, "")


class ArbitraryNumberOfArgumentsCurryTestCase(unittest.TestCase):
    def test_concat_4_strings(self):
        self.assertEqual(curry_explicit(concat, 4)("rid")("neighborhood")("visit")("oil"), "ridneighborhoodvisitoil")

    def test_concat_7_strings(self):
        result = curry_explicit(concat, 7)("altogether")("population")("deceit")("soup")("salary")("across")("drag")
        expected = "altogetherpopulationdeceitsoupsalaryacrossdrag"
        self.assertEqual(result, expected)

    def test_concat_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            curry_explicit(concat, -142)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_concat_too_many_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(concat, 4)("arch")("relief")("confident")("rent")("broadcast")

        self.assertTrue("object is not callable" in str(context.exception))

    def test_concat_too_many_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(concat, 4)("explosive", "room", "dog", "grammatical", "live")

        self.assertTrue("takes 1 positional argument but 5 were given" in str(context.exception))

    def test_concat_too_few_positional_arguments(self):
        with self.assertRaises(TypeError) as context:
            curry_explicit(concat, 4)()("broad")()("film")

        self.assertTrue("missing 1 required positional argument" in str(context.exception))
