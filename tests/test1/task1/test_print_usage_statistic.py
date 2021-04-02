import unittest

from exam.test1.task1.spy import print_usage_statistic, Spy
from tests.tests_utils import check_message


class SpyTestCase(unittest.TestCase):
    def test_non_spy_function(self):
        with self.assertRaises(ValueError) as context:

            def foo():
                return 5

            for _, _ in print_usage_statistic(foo):
                pass

        self.assertTrue(check_message(context, "The function should have been decorated with @Spy."))

    def test_function_without_logs(self):
        @Spy
        def foo():
            return 5

        result = []
        for _, parameters in print_usage_statistic(foo):
            result.append(parameters)

        self.assertTrue(len(result) == 0)

    def test_function_with_logs_arg(self):
        @Spy
        def foo(arg):
            return arg

        foo(-827)
        foo(861)
        foo(-172)

        result = []
        for _, parameters in print_usage_statistic(foo):
            result.append(parameters)

        self.assertEqual(
            result, [{"args": (-827,), "kwargs": {}}, {"args": (861,), "kwargs": {}}, {"args": (-172,), "kwargs": {}}]
        )

    def test_function_with_logs_kwarg(self):
        @Spy
        def foo(kwarg):
            return kwarg

        foo(kwarg=-431)
        foo(kwarg=804)
        foo(kwarg=542)

        result = []
        for _, parameters in print_usage_statistic(foo):
            result.append(parameters)

        self.assertEqual(
            result,
            [
                {"args": (), "kwargs": {"kwarg": -431}},
                {"args": (), "kwargs": {"kwarg": 804}},
                {"args": (), "kwargs": {"kwarg": 542}},
            ],
        )
