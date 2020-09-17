# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,7,8),'Scalene','5,7,8 should be scalene')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(5,4,4),'Isosceles','5,4,4 should be isoceles')

    def testInvalid(self):
        self.assertEqual(classifyTriangle(677,432,300),"InvalidInput","677,432,300 should be Invalid")

    def testInvalid(self):
        self.assertEqual(classifyTriangle(-5,4,6),"InvalidInput","-5,4,6 should be Invalid")

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5,6,14),"NotATriangle","5,6,14 should be Invalid")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

