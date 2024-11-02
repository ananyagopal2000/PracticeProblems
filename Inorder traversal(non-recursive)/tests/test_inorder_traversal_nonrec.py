import unittest
from inorder_traversal_nonrec import Tree, TreeTraversal

class TestInorderTraversalNRC(unittest.TestCase):
    def test_inorder(self):
        root=Tree(1,Tree(2), Tree(3))
        self.assertEqual(TreeTraversal.inorder_traversal(root), [2,1,3])

    def test_inorder_tree_unequal(self):
        root=Tree(1,Tree(2))
        self.assertEqual(TreeTraversal.inorder_traversal(root), [2,1])