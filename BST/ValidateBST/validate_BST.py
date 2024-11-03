"""
To check if a binary tree is a BST, we have to traverse through the tree and check if the root.val is lesser than root.left and
root.val is greater than root.right value. if this holds good for all the nodes in the tree, we can say its a BST. 
"""
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree_Operations:
    def CreateTree1(self):
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
    
          # 10
    # 7         12
# 5       8  11     13
   
    def CreateTree2(self):
        TreeNode1 =TreeNode(10)
        TreeNode2 = TreeNode(7)
        TreeNode3 = TreeNode(12)
        TreeNode4 = TreeNode(5)
        TreeNode5 = TreeNode(8)
        TreeNode6 = TreeNode(13)
        TreeNode7 = TreeNode(11)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6
        TreeNode3.right = TreeNode7

        return TreeNode1
 
    
         # 10
    # 7         12
# 5       8  13     11

class IsBST:
    def isBST(self, root):
        def helper(root, left, right):
            if not root:
                return True
            
            if not (root.val>left and root.val<right):
                return False
            
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        return helper(root, float("-inf"), float("inf"))