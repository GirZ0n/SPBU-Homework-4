import unittest
from functools import reduce

from homework.homework2.task1.curry import curry_explicit
from homework.homework2.task1.uncurry import uncurry_explicit
from tests.tests_utils import check_message

ARITY_CANNOT_BE_NEGATIVE = "Arity cannot be negative."
OBJECT_IS_NOT_CALLABLE = "object is not callable"
NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY = "The number of arguments passed must match the arity."


def const() -> int:
    return 42


class ZeroArgumentsUncurryTestCase(unittest.TestCase):
    def test_const(self):
        self.assertEqual(uncurry_explicit(const, 0)(), 42)

    def test_const_negativity_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(const, -681)

        self.assertTrue(check_message(context, ARITY_CANNOT_BE_NEGATIVE))

    def test_const__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(const, 0)(447, -781)

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_const_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(const, 4)(984, -305, -891, -462)

        self.assertTrue(check_message(context, "takes 0 positional arguments but 1 was given"))


def inc(x: int) -> int:
    return x + 1


class OneArgumentUncurryTestCase(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(uncurry_explicit(inc, 1)(804), 805)

    def test_inc_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(inc, -71)

        self.assertTrue(check_message(context, ARITY_CANNOT_BE_NEGATIVE))

    def test_inc__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 1)(447, -781, -898)

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_inc__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 1)()

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_inc_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 4)(984, -305, -891, -462)

        self.assertTrue(check_message(context, OBJECT_IS_NOT_CALLABLE))

    def test_inc_arity_is_less_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(inc, 0)()

        self.assertTrue(check_message(context, "missing 1 required positional argument"))


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

        self.assertTrue(check_message(context, ARITY_CANNOT_BE_NEGATIVE))

    def test_mul__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 2)(-891, 78, -248, 497, 64)

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_mul__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 2)(-752)

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_mul_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(mul, 5)(-851, 308, -776, -25, -5)

        self.assertTrue(check_message(context, OBJECT_IS_NOT_CALLABLE))


concat = curry_explicit(lambda *args: reduce(lambda acc, x: acc + x, args, ""), 5)


class ArbitraryNumberOfArgumentsUncurryTestCase(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(
            uncurry_explicit(concat, 5)("life", "type", "money", "strength", "crack"), "lifetypemoneystrengthcrack"
        )

    def test_concat_negative_arity(self):
        with self.assertRaises(ValueError) as context:
            uncurry_explicit(concat, -702)

        self.assertTrue(check_message(context, ARITY_CANNOT_BE_NEGATIVE))

    def test_concat__number_of_arguments_is_greater_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 5)("sign", "weed", "event", "ill", "rob", "consider", "bind", "perhaps", "have")

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_concat__number_of_arguments_is_less_than_arity(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 5)("escape", "represent", "bottle")

        self.assertTrue(check_message(context, NUMBER_OF_ARGUMENTS_PASSED_MUST_MATCH_ARITY))

    def test_concat_arity_is_greater_than_arity_of_function(self):
        with self.assertRaises(TypeError) as context:
            uncurry_explicit(concat, 8)("merchant", "wicked", "sign", "excessive", "salary", "mild", "clay", "colony")

        self.assertTrue(check_message(context, OBJECT_IS_NOT_CALLABLE))
