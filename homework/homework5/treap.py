from collections.abc import MutableMapping
from typing import Optional, Iterator, Any

from homework.homework5.node import Node, KT, VT, PT


class Treap(MutableMapping):
    """
    Randomized binary search tree implementation.
    """

    __size: int = 0
    __head: Optional[Node] = None

    def __str__(self) -> str:
        """
        The json representation of the node.
        """
        return str(self.__head)

    def __setitem__(self, key: KT, value: VT) -> None:
        """
        Inserts the value into the treap by key.

        If the key is already present in the treap, it updates the value.
        """
        if key in self:
            assert self.__head is not None
            self.__head.update(key, value)
        else:
            if self.__head is None:
                self.__head = Node(key, value)
            else:
                self.__head = self.__head.insert(key, value)

            self.__size += 1

    def insert(self, key: KT, value: VT, priority: PT) -> None:
        """
        Inserts the value into the treap by key and priority.
        """
        if key in self:
            raise KeyError(f"The given key ({key}) is already in the tree")

        if self.__head is None:
            self.__head = Node(key, value, priority)
        else:
            self.__head = self.__head.insert(key, value, priority)

        self.__size += 1

    def __contains__(self, key: Any) -> bool:
        """
        Checks if an item is in the tree.
        """
        return self.__head is not None and key in self.__head

    def __delitem__(self, key: KT) -> None:
        """
        Deletes an item by key.
        """
        if self.__head is None:
            raise KeyError("The treap is empty")

        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        self.__head = self.__head.remove(key)

        self.__size -= 1

    def __getitem__(self, key: KT) -> VT:
        """
        Returns the value of the element by the key.
        """
        if self.__head is None:
            raise KeyError("The treap is empty")

        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        return self.__head.get(key)

    def __len__(self) -> int:
        """
        Returns the number of elements in the treap.
        """
        return self.__size

    def __iter__(self) -> Iterator[VT]:
        """
        Pre-order iterator.
        """
        if self.__head is None:
            yield from ()
        else:
            yield from self.__head

    def __reversed__(self) -> Iterator[VT]:
        """
        Post-order iterator.
        """
        if self.__head is None:
            yield from ()
        else:
            yield from reversed(self.__head)
