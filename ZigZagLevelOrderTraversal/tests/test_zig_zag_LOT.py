import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from zigzagLOT import TreeNode, TreeOperations, ZigZagLOT

class TestZigZagLevelOrderTraversal(unittest.TestCase):
    def test_std_bin_tree(self):
        tree_op = TreeOperations()
        root = tree_op.CreateTree()
        zigzag_level_order_trav = ZigZagLOT(root)
        self.assertEqual(zigzag_level_order_trav.zigzagLOT(), [[1],[3,2],[4,5,6,7]])