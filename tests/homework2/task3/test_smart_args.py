import datetime
from time import sleep
from unittest import TestCase

from homework.homework2.task3.smart_args import smart_args, Evaluated, Isolated


def check_message(context, expected_message: str) -> bool:
    return expected_message in str(context.exception)


class SmartArgsTestCase(TestCase):
    def test_isolated_inside_evaluated(self):
        with self.assertRaises(ValueError) as context:

            @smart_args
            def check(*, arg=Evaluated(Isolated())):
                pass

        self.assertTrue(check_message(context, "Isolated cannot be used with Evaluated"))

    def test_evaluated_inside_isolated(self):
        with self.assertRaises(ValueError) as context:

            @smart_args
            def check(*, arg=Isolated(Evaluated(lambda: 42))):
                pass

        self.assertTrue(check_message(context, "Evaluated cannot be used with Isolated"))

    def test_function_with_params_as_argument_of_evaluated(self):
        with self.assertRaises(ValueError) as context:

            @smart_args
            def check(*, arg=Evaluated(lambda x, y, z: 42)):
                pass

        self.assertTrue(check_message(context, "Functions with arguments are not supported by Evaluated"))

    def test_isolated_keyword_argument(self):
        @smart_args
        def list_sort(*, input_list=Isolated()):
            input_list.sort()

        input_list = [-644, 883, 796, -608, -985]

        list_sort(input_list=input_list)

        self.assertEqual(input_list, [-644, 883, 796, -608, -985])

    def test_evaluated_keyword_argument(self):
        def get_timestamp():
            return datetime.datetime.now().timestamp()

        @smart_args
        def check(*, x=get_timestamp(), y=Evaluated(get_timestamp)):
            return x, y

        x1, y1 = check()
        sleep(0.001)
        x2, y2 = check()

        self.assertTrue(x1 == x2 and y1 < y2)
