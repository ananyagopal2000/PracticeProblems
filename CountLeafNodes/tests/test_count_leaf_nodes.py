import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from count_leaf_nodes import Tree_Operations, CountLeafNodes
import unittest

class TestTreeOperations(unittest.TestCase):
    def test_count_leaf_nodes(self):
        tree_operations = Tree_Operations()  # Creating an instance of Tree_Operations
        root = tree_operations.CreateTree()  # Calling CreateTree on the instance
        
        count_leaves = CountLeafNodes()
        self.assertEqual(count_leaves.count_leaf_nodes(root), 4)
        # print(CountLeafNodes.count_leaf_nodes(root))