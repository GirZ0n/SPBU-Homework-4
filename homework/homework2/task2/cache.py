from collections import OrderedDict
from functools import update_wrapper
from typing import Hashable, Callable, OrderedDict as OrderedDictType


class _Cache:
    def __init__(self, function: Callable, size: int):
        self._function = function
        self._size = size
        self._cache: OrderedDictType = OrderedDict()
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
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
    def __make_key(*args: Hashable, **kwargs: Hashable) -> tuple:
        key = args
        if kwargs:
            key += tuple(sorted(kwargs.items()))

        return key
        # return args + tuple(sorted(kwargs.items()))


def cache_decorator(func=None, *, size: int = 0):
    if size < 0:
        raise ValueError("Size must be a non-negative number.")

    if func is None:
        return lambda f: _Cache(f, size)

    return _Cache(func, size)


# ---------------------------------------------------------------------

# F = TypeVar("F", bound=Callable[..., object])
#
#
# class ActionWithAttributes(Protocol[F]):
#     cache: OrderedDict
#     __call__: F
#
#
# def action_with_attributes(action: F) -> ActionWithAttributes[F]:
#     action_with_attributes = cast(ActionWithAttributes[F], action)
#     action_with_attributes.cache = OrderedDict()
#     return action_with_attributes
#
#
# def cache_decorator(func=None, *, size: int = 0):
#     if size < 0:
#         raise ValueError("Size must be a non-negative number.")
#
#     if func is None:
#         return lambda f: cache_decorator(f, size=size)
#
#     @action_with_attributes
#     @wraps(func)
#     def inner(*args: Hashable, **kwargs: Hashable):
#         if size == 0:
#             return func(*args, **kwargs)
#
#         key = make_key(*args, **kwargs)
#         if key in inner.cache:
#             return inner.cache[key]
#
#         value = func(*args, **kwargs)
#
#         if len(inner.cache) >= size:
#             inner.cache.popitem(last=False)
#         inner.cache[key] = value
#
#         return value
#
#     inner.cache = OrderedDict()
#
#     def make_key(*args: Hashable, **kwargs: Hashable) -> tuple:
#         return args + tuple(sorted(kwargs.items()))
#
#     return inner


@cache_decorator(size=3)
def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(10)


print(fib._cache)

fib(9)

print(fib._cache)

fib(5)

print(fib._cache)
