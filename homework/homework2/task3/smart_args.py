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
def smart_args(func=None):
    """
    Decorator that parses the default value types of function arguments.

    :param func: any function that will use smart_args
    :return: the original function wrapped in the decorator
    """
    if func is None:
        return lambda f: _SmartArgs(f)

    return _SmartArgs(func)


class _SmartArgs:
    def __init__(self, function: Callable):
        self._function = function
        update_wrapper(self, function)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for parameter_name, parameter in signature(self._function).parameters.items():
            if isinstance(parameter.default, Isolated):
                if parameter_name in kwargs.keys():
                    kwargs[parameter_name] = deepcopy(kwargs[parameter_name])
                else:
                    raise KeyError(f"Parameter '{parameter_name}' not passed to function")

            if isinstance(parameter.default, Evaluated):
                if parameter_name not in kwargs.keys():
                    kwargs[parameter_name] = parameter.default.func()

        return self._function(*args, **kwargs)
