# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Mar 13, 2025

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@editor: eyuen
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # Check for valid input: all sides must be integers between 1 and 200
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Check for valid triangle (Triangle Inequality Theorem)
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    # Check for right triangle using Pythagorean Theorem
    sides = sorted([a, b, c])  # Sort to ensure correct order
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'

    # Check for equilateral triangle
    if a == b == c:
        return 'Equilateral'
    
    # Check for isosceles triangle
    if a == b or b == c or a == c:
        return 'Isosceles'

    # If no sides are equal, it's a scalene triangle
    return 'Scalene'
