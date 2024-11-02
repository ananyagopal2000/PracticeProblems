"""
check for validity of the array, the array should neither be strictly increassing or strinctly decreasing. if it is, return False. 
to find peak, use binary search technique to find a mid elemnt and check for array[mid-1]<array[mid] and array[mid+1]<array[mid] . 
if so return the mid element, else if array[mid]>array[mid-1] and array[mid]>array[mid+1], increment the left pointer else 
increment right pointer 
"""

class Peakelement:
    def __init__(self, array):
        self.array=array

    def array_validity(self):        
        if len(self.array)<2:
            return False
        elif self.array[0]>self.array[1]:
            return False
        elif self.array[0]<self.array[1] and self.array[-1]>self.array[-2]:
            return False        
        else:
            return self.find_peak_element()

    def find_peak_element(self):
        l, r=0, len(self.array)

        while l<=r:
            mid=(l+r)//2
            if self.array[mid]>self.array[mid-1] and self.array[mid]>self.array[mid+1]:
                l=mid+1
            
            if self.array[mid]<self.array[mid-1] and self.array[mid]>self.array[mid+1]:
                r=mid-1

            if self.array[mid-1]<self.array[mid] and self.array[mid+1]<self.array[mid]:
                return self.array[mid]
            
