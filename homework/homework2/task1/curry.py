from typing import Callable, Any, List

from homework.homework2.task1.uncurry import uncurry_explicit


def curry_explicit(function: Callable, arity: int) -> Callable:
    """
    Converts a function that takes multiple arguments into a sequence of functions that each take a single argument.

    :param function: any function.
    :param arity: the number of arguments that the function takes.
    :return: curried function.
    """

    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    if arity == 0:
        return function

    def __inner(arguments: List):
        if arity == len(arguments):
            return function(*arguments)

        def curry(arg: Any) -> Callable:
            return __inner([*arguments, arg])

        return curry

    argument_list: List = []
    return __inner(argument_list)
