import unittest
import homework.homework1.task2.wc as wc

path = "./resources"


class WcTestCase(unittest.TestCase):
    def test_empty_file(self):
        with open("resources/empty.txt", "r") as f:
            info = wc.get_file_information(f)
            self.assertEqual(info.number_of_lines, 0)
            self.assertEqual(info.number_of_words, 0)
            self.assertEqual(info.number_of_bytes, 0)

    def test_one_line_one_word(self):
        with open(f"{path}/one_line_one_word.txt", "r") as f:
            info = wc.get_file_information(f)
            self.assertEqual(info.number_of_lines, 1)
            self.assertEqual(info.number_of_words, 1)
            self.assertEqual(info.number_of_bytes, 5)

    def test_one_line_a_lot_of_words(self):
        with open("resources/one_line_a_lot_of_words.txt", "r") as f:
            info = wc.get_file_information(f)
            self.assertEqual(info.number_of_lines, 1)
            self.assertEqual(info.number_of_words, 5)
            self.assertEqual(info.number_of_bytes, 64)

    def test_many_lines(self):
        with open("resources/many_lines.txt", "r") as f:
            info = wc.get_file_information(f)
            self.assertEqual(info.number_of_lines, 13)
            self.assertEqual(info.number_of_words, 7)
            self.assertEqual(info.number_of_bytes, 163)
