from typing import Optional, Callable, Any


def reduce_right(function: Callable, values: Any, initial: Optional[Any] = None) -> Any:
    elements = [element for element in values]

    if initial is not None:
        elements.append(initial)

    if len(elements) < 2:
        raise ValueError("You need to pass at least two values (including initial).")

    elements.reverse()

    current_value = function(elements[1], elements[0])
    for element in elements[2:]:
        current_value = function(element, current_value)

    return current_value


print(reduce_right(lambda x, y: f"({x}+{y})", (ord(c) for c in "abcde"), "5"))
