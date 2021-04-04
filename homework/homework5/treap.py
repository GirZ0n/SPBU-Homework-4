from abc import abstractmethod, ABCMeta
from collections.abc import MutableMapping
from typing import Optional, TypeVar, Generic, Iterator, Any

from node import Node


class Treap(MutableMapping):
    size: int = 0
    head: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.head)

    def __setitem__(self, key: float, value: Any) -> None:
        if key in self:
            assert self.head is not None
            self.head.update(key, value)
        else:
            if self.head is None:
                self.head = Node(key, value)
            else:
                self.head = self.head.insert(key, value)

            self.size += 1

    def __contains__(self, key) -> bool:
        return self.head is not None and key in self.head

    def __delitem__(self, key: float) -> None:
        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        if self.head is None:
            raise KeyError("The treap is empty")

        self.head = self.head.remove(key)

        self.size -= 1

    def __getitem__(self, key: float) -> Any:
        if key not in self:
            raise KeyError(f"There is no such key ({key}) in the treap")

        assert self.head is not None
        return self.head.get(key)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[Any]:
        if self.head is None:
            yield from ()

        assert self.head is not None
        yield from self.head

    def __reversed__(self) -> Iterator[Any]:
        if self.head is None:
            yield from ()

        assert self.head is not None
        yield from reversed(self.head)
