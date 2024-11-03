import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from inorder_traversal_nonrec import TreeNode, TreeTraversal

class TestInorderTraversalNRC(unittest.TestCase):
    def test_inorder(self):
        root=TreeNode(1,TreeNode(2), TreeNode(3))
        tree_traversal=TreeTraversal(root)
        self.assertEqual(tree_traversal.inorder_traversal(), [2,1,3])

    def test_inorder_tree_unequal(self):
        root=TreeNode(1,TreeNode(2))
        tree_traversal=TreeTraversal(root)
        self.assertEqual(tree_traversal.inorder_traversal(), [2,1])