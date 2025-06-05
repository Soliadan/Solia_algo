import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab_8 import load_graph_from_csv



class TestCSVExamples(unittest.TestCase):

    def test_balanced_flow(self):
        graph = load_graph_from_csv(os.path.join(os.path.dirname(__file__), "balanced_flow.csv"))
        result = graph.max_total_flow()
        self.assertEqual(result, 7, "Expected max flow of 7 for balanced_flow.csv")

    def test_split_to_two_sinks(self):
        graph = load_graph_from_csv(os.path.join(os.path.dirname(__file__), "split_to_two_sinks.csv"))
        result = graph.max_total_flow()
        self.assertEqual(result, 9, "Expected max flow of 9 for split_to_two_sinks.csv")

    def test_bottleneck_between_middle(self):
        graph = load_graph_from_csv(os.path.join(os.path.dirname(__file__), "bottleneck_between_middle.csv"))
        result = graph.max_total_flow()
        self.assertEqual(result, 5, "Expected max flow of 5 for bottleneck_between_middle.csv")

if __name__ == "__main__":
    unittest.main()
