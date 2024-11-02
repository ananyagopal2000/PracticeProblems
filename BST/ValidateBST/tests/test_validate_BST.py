import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from validate_BST import Tree_Operations, IsBST

class TestIsBST(unittest.TestCase):
    def test_a_BST(self):
        tree_op=Tree_Operations()
        root1=tree_op.CreateTree1()
        is_BST=IsBST()
        self.assertEqual(is_BST.isBST(root1), True)

    def test_a_nonBST(self):
        tree_op=Tree_Operations()
        root2=tree_op.CreateTree2()
        is_BST=IsBST()
        self.assertFalse(is_BST.isBST(root2), False)


