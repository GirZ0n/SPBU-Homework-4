from copy import deepcopy
from random import random
from typing import Tuple, Optional, Any, Generic


class Node:
    key: float
    value: Any

    priority: float

    left_child: Optional["Node"] = None
    right_child: Optional["Node"] = None

    def __init__(self, key: float, value: Any, priority: Optional[float] = None):
        self.key = key
        self.value = value

        if priority is None:
            self.priority = random()
        else:
            self.priority = priority

    def __str__(self):
        """
        Converts Node to json string.

        :return: json string.
        """

        left_child_json = str(self.left_child) if self.left_child is not None else "null"
        right_child_json = str(self.right_child) if self.right_child is not None else "null"

        return (
                f'{{"key": {self.key}, "data": {self.value}, "priority": {self.priority}, '
                + f'"left": {left_child_json}, "right": {right_child_json} }}'
        )

    def __contains__(self, key: float) -> bool:
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
            yield from self.left_child
        if self.right_child is not None:
            yield from self.right_child
        yield self.value

    def insert(self, key: float, value: Any, priority: Optional[float] = None) -> "Node":
        new_node = Node(key, value, priority)

        left_split, right_split = self.__split(key)

        if left_split is None:
            return new_node.__merge(right_split)
        else:
            left_split = left_split.__merge(new_node)
            return left_split.__merge(right_split)

    def get(self, key: float) -> Any:
        if self.key == key:
            return self.value

        if self.left_child is not None and key < self.key:
            return self.left_child.get(key)

        if self.right_child is not None and key > self.key:
            return self.right_child.get(key)

    def update(self, key: float, new_value: Any):
        if self.key == key:
            self.value = new_value

        if self.left_child is not None and key < self.key:
            self.left_child.update(key, new_value)

        if self.right_child is not None and key > self.key:
            self.right_child.update(key, new_value)

    def remove(self, key: float) -> Optional["Node"]:
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

    def __split(self, key: float) -> Tuple[Optional["Node"], Optional["Node"]]:
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
