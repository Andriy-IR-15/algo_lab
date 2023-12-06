import unittest

from src.main import read_file, group_by_tribe, count_possible_pairs


class TestTribesFunctions(unittest.TestCase):

    def test_read_file(self):
        file_path = "test/input.txt"
        tribes, mans, women = read_file(file_path)

        self.assertEqual(len(tribes), ...)
        self.assertEqual(len(mans), ...)
        self.assertEqual(len(women), ...)

    def test_group_by_tribe(self):
        tribes = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2}
        mans = {1, 2, 4}
        women = {3, 5}
        tribe_groups = group_by_tribe(tribes, mans, women)

        self.assertEqual(len(tribe_groups["mans"]), ...)
        self.assertEqual(len(tribe_groups["women"]), ...)

    def test_count_possible_pairs(self):
        tribe_groups = {
            "mans": {0: [1, 2], 1: [3, 4]},
            "women": {2: [5, 6]}
        }
        count, possible_pairs = count_possible_pairs(tribe_groups)

        self.assertEqual(count, ...)
        self.assertEqual(len(possible_pairs), ...)


if __name__ == '__main__':
    unittest.main()
