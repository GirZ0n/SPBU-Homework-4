from collections import OrderedDict
from unittest import TestCase
from homework.homework2.task2.cache import cache_decorator


class CacheFunctionWithOneArgumentTestCase(TestCase):
    def test_negative_size_cache(self):
        with self.assertRaises(ValueError) as context:

            @cache_decorator(size=-162)
            def fib(n: int) -> int:
                if n == 1 or n == 2:
                    return 1
                return fib(n - 1) + fib(n - 2)

        self.assertTrue("Size must be a non-negative number." in str(context.exception))

    def test_zero_size_cache(self):
        @cache_decorator
        def fib(n: int) -> int:
            if n == 1 or n == 2:
                return 1
            return fib(n - 1) + fib(n - 2)

        fib(5)
        fib(6)
        fib(7)

        self.assertFalse(fib._cache)

    def test_positive_size_cache(self):
        @cache_decorator(size=10)
        def fib(n: int) -> int:
            if n == 1 or n == 2:
                return 1
            return fib(n - 1) + fib(n - 2)

        fib(10)
        fib(9)
        fib(8)

        print(fib._cache)

        self.assertEqual(
            fib._cache,
            OrderedDict(
                [
                    ((2,), 1),
                    ((1,), 1),
                    ((3,), 2),
                    ((4,), 3),
                    ((5,), 5),
                    ((6,), 8),
                    ((7,), 13),
                    ((8,), 21),
                    ((9,), 34),
                    ((10,), 55),
                ]
            ),
        )


class CacheFunctionWithArgsTestCase(TestCase):
    def test_negative_size_cache(self):
        with self.assertRaises(ValueError) as context:

            @cache_decorator(size=-444)
            def sum_of_squares(*args: int) -> int:
                return sum(x ** 2 for x in args)

        self.assertTrue("Size must be a non-negative number." in str(context.exception))

    def test_zero_size_cache(self):
        @cache_decorator
        def sum_of_squares(*args: int) -> int:
            return sum(x ** 2 for x in args)

        sum_of_squares(3, 4, 5)
        sum_of_squares(6, 7, 8)
        sum_of_squares(9, 10, 11)

        self.assertFalse(sum_of_squares._cache)

    def test_positive_size_cache(self):
        @cache_decorator(size=10)
        def sum_of_squares(*args: int) -> int:
            return sum(x ** 2 for x in args)

        sum_of_squares(3, 4, 5)
        sum_of_squares(3, 5, 4)
        sum_of_squares(4, 3, 5)
        sum_of_squares(4, 5, 3)
        sum_of_squares(5, 3, 4)
        sum_of_squares(5, 4, 3)
        sum_of_squares(3, 4, 5)
        sum_of_squares(3, 5, 4)
        sum_of_squares(4, 3, 5)
        sum_of_squares(4, 5, 3)
        sum_of_squares(5, 3, 4)
        sum_of_squares(5, 4, 3)

        self.assertEqual(
            sum_of_squares._cache,
            OrderedDict(
                [((3, 4, 5), 50), ((3, 5, 4), 50), ((4, 3, 5), 50), ((4, 5, 3), 50), ((5, 3, 4), 50), ((5, 4, 3), 50)]
            ),
        )


class CacheFunctionWithOneKeywordArgument(TestCase):
    def test_negative_size_cache(self):
        with self.assertRaises(ValueError) as context:

            @cache_decorator(size=-34)
            def fib(*, n: int) -> int:
                if n == 1 or n == 2:
                    return 1
                return fib(n=n - 1) + fib(n=n - 2)

        self.assertTrue("Size must be a non-negative number." in str(context.exception))

    def test_zero_size_cache(self):
        @cache_decorator
        def fib(*, n: int) -> int:
            if n == 1 or n == 2:
                return 1
            return fib(n=n - 1) + fib(n=n - 2)

        fib(n=10)
        fib(n=9)
        fib(n=8)

        self.assertFalse(fib._cache)

    def test_positive_size_cache(self):
        @cache_decorator(size=10)
        def fib(*, n: int) -> int:
            if n == 1 or n == 2:
                return 1
            return fib(n=n - 1) + fib(n=n - 2)

        fib(n=10)
        fib(n=9)
        fib(n=8)

        self.assertEqual(
            fib._cache,
            OrderedDict(
                [
                    ((("n", 2),), 1),
                    ((("n", 1),), 1),
                    ((("n", 3),), 2),
                    ((("n", 4),), 3),
                    ((("n", 5),), 5),
                    ((("n", 6),), 8),
                    ((("n", 7),), 13),
                    ((("n", 8),), 21),
                    ((("n", 9),), 34),
                    ((("n", 10),), 55),
                ]
            ),
        )


class CacheFunctionWithKwargsTestCase(TestCase):
    def test_negative_size_cache(self):
        with self.assertRaises(ValueError) as context:

            @cache_decorator(size=-289)
            def sum_of_squares(**kwargs: int) -> int:
                return sum(x ** 2 for _, x in kwargs.items())

        self.assertTrue("Size must be a non-negative number." in str(context.exception))

    def test_zero_size_cache(self):
        @cache_decorator
        def sum_of_squares(**kwargs: int) -> int:
            return sum(x ** 2 for _, x in kwargs.items())

        sum_of_squares(a=3, b=4, c=5)
        sum_of_squares(a=6, b=7, c=8)
        sum_of_squares(a=9, b=10, c=11)

        self.assertFalse(sum_of_squares._cache)

    def test_positive_size_cache(self):
        @cache_decorator(size=10)
        def sum_of_squares(**kwargs: int) -> int:
            return sum(x ** 2 for _, x in kwargs.items())

        sum_of_squares(a=3, b=4, c=5)
        sum_of_squares(a=3, b=5, c=4)
        sum_of_squares(a=4, b=3, c=5)
        sum_of_squares(a=4, b=5, c=3)
        sum_of_squares(a=5, b=3, c=4)
        sum_of_squares(a=5, b=4, c=3)
        sum_of_squares(a=3, b=4, c=5)
        sum_of_squares(a=3, b=5, c=4)
        sum_of_squares(a=4, b=3, c=5)
        sum_of_squares(a=4, b=5, c=3)
        sum_of_squares(a=5, b=3, c=4)
        sum_of_squares(a=5, b=4, c=3)

        print(sum_of_squares._cache)

        self.assertEqual(
            sum_of_squares._cache,
            OrderedDict(
                [
                    ((("a", 3), ("b", 4), ("c", 5)), 50),
                    ((("a", 3), ("b", 5), ("c", 4)), 50),
                    ((("a", 4), ("b", 3), ("c", 5)), 50),
                    ((("a", 4), ("b", 5), ("c", 3)), 50),
                    ((("a", 5), ("b", 3), ("c", 4)), 50),
                    ((("a", 5), ("b", 4), ("c", 3)), 50),
                ]
            ),
        )
