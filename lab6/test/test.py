import unittest

from src.lab6 import naive_string_search


class TestNaiveStringSearch(unittest.TestCase):

    def test_empty_strings(self):
        text = ""
        pattern = ""
        self.assertEqual(naive_string_search(text, pattern), (0, 0))

    def test_single_character_strings(self):
        text = "a"
        pattern = "a"
        self.assertEqual(naive_string_search(text, pattern), (0, 1))

        text = "b"
        pattern = "a"
        self.assertEqual(naive_string_search(text, pattern), (-1, 0))

    def test_simple_strings(self):
        text = "abcabc"
        pattern = "abc"
        self.assertEqual(naive_string_search(text, pattern), (0, 3))

        text = "abcabc"
        pattern = "bc"
        self.assertEqual(naive_string_search(text, pattern), (1, 2))

        text = "abcabc"
        pattern = "c"
        self.assertEqual(naive_string_search(text, pattern), (2, 1))

    def test_strings_with_multiple_matches(self):
        text = "abcabcabc"
        pattern = "abc"
        self.assertEqual(naive_string_search(text, pattern), (0, 3))
        self.assertEqual(naive_string_search(text, pattern), (4, 7))

    def test_strings_with_no_matches(self):
        text = "abcabc"
        pattern = "def"
        self.assertEqual(naive_string_search(text, pattern), (-1, 0))


if __name__ == "__main__":
    unittest.main()
