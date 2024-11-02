import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from min_stack import MinStack, MinStack_II

class TestMinStack(unittest.TestCase):
    def test_min_stack_operations(self):
        stack = MinStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(-1)
        stack.push(4)
        stack.push(5)
        stack.push(0)
        self.assertEqual(stack.getMin(), -1, "Minimum after pushing elements should be -1")

        # Test pop and getMin to verify minimum updates correctly
        stack.pop()  # Pops 2
        self.assertEqual(stack.getMin(), -1, "Minimum should still be -1 after popping top")
        stack.pop()  # Pops 1
        stack.pop()  # Pops 2
        self.assertEqual(stack.getMin(), -1, "Minimum should still be -1 after popping another element")
        
        stack.pop()  # Pops -1
        self.assertEqual(stack.getMin(), 1, "Minimum should update to 1 after popping -1")

        # Test top operation
        self.assertEqual(stack.top(), 3, "Top element should be 3")

    def test_min_stack_II_operations(self):
        stack = MinStack_II()

        # Test push operations and getMin with duplicates and negatives
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(-1)
        stack.push(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.getMin(), -1, "Minimum after pushing elements should be -1")

        stack.pop()  # Pops 2
        self.assertEqual(stack.getMin(), -1, "Minimum should still be -1 after popping top")
        stack.pop()  # Pops 1
        stack.pop()  # Pops 2
        self.assertEqual(stack.getMin(), -1, "Minimum should still be -1 after popping another element")
        
        stack.pop()  # Pops -1
        self.assertEqual(stack.getMin(), 1, "Minimum should update to 1 after popping -1")

        # Test top operation
        self.assertEqual(stack.top(), 3, "Top element should be 3")

if __name__ == "__main__":
    unittest.main()