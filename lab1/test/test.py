import unittest

from src.lab1 import find_kth_largest


class Test(unittest.TestCase):
    def test_find_kth_largest(self):
        input_array = [15, 7, 22, 9, 36, 2, 42, 18]
        k_value = 3
        result, index = find_kth_largest(input_array, k_value)
        self.assertEqual(result, 9)
        self.assertEqual(index, 3)

        input_array = []
        k_value = 2
        result, index = find_kth_largest(input_array, k_value)
        self.assertIsNone(result)
        self.assertIsNone(index)

        input_array = [15, 7, 22, 9, 36, 2, 42, 18]
        k_value = 0
        result, index = find_kth_largest(input_array, k_value)
        self.assertIsNone(result)
        self.assertIsNone(index)

        input_array = [15, 7, 22, 9, 36, 2, 42, 18]
        k_value = 9
        result, index = find_kth_largest(input_array, k_value)
        self.assertIsNone(result)
        self.assertIsNone(index)


if __name__ == '__main__':
    unittest.main()
