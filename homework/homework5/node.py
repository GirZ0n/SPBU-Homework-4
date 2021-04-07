from json import dumps, JSONEncoder, JSONDecoder
from random import random
from typing import Tuple, Optional, Any, Iterator

KT = float
VT = Any
PT = float


class Node:
    """
    Auxiliary class for Treap.

    """

    key: KT
    value: VT
    priority: PT

    left_child: Optional["Node"] = None
    right_child: Optional["Node"] = None

    def __init__(
        self,
        key: KT,
        value: VT,
        priority: Optional[PT] = None,
        left_child: Optional["Node"] = None,
        right_child: Optional["Node"] = None,
    ):
        self.key = key
        self.value = value

        if priority is None:
            self.priority = random()
        else:
            self.priority = priority

        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        """
        The json representation of the node.
        """
        return dumps(self, allow_nan=True, cls=self.NodeEncoder)

    def __eq__(self, other: Any):
        if isinstance(other, Node):
            return (
                self.key == other.key
                and self.value == other.value
                and self.priority == other.priority
                and self.left_child == other.left_child
                and self.right_child == other.right_child
            )
        return False

    def __contains__(self, key: KT) -> bool:
        """
        Checks if the key is contained in the node.
        """
        if self.key == key:
            return True

        if self.__key_in_left_child(key):
            assert self.left_child is not None
            return key in self.left_child

        if self.__key_in_right_child(key):
            assert self.right_child is not None
            return key in self.right_child

        return False

    def __iter__(self) -> Iterator[VT]:
        """
        Pre-order iterator.
        """
        yield self.value
        if self.left_child is not None:
            yield from self.left_child
        if self.right_child is not None:
            yield from self.right_child

    def __reversed__(self) -> Iterator[VT]:
        """
        Post-order iterator.
        """
        if self.left_child is not None:
            yield from reversed(self.left_child)
        if self.right_child is not None:
            yield from reversed(self.right_child)
        yield self.value

    def insert(self, key: KT, value: VT, priority: Optional[PT] = None) -> "Node":
        """
        Inserts the value into the node by key and priority.

        :return: node with inserted value.
        """
        new_node = Node(key, value, priority)

        left_split, right_split = self.__split(key)

        if left_split is None:
            return new_node.__merge(right_split)

        left_split = left_split.__merge(new_node)
        return left_split.__merge(right_split)

    def get(self, key: KT) -> VT:
        """
        Returns a value by key.
        """
        if self.key == key:
            return self.value

        if self.__key_in_left_child(key):
            assert self.left_child is not None
            return self.left_child.get(key)

        if self.__key_in_right_child(key):
            assert self.right_child is not None
            return self.right_child.get(key)

    def update(self, key: KT, new_value: VT):
        """
        Updates a value by key.
        """
        if self.key == key:
            self.value = new_value

        if self.__key_in_left_child(key):
            assert self.left_child is not None
            self.left_child.update(key, new_value)

        if self.__key_in_right_child(key):
            assert self.right_child is not None
            self.right_child.update(key, new_value)

    def remove(self, key: KT) -> Optional["Node"]:
        """
        Deletes a value by key.

        :return: node without the deleted key.
        """
        left_subtree, right_subtree = self.__split(key)

        if right_subtree is None:
            return left_subtree

        right_subtree = right_subtree.__remove_smallest()

        if left_subtree is None:
            return right_subtree

        return left_subtree.__merge(right_subtree)

    def __remove_smallest(self) -> Optional["Node"]:
        """
        Removes the smallest key from the node.

        :return: node without the smallest key.
        """
        if self.left_child is None:
            return self.right_child

        self.left_child = self.left_child.__remove_smallest()
        return self

    def __split(self, key: KT) -> Tuple[Optional["Node"], Optional["Node"]]:
        """
        Splits the node by key. The left node has all the keys smaller than the given key,
        and the right node has all the others.

        :return: two nodes.
        """
        if key > self.key:
            if self.right_child is None:
                return self, None

            left_subtree, right_subtree = self.right_child.__split(key)

            result = self
            result.right_child = left_subtree
            return result, right_subtree

        if self.left_child is None:
            return None, self

        left_tree, right_tree = self.left_child.__split(key)

        result = self
        result.left_child = right_tree
        return left_tree, result

    def __merge(self, other: Optional["Node"]) -> "Node":
        """
        Combines two nodes.

        :return: merged node.
        """
        if other is None:
            return self

        if self.priority > other.priority:
            result = self
            if self.right_child is None:
                result.right_child = other
            else:
                result.right_child = self.right_child.__merge(other)
            return result

        result = other
        if other.left_child is None:
            result.left_child = self
        else:
            result.left_child = self.__merge(other.left_child)
        return result

    def __key_in_left_child(self, key: KT) -> bool:
        """
        Checks if the key is in the left subtree.
        """
        return (self.left_child is not None) and (key < self.key)

    def __key_in_right_child(self, key: KT) -> bool:
        """
        Checks if the key is in the right subtree.
        """
        return (self.right_child is not None) and (key > self.key)

    class NodeEncoder(JSONEncoder):
        """
        An auxiliary class that allows you to get the json representation of a node.
        """

        def default(self, obj):
            if isinstance(obj, Node):
                return obj.__dict__
            return JSONEncoder.default(self, obj)

    class NodeDecoder(JSONDecoder):
        """
        A helper class that allows you to retrieve a node from a json representation.
        """

        def __init__(self, *args, **kwargs):
            JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

        @staticmethod
        def object_hook(dct):
            return Node(**dct)
