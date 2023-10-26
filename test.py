import unittest

from main import minEatingSpeed


class TestMinEatingSpeed(unittest.TestCase):

    def test_case1(self):
        piles1 = [3, 6, 7, 11]
        H1 = 8
        self.assertEqual(minEatingSpeed(piles1, H1), 4)

    def test_case2(self):
        piles2 = [30, 11, 23, 4, 20]
        H2 = 5
        self.assertEqual(minEatingSpeed(piles2, H2), 30)

    def test_case3(self):
        piles3 = [30, 11, 23, 4, 20]
        H3 = 6
        self.assertEqual(minEatingSpeed(piles3, H3), 23)

if __name__ == '__main__':
    unittest.main()
