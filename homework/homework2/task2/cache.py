import functools
from collections import OrderedDict
from typing import Hashable


def cache_decorator(func=None, *, size: int = 0):
    if size < 0:
        raise ValueError("Size must be a non-negative number.")

    if func is None:
        return lambda f: cache_decorator(f, size=size)

    @functools.wraps(func)
    def inner(*args: Hashable, **kwargs: Hashable):
        if size == 0:
            return func(*args, **kwargs)

        key = make_key(*args, **kwargs)
        if key in inner.cache:
            return inner.cache[key]

        value = func(*args, **kwargs)

        if len(inner.cache) >= size:
            inner.cache.popitem(last=False)
        inner.cache[key] = value

        return value

    inner.cache = OrderedDict()

    def make_key(*args: Hashable, **kwargs: Hashable) -> tuple:
        return args + tuple(sorted(kwargs.items()))

    return inner
