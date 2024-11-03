import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from lowest_common_ancestor import TreeNode, TreeOperations, LowestCommonAncestor

class TestLowestCommonAncestor(unittest.TestCase):
    
    def test_lowest_common_ancestor(self):
        tree_op=TreeOperations()
        root=tree_op.CreateTree1()
        lca=LowestCommonAncestor(root)
        self.assertEqual(lca.lowest_common_ancestor(root, 4, 5), 2)

        self.assertEqual(lca.lowest_common_ancestor(root, 6, 5), 1)

        self.assertEqual(lca.lowest_common_ancestor(root, 6, 5), 3)

if __name__=='__main__':
    unittest.main()