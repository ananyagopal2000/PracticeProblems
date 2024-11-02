import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from path_finder import PathFinder

class TestPathFinder(unittest.TestCase):
    def test_valid_matrix(self):
        matrix=[[1,1,0,0],[1,1,1,1],[0,0,1,1]]
        self.assertEqual(PathFinder.matrix_validity(matrix), True)

    def test_invalid_start_matrix(self):
        matrix=[[0,1,0,0],[1,1,1,1],[0,0,1,1]]
        self.assertEqual(PathFinder.matrix_validity(matrix), False)

    def test_invalid_end_matrix(self):
        matrix=[[1,1,0,0],[1,1,1,1],[0,0,1,0]]
        self.assertEqual(PathFinder.matrix_validity(matrix), False)