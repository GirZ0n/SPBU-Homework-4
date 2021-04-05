from copy import deepcopy
from random import random
from typing import Tuple, Optional, Any
from json import dumps, JSONEncoder, JSONDecoder


class Node:
    priority: float

    left_child: Optional["Node"] = None
    right_child: Optional["Node"] = None

    def __init__(
        self,
        key,
        value,
        priority: Optional[float] = None,
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
        return dumps(self, allow_nan=True, cls=self.NodeEncoder)

    def __eq__(self, other):
        if isinstance(other, Node):
            return (
                self.key == other.key
                and self.value == other.value
                and self.priority == other.priority
                and self.left_child == other.left_child
                and self.right_child == other.right_child
            )
        return False

    def __contains__(self, key) -> bool:
        if self.key == key:
            return True

        if (self.left_child is not None) and (key < self.key):
            return key in self.left_child

        if (self.right_child is not None) and (key > self.key):
            return key in self.right_child

        return False

    def __iter__(self):
        yield self.value
        if self.left_child is not None:
            yield from self.left_child
        if self.right_child is not None:
            yield from self.right_child

    def __reversed__(self):
        if self.left_child is not None:
            yield from reversed(self.left_child)
        if self.right_child is not None:
            yield from reversed(self.right_child)
        yield self.value

    def insert(self, key, value, priority: Optional[float] = None) -> "Node":
        new_node = Node(key, value, priority)

        left_split, right_split = self.__split(key)

        if left_split is None:
            return new_node.__merge(right_split)
        else:
            left_split = left_split.__merge(new_node)
            return left_split.__merge(right_split)

    def get(self, key) -> Any:
        if self.key == key:
            return self.value

        if self.left_child is not None and key < self.key:
            return self.left_child.get(key)

        if self.right_child is not None and key > self.key:
            return self.right_child.get(key)

    def update(self, key, new_value):
        if self.key == key:
            self.value = new_value

        if self.left_child is not None and key < self.key:
            self.left_child.update(key, new_value)

        if self.right_child is not None and key > self.key:
            self.right_child.update(key, new_value)

    def remove(self, key) -> Optional["Node"]:
        left_subtree, right_subtree = self.__split(key)

        if right_subtree is not None:
            right_subtree = right_subtree.__remove_smallest()
        else:
            return left_subtree

        if left_subtree is None:
            return right_subtree

        return left_subtree.__merge(right_subtree)

    def __remove_smallest(self) -> Optional["Node"]:
        if self.left_child is None:
            return deepcopy(self.right_child)

        self.left_child = self.left_child.__remove_smallest()
        return deepcopy(self)

    def __split(self, key) -> Tuple[Optional["Node"], Optional["Node"]]:
        if key > self.key:
            if self.right_child is None:
                return deepcopy(self), None

            left_subtree, right_subtree = self.right_child.__split(key)

            result = deepcopy(self)
            result.right_child = left_subtree
            return result, right_subtree
        else:
            if self.left_child is None:
                return None, deepcopy(self)

            left_tree, right_tree = self.left_child.__split(key)

            result = deepcopy(self)
            result.left_child = right_tree
            return left_tree, result

    def __merge(self, other: Optional["Node"]) -> "Node":
        if other is None:
            return deepcopy(self)

        if self.priority > other.priority:
            result = deepcopy(self)
            if self.right_child is None:
                result.right_child = deepcopy(other)
            else:
                result.right_child = self.right_child.__merge(other)
            return result
        else:
            result = deepcopy(other)
            if other.left_child is None:
                result.left_child = deepcopy(self)
            else:
                result.left_child = self.__merge(other.left_child)
            return result

    class NodeEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Node):
                return obj.__dict__
            return JSONEncoder.default(self, obj)

    class NodeDecoder(JSONDecoder):
        def __init__(self, *args, **kwargs):
            JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

        def object_hook(self, dct):
            return Node(**dct)
