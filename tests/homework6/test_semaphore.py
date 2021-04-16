import unittest
from threading import Thread

from tests.tests_utils import check_message

from homework.homework6.semaphore import Semaphore


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

    def test_incorrect_semaphore_size(self):
        with self.assertRaises(ValueError) as context:
            Semaphore(-206)

        self.assertTrue(check_message(context, "Semaphore initial size must be >= 0"))

    def test_increment_one_thread(self):
        tread = Thread(target=self.increment())

        tread.start()
        tread.join()

        self.assertEqual(self.count, 100_000)

    def test_increment_ten_threads(self):
        threads = [Thread(target=self.increment()) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(self.count, 100_000 * 10)

    def test_increment_with_long_critical_section_one_thread(self):
        tread = Thread(target=self.increment_with_long_critical_section())

        tread.start()
        tread.join()

        self.assertEqual(self.count, 100_000)

    def test_increment_with_long_critical_section_ten_threads(self):
        threads = [Thread(target=self.increment_with_long_critical_section()) for _ in range(10)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.assertEqual(self.count, 100_000 * 10)
