from collections import OrderedDict
from functools import update_wrapper
from typing import Callable, OrderedDict as OrderedDictType, Any


# Wraps _Cache to allow for deferred calling
def cache_decorator(func=None, *, size: int = 0):
    """A simple decorator that caches function values."""
    if size < 0:
        raise ValueError("Size must be a non-negative number.")

    if func is None:
        return lambda f: _Cache(f, size)

    return _Cache(func, size)


class _Cache:
    def __init__(self, function: Callable, size: int):
        self._function = function
        self._size = size
        self._cache: OrderedDictType = OrderedDict()
        update_wrapper(self, function)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self._size == 0:
            return self._function(*args, **kwargs)

        key = self.__make_key(*args, **kwargs)
        if key in self._cache:
            return self._cache[key]

        value = self._function(*args, **kwargs)

        if len(self._cache) >= self._size:
            self._cache.popitem(last=False)
        self._cache[key] = value

        return value

    @staticmethod
    def __make_key(*args: Any, **kwargs: Any) -> tuple:
        return args + tuple(sorted(kwargs.items()))
