import unittest
import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class TreeOperations:
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

class LevelOrderTraversal:
    def __init__(self, root):
        self.root=root
        self.res=[]

    def LevelOrder(self):
        q=collections.deque()
        q.append(self.root)
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                self.res.append(level)
        return self.res
                
