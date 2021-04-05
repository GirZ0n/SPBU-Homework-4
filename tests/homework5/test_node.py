import json
import unittest
from pathlib import Path

from homework.homework5.node import Node

resources = Path("tests/homework5/resources")


def create_full_node() -> Node:
    node = Node(1, 1, 1)
    node = node.insert(2, 2, 4)
    node = node.insert(3, 3, 3)
    node = node.insert(4, 4, 7)
    node = node.insert(5, 5, 5)
    node = node.insert(6, 6, 6)
    node = node.insert(7, 7, 2)
    return node


class NodeTestCase(unittest.TestCase):
    def test_insert_without_child(self):
        actual = Node(1, 1, 1)

        with open(resources / "without_child.json") as f:
            expected = json.loads(f.read(), cls=Node.NodeDecoder)

        self.assertEqual(expected, actual)

    def test_insert_only_left_child(self):
        actual = Node(1, 1, 1)
        actual = actual.insert(2, 2, 4)

        with open(resources / "only_left_child.json") as f:
            expected = json.loads(f.read(), cls=Node.NodeDecoder)

        self.assertEqual(expected, actual)

    def test_insert_only_right_child(self):
        actual = Node(3, 3, 1)
        actual = actual.insert(2, 2, 4)

        with open(resources / "only_right_child.json") as f:
            expected = json.loads(f.read(), cls=Node.NodeDecoder)

        self.assertEqual(expected, actual)

    def test_insert_full_treap(self):
        actual = create_full_node()

        with open(resources / "full_treap.json") as f:
            expected = json.loads(f.read(), cls=Node.NodeDecoder)

        self.assertEqual(expected, actual)

    def test_contains_key_in_node(self):
        node = create_full_node()
        self.assertTrue(5 in node)

    def test_contains_key_not_in_node(self):
        node = create_full_node()
        self.assertFalse(42 in node)

    def test_iterator(self):
        node = create_full_node()
        self.assertEqual(list(node), [4, 2, 1, 3, 6, 5, 7])

    def test_reversed(self):
        node = create_full_node()
        self.assertEqual(list(reversed(node)), [1, 3, 2, 5, 7, 6, 4])

    def test_get(self):
        node = create_full_node()
        self.assertEqual(node.get(3), 3)

    def test_update(self):
        node = create_full_node()
        node.update(3, 42)
        self.assertEqual(node.get(3), 42)

    def test_remove(self):
        node = create_full_node()
        node = node.remove(5)
        self.assertFalse(5 in node)
