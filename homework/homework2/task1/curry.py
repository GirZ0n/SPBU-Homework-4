from typing import Callable, Any, List


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Converts a function that takes multiple arguments into a sequence of functions that each take a single argument.

    :param function: any function.
    :param arity: the number of arguments that the function takes.
    :return: curried function.
    """

    def __inner(arguments: List) -> Callable:
        if arity < 0:
            raise ValueError("Arity cannot be negative.")

        if arity == 0:
            return function

        def curry(arg: Any) -> Callable:
            if len(arguments) + 1 < arity:
                return __inner([*arguments, arg])
            else:
                return function(*arguments, arg)

        return curry

    argument_list: List = []
    return __inner(argument_list)
