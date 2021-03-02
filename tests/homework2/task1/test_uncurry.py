import unittest
from functools import reduce

from homework.homework2.task1.curry import curry_explicit
from homework.homework2.task1.uncurry import uncurry_explicit


def const() -> int:
    return 42


class ZeroArgumentsUncurryTestCase(unittest.TestCase):
    def test_const(self):
        self.assertEqual(uncurry_explicit(const, 0)(), 42)

    def test_const_negativity_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(const, -681)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_const__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(const, 0)(447, -781)

        self.assertTrue("The number of arguments passed must match the arity." in str(context.exception))

    def test_const_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(const, 4)(984, -305, -891, -462)

        self.assertTrue("takes 0 positional arguments but 1 was given" in str(context.exception))


def inc(x: int) -> int:
    return x + 1


class OneArgumentUncurryTestCase(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(uncurry_explicit(inc, 1)(804), 805)

    def test_inc_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(inc, -71)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_inc__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 1)(447, -781, -898)

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_inc__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 1)()

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_inc_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 4)(984, -305, -891, -462)

        self.assertTrue("object is not callable" in str(context.exception))

    def test_inc_arity_is_less_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 0)()

        self.assertTrue("missing 1 required positional argument" in str(context.exception))


def mul(x: int):
    def inner(y: int):
        return x * y

    return inner


class TwoArgumentsUncurryTestCase(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(uncurry_explicit(mul, 2)(804, 816), 656064)

    def test_mul_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(mul, -702)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_mul__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 2)(-891, 78, -248, 497, 64)

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_mul__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 2)(-752)

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_mul_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 5)(-851, 308, -776, -25, -5)

        self.assertTrue("object is not callable" in str(context.exception))


concat = curry_explicit(lambda *args: reduce(lambda acc, x: acc + x, args, ""), 5)


class ArbitraryNumberOfArgumentsUncurryTestCase(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(
            uncurry_explicit(concat, 5)("life", "type", "money", "strength", "crack"), "lifetypemoneystrengthcrack"
        )

    def test_concat_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(concat, -702)

        self.assertTrue("Arity cannot be negative." in str(context.exception))

    def test_concat__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 5)("sign", "weed", "event", "ill", "rob", "consider", "bind", "perhaps", "have")

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_concat__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 5)("escape", "represent", "bottle")

        self.assertTrue("The number of arguments passed must match the arity" in str(context.exception))

    def test_concat_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 8)("merchant", "wicked", "sign", "excessive", "salary", "mild", "clay", "colony")

        self.assertTrue("object is not callable" in str(context.exception))
