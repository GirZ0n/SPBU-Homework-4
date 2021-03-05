from typing import Callable, Any


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Converts a function that takes multiple arguments into a sequence of functions that each take a single argument
    """

    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    if arity == 0:
        return function

    arguments_left = arity
    args = []

    def curry(arg: Any) -> Callable:
        nonlocal args
        args.append(arg)

        nonlocal arguments_left
        if arguments_left == 1:
            result = function(*args)
            args.clear()
            arguments_left = arity
            return result
        else:
            arguments_left -= 1
            return curry

    return curry
