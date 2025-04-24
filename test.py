import unittest
from lab_5 import find_min_depth

class TestMinDepth(unittest.TestCase):

    def test_single_node(self):
        graph = {}
        root = 1
        self.assertEqual(find_min_depth(root, graph), 1)

    def test_linear_tree(self):
        graph = {
            1: [2],
            2: [3],
            3: [4]
        }
        root = 1
        self.assertEqual(find_min_depth(root, graph), 4)

    def test_balanced_tree(self):
        graph = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7]
        }
        root = 1
        self.assertEqual(find_min_depth(root, graph), 3)

    def test_early_leaf(self):
        graph = {
            1: [2, 3],
            2: [],
            3: [4]
        }
        root = 1
        self.assertEqual(find_min_depth(root, graph), 2)

    def test_disconnected_node(self):
        graph = {
            1: [2],
            2: [3]
        }
        root = 1
        self.assertEqual(find_min_depth(root, graph), 3)

if __name__ == '__main__':
    unittest.main()