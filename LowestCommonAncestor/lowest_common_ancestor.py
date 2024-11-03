"""
Iterate through the tree and check if node value is either p or q, if its either one of them return the node. if for a node, both
left node and right node is present then return the node, otherwise return left node is left is present else right node.
"""
import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class TreeOperations:
    def CreateTree1(self):
        TreeNode1 =TreeNode(1)
        TreeNode2 = TreeNode(2)
        TreeNode3 = TreeNode(3)
        TreeNode4 = TreeNode(4)
        TreeNode5 = TreeNode(5)
        TreeNode6 = TreeNode(6)
        TreeNode7 = TreeNode(7)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6
        TreeNode3.right = TreeNode7

        return TreeNode1

class LowestCommonAncestor(unittest.TestCase):
    def __init__(self, root):
        self.root=root

    def lowest_common_ancestor(self, root, p, q):
        if self.root==None:
            return
        
        if self.root.val==p or self.root.val==q:
            return root
        
        left=LowestCommonAncestor(self.root.left, p, q)
        right=LowestCommonAncestor(self.root.right, p, q)

        if left and right:
            return self.root.val
        
        return left if left else right
    
    


