# -*- coding: utf-8 -*-
"""
Updated Mar 13, 2025
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@editor: eyuen
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # Test cases for right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')
    
    # Test case for equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')
    
    # Test cases for isosceles triangles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')
    
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(7, 7, 10), 'Isosceles', '7,7,10 should be isosceles')
    
    # Test cases for scalene triangles
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(7, 9, 11), 'Scalene', '7,9,11 should be scalene')
    
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(13, 14, 15), 'Scalene', '13,14,15 should be scalene')
    
    # Test cases for invalid triangles
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')
    
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 is not a triangle')
    
    # Test cases for invalid inputs
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput', '-1,5,5 should be invalid')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(5.5, 5, 5), 'InvalidInput', '5.5,5,5 should be invalid')
    
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 should be invalid')
    
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(201, 199, 198), 'InvalidInput', '201,199,198 should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

