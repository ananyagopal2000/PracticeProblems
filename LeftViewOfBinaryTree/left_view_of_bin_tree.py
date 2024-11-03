"""
We iterate through the tree in preorder manner and simultaneuosly calculate the height of the tree at every level, We prioritize
going t the left nodes first and when the height is not present in the dictionary, where we are saving the first left node at that
particular level, we append it to the dictionary. If the height is already present in the dictionary, we do not append anything
to it. Once the tree traversal is done, we return the list of values we have saved in the dictionary at each level of the tree
"""
# Get all the elements of a tree when viewed from left.

# Case 1:		(root, 0)	{0:, 1:, 2:, 3:}
# 			   5
# ->   6 (1)		  8(1)
#  3 (2)	    4(2)         1
# 			 4        5	

# Output: [5, 6, 3, 4]

# Case  2:
# 			5
#   ->				8
#  	            2 		1

# Output: [5, 8, 2]

# Case 3:
#               5
#   ->		6		8
#  	    3          2 		1

# Output: [5, 6, 3]

# Case 4:
# 5 
# 8 
# 1
# Output: [5, 8, 1]

# Case 5: 	
# 			5 

# Output: [5]

import unittest

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class TreeOperations:
    def CreateTree1():
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
    
    def CreateTree2():
        TreeNode1 = TreeNode(5)
        TreeNode2 = TreeNode(6)
        TreeNode3 = TreeNode(8)
        TreeNode4 = TreeNode(3)
        TreeNode5 = TreeNode(4)
        TreeNode6 = TreeNode(1)
        TreeNode7 = TreeNode(4)
        TreeNode8 = TreeNode(9)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.right = TreeNode6
        TreeNode6.left = TreeNode7
        TreeNode6.right = TreeNode8
        
        return TreeNode1
    
    def CreateTree3():
        TreeNode1 =TreeNode(5)
        TreeNode2 = TreeNode(8)
        TreeNode3 = TreeNode(2)
        TreeNode4 = TreeNode(1)

        TreeNode1.right=TreeNode2
        TreeNode2.left=TreeNode3
        TreeNode2.right=TreeNode4

        return TreeNode1
    
    def CreateTree4():
        TreeNode1 =TreeNode(5)
        TreeNode2 = TreeNode(8)
        TreeNode3 = TreeNode(1)

        TreeNode1.right=TreeNode2
        TreeNode2.right=TreeNode3

        return TreeNode1

class LeftViewOfBST(unittest.TestCase):
    def __init__(self, root):
        self.root=root
           
    def left_view_of_BST(self, root):
        self.dict={}
        def helper(root, height):
            if not root:
                return None
            
            elif height not in self.dict:
                self.dict[height]=root.val 

            helper(root.left, height+1)
            helper(root.right, height+1)
        
        helper(root, 0)
        # print(self.dict)
        return [self.dict[height] for height in self.dict]

        
            



# Case 1:		(root, 0)	{0:, 1:, 2:, 3:}
# 			   5
# ->   6 (1)		  8(1)
#  3 (2)	 4(2)           1
# 			           4        5	