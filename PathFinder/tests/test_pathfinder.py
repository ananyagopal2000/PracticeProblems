import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from path_finder import PathFinder

class TestPathFinder(unittest.TestCase):
    def test_valid_matrix(self):
        matrix=[[1,1,0,0],[1,1,1,1],[0,0,1,1]]
        path_finder = PathFinder(matrix)
        self.assertEqual(path_finder.matrix_validity(), True)

    def test_invalid_start_matrix(self):
        matrix=[[0,1,0,0],[1,1,1,1],[0,0,1,1]]
        path_finder = PathFinder(matrix)
        self.assertEqual(path_finder.matrix_validity(), False)

    def test_invalid_end_matrix(self):
        matrix=[[1,1,0,0],[1,1,1,1],[0,0,1,0]]
        path_finder = PathFinder(matrix)
        self.assertEqual(path_finder.matrix_validity(), False)