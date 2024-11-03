import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from LeftViewOfBinaryTree.left_view_of_bin_tree import TreeNode, TreeOperations, LeftViewOfBST

class TestLeftViewOfBinaryTree(unittest.TestCase):
    def test_standard_binary_tree(self):
        tree_op=TreeOperations
        root = tree_op.CreateTree1()
        left_view=LeftViewOfBST(root)
        # print(left_view.left_view_of_BST(root))
        self.assertEqual(left_view.left_view_of_BST(root), [1,2,4])

    def test_unstructured_binary_tree(self):
        tree_op=TreeOperations
        root1 = tree_op.CreateTree1()
        root2 = tree_op.CreateTree2()
        root3 = tree_op.CreateTree3()
        root4 = tree_op.CreateTree4()
        root5 = TreeNode(5)

        left_view1=LeftViewOfBST(root1)
        left_view2=LeftViewOfBST(root2)
        left_view3=LeftViewOfBST(root3)
        left_view4=LeftViewOfBST(root4)
        left_view5=LeftViewOfBST(root5)

        self.assertEqual(left_view1.left_view_of_BST(root1), [1,2,4])
        self.assertEqual(left_view2.left_view_of_BST(root2), [5,6,3,4])
        self.assertEqual(left_view3.left_view_of_BST(root3), [5,8,2])
        self.assertEqual(left_view3.left_view_of_BST(root4), [5,8,1])
        self.assertEqual(left_view4.left_view_of_BST(root5), [5])


    