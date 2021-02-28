def curry_explicit(function, arity: int):
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:
        return function

    # TODO: Проверить, что указанная арность не больше арности функции

    current_arity = arity

    args = []

    def inner(arg):
        nonlocal args
        args.append(arg)

        nonlocal current_arity
        if current_arity == 1:
            result = function(*args)
            args.clear()
            current_arity = arity
            return result
        else:
            current_arity -= 1
            return inner

    return inner
