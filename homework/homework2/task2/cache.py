import functools
from collections import OrderedDict
from typing import Optional


def cache_decorator(func=None, *, size: Optional[int] = None):
    if func is None:
        return lambda f: cache_decorator(f, size=size)

    cache = OrderedDict()

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if size is None:
            return func(*args, **kwargs)

        key = make_key(*args, **kwargs)
        if key in cache:
            return cache[key]

        value = func(*args, **kwargs)

        if len(cache) >= size:
            cache.popitem(last=False)
        cache[key] = value

        return value

    def make_key(*args, **kwargs) -> tuple:
        key = args

        for item in kwargs.items():
            key += item

        return key

    return inner
