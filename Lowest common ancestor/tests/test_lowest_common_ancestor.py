import unittest
from lowest_common_ancestor import TreeNode, LowestCommonAncestor

class TestLowestCommonAncestor(unittest.TestCase):
    def setup_tree(self):
        self.root=TreeNode(1)
        self.root.left=TreeNode(2)
        self.root.right=TreeNode(3)
        self.root.left.left=TreeNode(4)
        self.root.left.right=TreeNode(5)
        self.root.right.left=TreeNode(6)
        self.root.right.right=TreeNode(7)

    def test_lowest_common_ancestor(self):

        lca=LowestCommonAncestor.lowest_common_ancestor(self.root, 4, 5)
        self.assertEqual(lca.val, 2)

        lca=LowestCommonAncestor.lowest_common_ancestor(self.root, 6, 5)
        self.assertEqual(lca.val, 1)

        lca=LowestCommonAncestor.lowest_common_ancestor(self.root, 6, 7)
        self.assertEqual(lca.val, 3)

if __name__=='__main__':
    unittest.main()