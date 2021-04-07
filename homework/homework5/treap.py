from collections.abc import MutableMapping
from typing import Optional, Iterator, Any

from homework.homework5.node import Node

KT = float
VT = Any
PT = float


class Treap(MutableMapping):
    __size: int = 0
    __head: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.__head)

    def __setitem__(self, key: KT, value: VT) -> None:
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
        if key in self:
            raise KeyError(f"The given key ({key}) is already in the tree")

        if self.__head is None:
            self.__head = Node(key, value, priority)
        else:
            self.__head = self.__head.insert(key, value, priority)

        self.__size += 1

    def __contains__(self, key: Any) -> bool:
        return self.__head is not None and key in self.__head

    def __delitem__(self, key: KT) -> None:
        if self.__head is None:
            raise KeyError("The treap is empty")

        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        self.__head = self.__head.remove(key)

        self.__size -= 1

    def __getitem__(self, key: KT) -> VT:
        if self.__head is None:
            raise KeyError("The treap is empty")

        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        return self.__head.get(key)

    def __len__(self) -> int:
        return self.__size

    def __iter__(self) -> Iterator[VT]:
        if self.__head is None:
            yield from ()
        else:
            yield from self.__head

    def __reversed__(self) -> Iterator[VT]:
        if self.__head is None:
            yield from ()
        else:
            yield from reversed(self.__head)
