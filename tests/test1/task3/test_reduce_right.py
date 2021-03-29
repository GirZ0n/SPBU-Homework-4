import unittest

from exam.test1.task3.reduce_right import reduce_right
from tests.tests_utils import check_message


class ReduceRightTestCase(unittest.TestCase):
    def test_too_few_values(self):
        with self.assertRaises(ValueError) as context:
            reduce_right(lambda x, y: f"({x}+{y})", (ord(c) for c in "a"))

        self.assertTrue(check_message(context, "You need to pass at least two values (including initial)."))

    def test_without_initial(self):
        result = reduce_right(lambda x, y: f"({x}+{y})", (ord(c) for c in "abcde"))
        self.assertEqual(result, "(97+(98+(99+(100+101))))")

    def test_with_initial(self):
        result = reduce_right(lambda x, y: f"({x}+{y})", (ord(c) for c in "abcde"), "5")
        self.assertEqual(result, "(97+(98+(99+(100+(101+5)))))")
