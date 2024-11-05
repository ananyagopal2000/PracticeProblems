import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from level_order_traversal import TreeNode, TreeOperations, LevelOrderTraversal

class TestLevelOrderTraversal(unittest.TestCase):
    def test_std_bin_tree(self):
        tree_op = TreeOperations()
        root = tree_op.CreateTree()
        level_order_trav = LevelOrderTraversal(root)
        self.assertEqual(level_order_trav.LevelOrder(), [[1],[2,3],[4,5,6,7]])


