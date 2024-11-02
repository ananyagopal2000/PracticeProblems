"""
Count leaf nodes usig post order traversal. increase count when both left and right child is not present for a node. 
calculate this for both left and right subtree and return the sum of it to the parent 
"""

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree_Operations:
    def CreateTree(self):
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

class CountLeafNodes:
    def __init__(self):
        pass
    
    def count_leaf_nodes(self, root):
        if root==None:
            return 0
        
        if root.left==None and root.right==None:
            return 1
        
        left=self.count_leaf_nodes(root.left)
        right=self.count_leaf_nodes(root.right)
        return left+right
