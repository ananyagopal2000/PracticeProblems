"""
Traverse throught the tree, starting from root, if node is present, append the node value to the stack. if node is not present,
pop the stack and append the value to the result array and search for the right node and continue the process until the stack is empty.
"""
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right   

class TreeTraversal(unittest.TestCase):
    def __init__(self, root):
        self.root=root
        self.stack=[]
        self.res=[]

    def inorder_traversal(self):
        current=self.root 
        while current or self.stack:       
            while current :
                self.stack.append(current)
                current=current.left
            
            current=self.stack.pop()
            self.res.append(current.val)
            current=current.right

        return self.res