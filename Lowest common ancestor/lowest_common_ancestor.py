"""
Iterate through the tree and check if node value is either p or q, if its either one of them return the node. if for a node, both
left node and right node is present then return the node, otherwise return left node is left is present else right node.
"""
import unittest
class TreeNode(unittest.TestCase):
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class LowestCommonAncestor(unittest.TestCase):
    def __init__(self):
        pass

    def lowest_common_ancestor(root, p, q):
        if root==None:
            return
        
        if root.val==p or root.val==q:
            return root
        
        left=LowestCommonAncestor(root.left, p, q)
        right=LowestCommonAncestor(root.right, p, q)

        if left and right:
            return root.val
        
        return left if left else right
    
    


