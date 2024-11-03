"""
Firstly, we need to check the matrix validity: 1. if the matrix is empty, or the first element in the matrix=0 or the (m-1 and n-1)th
element in the matrix is a 0, return false-cannot find path. 
Once the initial checks are satisfied, we can start from the first element and do dfs by simultaneously calling both the vertical
and horizontal elements until one of them reach the element at matrix[m-1][n-1], if this element is a 1 return True!
"""
import unittest

class PathFinder:
    def __init__(self, matrix):
        self.matrix=matrix
        self.m=-1
        self.n=-1
        if self.matrix!=None or len(self.matrix)!=0:
            self.m=len(self.matrix)
            self.n=len(self.matrix[0])
    
    def matrix_validity(self):
        if self.matrix[0][0]==0 or self.matrix[self.m-1][self.n-1]==0:
            return False
        
        elif self.m<0 or self.n<0:
            return False
        
        else:
            return self.pathfinder(0,0)

    def pathfinder(self, x, y):
        if x>self.m-1 or y>self.n-1 or x<0 or y<0:
            return False
        
        if self.matrix[x][y]==0:
            return False        
                
        if x==self.m-1 and y==self.n-1 and self.matrix[x][y]==1:
            return True
        
        return self.pathfinder(x+1,y) or self.pathfinder(x, y+1)