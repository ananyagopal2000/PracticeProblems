"""
In a BST, since all the smaller elements are always on the left side of the tree, we can assume that the smallest element would
be the leftmost leaf node present in the tree. So upon recursively calling for the left subtree we return the leftmost node 
with no left cheild present
"""

import unittest

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class TreeOperations:
    def CreateTree(self):
        TreeNode1 =TreeNode(10)
        TreeNode2 = TreeNode(7)
        TreeNode3 = TreeNode(12)
        TreeNode4 = TreeNode(5)
        TreeNode5 = TreeNode(8)
        TreeNode6 = TreeNode(11)
        TreeNode7 = TreeNode(13)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6
        TreeNode3.right = TreeNode7

        return TreeNode1
    
class MinValueBST:
    def __init__(self, root):
        self.root=root
        
    def is_BST(self):
        def helper(root, left, right):
            if not root:
                return True
            
            if not (root.val>left and root.val<right):
                return False
            
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        return helper(self.root, float("-inf"), float("inf"))

    def get_in_value_BST(self):
        if not self.root:
            return -1
        
        if not self.root.left:
            return self.root.val
        
        self.root=self.root.left
        return self.get_in_value_BST()
    
    def get_min_val(self):
        if self.is_BST():
            return self.get_in_value_BST()
        else:
            return 'The binary tree is not a BST, so cannot find the minimum value.'