"""
count_differences: given two trees, if there is a difference in value, return 1. check for left nodes in both trees and if any of 
them returns a -1, return a -1. calculate difference if there is a difference in value in the trees. then return the current 
difference along with left and right from every node to the parent.
"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree_Operations:
    @staticmethod
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
    
    @staticmethod
    def CreateTree2():
        TreeNode1 =TreeNode(1)
        TreeNode2 = TreeNode(2)
        TreeNode3 = TreeNode(3)
        TreeNode4 = TreeNode(4)
        TreeNode5 = TreeNode(5)
        TreeNode6 = TreeNode(6)
        TreeNode7 = TreeNode(10)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6
        TreeNode3.right = TreeNode7

        return TreeNode1   
    
    @staticmethod
    def CreateTree3():
        TreeNode1 =TreeNode(1)
        TreeNode2 = TreeNode(2)
        TreeNode3 = TreeNode(3)
        TreeNode4 = TreeNode(4)
        TreeNode5 = TreeNode(5)
        TreeNode6 = TreeNode(6)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6

        return TreeNode1  
    
    @staticmethod
    def CreateTree4():
        TreeNode1 =TreeNode(1)
        TreeNode2 = TreeNode(2)
        TreeNode3 = TreeNode(3)
        TreeNode4 = TreeNode(4)
        TreeNode5 = TreeNode(15)
        TreeNode6 = TreeNode(9)
        TreeNode7 = TreeNode(10)

        TreeNode1.left= TreeNode2
        TreeNode1.right= TreeNode3
        TreeNode2.left = TreeNode4
        TreeNode2.right = TreeNode5
        TreeNode3.left = TreeNode6
        TreeNode3.right = TreeNode7

        return TreeNode1   

class CountDifferenceInTrees:
    # def __init__(self, root1, root2):
    #     self.root1=root1
    #     self.root2=root2

    def count_differences(self, root1, root2):
        if not root1 and not root2:
            return 0
        
        if (not root1 and root2) or (root1 and not root2):
            return -1
        
        left_diff=self.count_differences(root1.left, root2.left)
        if left_diff==-1:
            return -1
        
        right_diff=self.count_differences(root1.right, root2.right)
        if right_diff==-1:
            return -1
        
        current_diff=0
        if root1 and root2 and root1.val!=root2.val:
            current_diff+=1

        return left_diff + right_diff + current_diff

    def count_differences_II(self):
        if not self.root1 and not self.root2:
            return 0
        
        if (not self.root1 and self.root2) or (self.root1 and not self.root2):
            return 1  
                    
        leftdiff=self.count_differences_II(self.root1.left, self.root2.left)

        if leftdiff%2==0 and self.root1 and self.root2:
            leftdiff+=2             
        
        rightdiff=self.count_differences_II(self.root1.right, self.root2.right)

        if rightdiff%2==0 and self.root1 and self.root2:
            rightdiff+=2

        currentdiff=0
        if self.root1.val!=self.root2.val:
            currentdiff+=2

        return rightdiff + leftdiff + currentdiff


#       1
#    2     3
#  4   5 6   7
# 8  9

#      1
#    2   3
#  4   5
# op: 2

#      1
#    2   
#  4   5
# op: 3


#       1
#    2     3
#  4   5 6   7
# 8  10
# op: 2
