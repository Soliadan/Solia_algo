import unittest
from lab_3 import BinaryTree, invert_binary_tree, pre_order

class TestInvertBinaryTree(unittest.TestCase):

    def test_invert_full_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        inverted_root = invert_binary_tree(root)
        expected_result = [1, 3, 7, 6, 2, 5, 4]
        self.assertEqual(pre_order(inverted_root), expected_result)

    def test_empty_tree(self):
        self.assertIsNone(invert_binary_tree(None))

    def test_single_node(self):
        root = BinaryTree(42)
        inverted_root = invert_binary_tree(root)
        self.assertEqual(pre_order(inverted_root), [42])

    def test_single_child_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        inverted_root = invert_binary_tree(root)
        self.assertEqual(pre_order(inverted_root), [1, 2])

    def test_two_level_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        inverted_root = invert_binary_tree(root)
        self.assertEqual(pre_order(inverted_root), [1, 3, 2])

if __name__ == "__main__":
    unittest.main()