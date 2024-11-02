import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from find_peak_element import Peakelement

class TestPeakElement(unittest.TestCase):

    def test_valid_array(self):
        arr=[1,2,3,4,5,4,3,2,1]
        peak=Peakelement(arr)
        self.assertEqual(peak.array_validity(), 5)

    def test_strictly_increasing(self):
        arr=[1,2,3,4,5]
        peak=Peakelement(arr)
        self.assertEqual(peak.array_validity(), False)

    def test_strictly_decreasing(self):
        arr=[5,4,3,2,1]
        peak=Peakelement(arr)
        self.assertEqual(peak.array_validity(), False)

    def test_short_array(self):
        arr=[1]
        peak=Peakelement(arr)
        self.assertEqual(peak.array_validity(), False)
    
    def test_empty_array(self):
        arr=[]
        peak=Peakelement(arr)
        self.assertEqual(peak.array_validity(), False)

if __name__=='__main__':
    unittest.main()
    
    