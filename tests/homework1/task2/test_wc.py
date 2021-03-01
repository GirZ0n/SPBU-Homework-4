import os
import unittest
from homework.homework1.task2.wc import get_file_information

FOLDER_PATH = f"{os.path.dirname(__file__)}/resources"


class WcTestCase(unittest.TestCase):
    def test_empty_file(self):
        with open(f"{FOLDER_PATH}/empty.txt") as f:
            info = get_file_information(f)
            self.assertEqual(info.number_of_lines, 0)
            self.assertEqual(info.number_of_words, 0)
            self.assertEqual(info.number_of_bytes, 0)

    def test_one_line_one_word(self):
        with open(f"{FOLDER_PATH}/one_line_one_word.txt") as f:
            info = get_file_information(f)
            self.assertEqual(info.number_of_lines, 1)
            self.assertEqual(info.number_of_words, 1)
            self.assertEqual(info.number_of_bytes, 5)

    def test_one_line_a_lot_of_words(self):
        with open(f"{FOLDER_PATH}/one_line_a_lot_of_words.txt") as f:
            info = get_file_information(f)
            self.assertEqual(info.number_of_lines, 1)
            self.assertEqual(info.number_of_words, 5)
            self.assertEqual(info.number_of_bytes, 64)

    def test_many_lines(self):
        with open(f"{FOLDER_PATH}/many_lines.txt") as f:
            info = get_file_information(f)
            self.assertEqual(info.number_of_lines, 13)
            self.assertEqual(info.number_of_words, 7)
            self.assertEqual(info.number_of_bytes, 163)
