import unittest
from typing import Callable
from threading import Thread

from tests.tests_utils import check_message

from homework.homework6.semaphore import Semaphore


def run_threads(number_of_threads: int, function: Callable):
    threads = [Thread(target=function) for _ in range(number_of_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


class SemaphoreRaisesTestCase(unittest.TestCase):
    def test_incorrect_semaphore_size(self):
        with self.assertRaises(ValueError) as context:
            Semaphore(-206)

        self.assertTrue(check_message(context, "Semaphore initial size must be >= 0"))


class SemaphoreIncrementTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.semaphore = Semaphore()
        self.count = 0

    def increment(self):
        for i in range(100_000):
            with self.semaphore:
                self.count += 1

    def increment_with_long_critical_section(self):
        with self.semaphore:
            for i in range(100_000):
                self.count += 1

    def test_increment_one_thread(self):
        run_threads(1, self.increment)

        self.assertEqual(self.count, 100_000)

    def test_increment_ten_threads(self):
        run_threads(10, self.increment)

        self.assertEqual(self.count, 100_000 * 10)

    def test_increment_with_long_critical_section_one_thread(self):
        run_threads(1, self.increment_with_long_critical_section)

        self.assertEqual(self.count, 100_000)

    def test_increment_with_long_critical_section_ten_threads(self):
        run_threads(10, self.increment_with_long_critical_section)

        self.assertEqual(self.count, 100_000 * 10)


class SemaphoreSquareTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.semaphore = Semaphore()
        self.numbers = []
        self.result = []

    def square(self):
        while True:
            with self.semaphore:
                if self.numbers:
                    self.result.append(self.numbers.pop(0) ** 2)
                else:
                    return

    def test_1_number_one_thread(self):
        self.numbers.append(104)

        run_threads(1, self.square)

        self.assertEqual(self.result, [104 ** 2])

    def test_1_number_10_threads(self):
        self.numbers.append(172)

        run_threads(10, self.square)

        self.assertEqual(self.result, [172 ** 2])

    def test_many_numbers_1_thread(self):
        self.numbers.extend(range(100_000))

        run_threads(1, self.square)

        self.assertEqual(self.result, list(map(lambda x: x ** 2, range(100_000))))

    def test_many_numbers_10_thread(self):
        self.numbers.extend(range(100_000))

        run_threads(10, self.square)

        self.assertEqual(self.result, list(map(lambda x: x ** 2, range(100_000))))
