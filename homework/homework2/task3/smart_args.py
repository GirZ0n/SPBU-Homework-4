from copy import deepcopy
from functools import update_wrapper
from inspect import signature
from typing import Callable, Any


class Evaluated:
    def __init__(self, func: Callable):
        """
        Substitutes the default value calculated at the time of the call.

        :param func: a function that will calculate the default value before each call.
        """
        if isinstance(func, Isolated):
            raise ValueError("Isolated cannot be used with Evaluated")

        if len(signature(func).parameters) != 0:
            raise ValueError("Functions with arguments are not supported by Evaluated")

        self.func = func


class Isolated:
    def __init__(self, arg=None):
        """
        Fictitious default value. Make a deep copy while receiving the argument.

        :param arg: the object to be isolated.
        """
        if isinstance(arg, Evaluated):
            raise ValueError("Evaluated cannot be used with Isolated")

        self.arg = arg


# Wraps _SmartArgs to allow for deferred calling
def smart_args(func=None, *, positional_arguments_included: bool = False):
    """
    Decorator that parses the default value types of function arguments.

    :param func: any function that will use smart_args
    :param positional_arguments_included: flag responsible for handling positional variables
    :return: the original function wrapped in the decorator
    """
    if func is None:
        return lambda f: _SmartArgs(f, positional_arguments_included)

    return _SmartArgs(func, positional_arguments_included)


class _SmartArgs:
    def __init__(self, function: Callable, positional_arguments_included: bool):
        self._function = function
        self._positional_arguments_included = positional_arguments_included
        update_wrapper(self, function)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for parameter_name, parameter in signature(self._function).parameters.items():
            if isinstance(parameter.default, Isolated):
                if parameter_name in kwargs.keys():
                    kwargs[parameter_name] = deepcopy(kwargs[parameter_name])
                elif not self._positional_arguments_included:
                    raise KeyError(f"Parameter '{parameter_name}' not passed to function")

            if isinstance(parameter.default, Evaluated):
                if parameter_name not in kwargs.keys():
                    kwargs[parameter_name] = parameter.default.func()

        if self._positional_arguments_included and len(args) > 0:
            args_list = []
            for arg in args:
                elem = arg
                if isinstance(arg, Isolated):
                    elem = deepcopy(arg.arg)
                if isinstance(arg, Evaluated):
                    elem = arg.func()

                args_list.append(elem)
            args = tuple(args_list)

        return self._function(*args, **kwargs)
