from typing import Callable


def uncurry_explicit(function: Callable, arity: int):
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    if arity == 0:
        return function

    def uncurry(*args):
        if len(args) != arity:
            raise TypeError("The number of arguments passed must match the arity.")

        if len(args) == 1:
            return function(*args)

        result = function(args[0])
        for i in range(1, arity):
            result = function(args[i])

        return result

    return uncurry
