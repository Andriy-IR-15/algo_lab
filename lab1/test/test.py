import unittest

# Імпортуємо функцію find_kth_largest з вашого основного модуля (main.py).
from main import find_kth_largest

# Створюємо клас для тестування функції find_kth_largest.
class TestKthLargest(unittest.TestCase):

    # Тест для перевірки функції find_kth_largest для коректного виконання.
    def test_kth_largest(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        self.assertEqual(find_kth_largest(arr, 1), (42, 6))
        # Інші тести можна додавати аналогічним чином.

    # Тест для перевірки обробки некоректного значення k.
    def test_invalid_k(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        self.assertEqual(find_kth_largest(arr, 0), (None, None))
        # Інші тести можна додавати аналогічним чином.

if __name__ == '__main__':
    unittest.main()