import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab_9 import find_max_chain

class TestFindMaxChain(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        self.output_dir = os.path.join(base_dir, "output")
        os.makedirs(self.output_dir, exist_ok=True)

        self.input1 = os.path.join(base_dir, "input", "wchain_test_1.in")
        self.input2 = os.path.join(base_dir, "input", "wchain_test_2.in")
        self.input3 = os.path.join(base_dir, "input", "wchain_test_3.in")

        self.output1 = os.path.join(self.output_dir, "output_test_1.out")
        self.output2 = os.path.join(self.output_dir, "output_test_2.out")
        self.output3 = os.path.join(self.output_dir, "output_test_3.out")


    def test_case_1(self):
        find_max_chain(self.input1, self.output1)
        with open(self.output1, 'r', encoding='utf-8') as f:
            self.assertEqual(int(f.read().strip()), 6)

    def test_case_2(self):
        find_max_chain(self.input2, self.output2)
        with open(self.output2, 'r', encoding='utf-8') as f:
            self.assertEqual(int(f.read().strip()), 4)

    def test_case_3(self):
        find_max_chain(self.input3, self.output3)
        with open(self.output3, 'r', encoding='utf-8') as f:
            self.assertEqual(int(f.read().strip()), 1)

if __name__ == '__main__':
    unittest.main()
