"""
Analyzed 10/07/2020 by Kristin Kim
py -m pylint (filename)
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    """
    This code implements the unit test functionality
    """

    def test_right_triangle(self):
        """
            input right triangle to verify
            functionality of right triangle checker
        """
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')


    def test_equilateral_triangles(self):
        """
            input equilateral to verify
            functionality of equilateral triangle checker
        """
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')


    def test_scalene_triangles(self):
        """
            input scalene to verify
            functionality of scalene triangle checker
        """
        self.assertEqual(classifyTriangle(5, 7, 8), 'Scalene', '5,7,8 should be scalene')

    def test_isosceles_triangles(self):
        """
             input isosceles to verify
             functionality of isosceles triangle checker
        """
        self.assertEqual(classifyTriangle(5, 4, 4), 'Isosceles', '5,4,4 should be isosceles')

    def test_invalid(self):
        """
            input large / negative dimension to verify
            functionality of invalid value checker
        """
        self.assertEqual(classifyTriangle(677, 432, 300), "InvalidInput", "677,432,300 is Invalid")
        self.assertEqual(classifyTriangle(-5, 4, 6), "InvalidInput", "-5,4,6 is Invalid")

    def test_not_triangle(self):
        """
            that can't connected
        :return: notify input is invalid
        """
        self.assertEqual(classifyTriangle(5, 6, 14), "NotATriangle", "5,6,14 should be Invalid")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
