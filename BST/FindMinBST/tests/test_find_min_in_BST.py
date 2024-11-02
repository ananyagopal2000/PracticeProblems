import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from find_min_in_BST import MinValueBST, TreeOperations, TreeNode

class TestMinValueInBST(unittest.TestCase):
    # def test_standard_BST(self):
    #     tree_op = TreeOperations()
    #     root = tree_op.CreateTree()
    #     # min_value = MinValueBST(root)
    #     self.assertEqual(MinValueBST(root), 3)  # Expected minimum value is 3

    def test_valid_bst(self):
        tree_op=TreeOperations()
        root=tree_op.CreateTree()
        bst = MinValueBST(root)
        self.assertEqual(bst.get_min_val(), 5)

    def test_single_node(self):
        root=TreeNode(30)
        bst = MinValueBST(root)
        self.assertEqual(bst.get_min_val(), 30)  # Expected minimum value is 42

    def test_left_skewed_tree(self):
        # Left-skewed tree:
        #    10
        #   /
        #  5
        # /
        # 2
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(2)
        bst = MinValueBST(root)
        self.assertEqual(bst.get_min_val(), 2) 

    def test_right_skewed_tree(self):
        # Right-skewed tree:
        #  10
        #    \
        #    20
        #      \
        #      30
        root = TreeNode(10)
        root.right = TreeNode(20)
        root.right.right = TreeNode(30)
        bst = MinValueBST(root)
        self.assertEqual(bst.get_min_val(), 10) 

    def test_empty_tree(self):
        bst = MinValueBST(None)
        self.assertEqual(bst.get_min_val(), -1) #Expected None