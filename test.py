import unittest
from lab_4 import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Task A", 2)
        self.pq.insert("Task B", 5)
        self.pq.insert("Task C", 3)
        self.assertEqual(self.pq.peek().value, "Task B")

    def test_extract_max(self):
        self.pq.insert("Low", 1)
        self.pq.insert("High", 10)
        self.pq.insert("Medium", 5)

        self.assertEqual(self.pq.extract_max().value, "High")
        self.assertEqual(self.pq.extract_max().value, "Medium")
        self.assertEqual(self.pq.extract_max().value, "Low")
        self.assertIsNone(self.pq.extract_max())

    def test_order_with_equal_priorities(self):
        self.pq.insert("Task A", 5)
        self.pq.insert("Task B", 5)
        self.pq.insert("Task C", 5)

        for _ in range(3):
            node = self.pq.extract_max()
            self.assertEqual(node.priority, 5)

    def test_peek_empty(self):
        self.assertIsNone(self.pq.peek())

    def test_extract_empty(self):
        self.assertIsNone(self.pq.extract_max())


if __name__ == "__main__":
    unittest.main()
