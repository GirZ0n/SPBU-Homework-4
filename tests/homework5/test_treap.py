import unittest
from pathlib import Path

from homework.homework5.treap import Treap
from tests.tests_utils import check_message

resources = Path("tests/resources/homework5")


def create_full_treap() -> Treap:
    treap = Treap()
    treap.insert(1, 1, 1)
    treap.insert(2, 2, 4)
    treap.insert(3, 3, 3)
    treap.insert(4, 4, 7)
    treap.insert(5, 5, 5)
    treap.insert(6, 6, 6)
    treap.insert(7, 7, 2)
    return treap


class TreapTestCase(unittest.TestCase):
    def test_contains_key_in_treap(self):
        treap = create_full_treap()
        self.assertTrue(3 in treap)

    def test_contains_key_not_in_treap(self):
        treap = create_full_treap()
        self.assertFalse(42 in treap)

    def test_delete_empty_treap(self):
        treap = Treap()
        with self.assertRaises(KeyError) as context:
            del treap[42]

        self.assertTrue(check_message(context, "The treap is empty"))

    def test_delete_key_not_in_treap(self):
        treap = create_full_treap()
        with self.assertRaises(KeyError) as context:
            del treap[42]

        self.assertTrue(check_message(context, "There is no such key (42) in the treap"))

    def test_delete_key_in_treap(self):
        treap = create_full_treap()
        del treap[3]

        self.assertTrue(3 not in treap)

    def test_get_empty_treap(self):
        treap = Treap()
        with self.assertRaises(KeyError) as context:
            treap[42]

        self.assertTrue(check_message(context, "The treap is empty"))

    def test_get_key_not_in_treap(self):
        treap = create_full_treap()
        with self.assertRaises(KeyError) as context:
            treap[42]

        self.assertTrue(check_message(context, "There is no such key (42) in the treap"))

    def test_get_key_in_treap(self):
        treap = create_full_treap()
        result = treap[3]

        self.assertEqual(result, 3)

    def test_len_empty_treap(self):
        treap = Treap()
        self.assertEqual(len(treap), 0)

    def test_len_non_empty_treap(self):
        treap = Treap()
        for i in range(10):
            treap[i] = i
        self.assertEqual(len(treap), 10)

    def test_iterator_empty_treap(self):
        treap = Treap()
        self.assertEqual(list(treap), [])

    def test_iterator_non_empty_treap(self):
        treap = create_full_treap()
        self.assertEqual(list(treap), [4, 2, 1, 3, 6, 5, 7])

    def test_reversed_empty_treap(self):
        treap = Treap()
        self.assertEqual(list(reversed(treap)), [])

    def test_reversed_non_empty_treap(self):
        treap = create_full_treap()
        self.assertEqual(list(reversed(treap)), [1, 3, 2, 5, 7, 6, 4])

    def test_set_empty_treap(self):
        treap = Treap()
        treap[5] = 5
        self.assertTrue(5 in treap)

    def test_set_key_not_in_treap(self):
        treap = create_full_treap()
        treap[42] = 42
        self.assertTrue(treap[42] == 42)

    def test_set_key_in_treap(self):
        treap = create_full_treap()
        treap[3] = 42
        self.assertTrue(treap[3], 42)
