import unittest

from main import BinaryTree, invert_binary_tree


class TestBinaryTreeInversion(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        new_root = invert_binary_tree(root)

        self.assertEqual(new_root.value, 1)
        self.assertEqual(new_root.left.value, 3)
        self.assertEqual(new_root.right.value, 2)
        self.assertEqual(new_root.left.left.value, 7)
        self.assertEqual(new_root.left.right.value, 6)
        self.assertEqual(new_root.right.left.value, 5)
        self.assertEqual(new_root.right.right.value, 4)

    def test_invert_empty_tree(self):
        result = invert_binary_tree(None)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
