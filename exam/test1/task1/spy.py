from datetime import datetime
from functools import update_wrapper
from typing import Callable, List, Any, Tuple


class Spy:
    def __init__(self, function: Callable):
        self._function = function
        self.logs: List[Tuple] = []
        update_wrapper(self, function)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        current_time = datetime.now()
        params = {"args": args, "kwargs": kwargs}
        self.logs.append((current_time, params))

        return self._function(*args, **kwargs)


def print_usage_statistic(function: Callable):
    if not isinstance(function, Spy):
        raise ValueError("The function should have been decorated with @Spy.")

    for element in function.logs:
        yield element
