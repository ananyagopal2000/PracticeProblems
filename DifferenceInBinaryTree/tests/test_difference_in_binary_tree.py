import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from difference_in_binary_tree import Tree_Operations, CountDifferenceInTrees

class TestDifferenceinbinarytree(unittest.TestCase):
    def test_no_difference(self):
        # tree_op=Tree_Operations
        root1=Tree_Operations.CreateTree1()
        root2=Tree_Operations.CreateTree1()
        counter=CountDifferenceInTrees()
        self.assertEqual(counter.count_differences(root1, root2), 0)

    def test_one_difference(self):
        # tree_op=Tree_Operations
        root1=Tree_Operations.CreateTree1()
        root2=Tree_Operations.CreateTree2()
        counter=CountDifferenceInTrees()     #(root1, root2)
        self.assertEqual(counter.count_differences(root1, root2), 1)

    def test_different_structure(self):
        # tree_op=Tree_Operations
        root1=Tree_Operations.CreateTree1()
        root2=Tree_Operations.CreateTree3()
        counter=CountDifferenceInTrees()
        self.assertEqual(counter.count_differences(root1,root2),-1)

    def test_multiple_differences(self):
        # tree_op=Tree_Operations
        root1=Tree_Operations.CreateTree1()
        root2=Tree_Operations.CreateTree4()
        counter=CountDifferenceInTrees()
        self.assertEqual(counter.count_differences(root1,root2),3)

if __name__=='__main__':
    unittest.main()