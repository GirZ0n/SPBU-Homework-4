from typing import Callable, Any


def uncurry_explicit(function: Callable, arity: int) -> Callable:
    """
    The inverse of curry_explicit.

    :param function: curried function.
    :param arity: the number of arguments that the original function takes.
    :return: original (not curried) function.
    """

    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    def uncurry(*args: Any) -> Callable:
        if len(args) != arity:
            raise TypeError("The number of arguments passed must match the arity.")

        if len(args) == 1 or len(args) == 0:
            return function(*args)

        result = function(args[0])
        for i in range(1, arity):
            result = result(args[i])

        return result

    return uncurry
