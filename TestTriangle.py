# -*- coding: utf-8 -*-
import unittest

from Triangle import classifyTriangle
class TestTriangles(unittest.TestCase):
def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(5,6,1),'Scalene','5,6,1 is a obtuse triangle')

def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,7,4),'Scalene','5,7,4 is a obtuse triangle')
        
def testEquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(1,1,1),'isocles','1,1,1 should be isocles')
A = input ("Enter side A")

B = input ("Enter side B")

C = input ("Enter side C")

if A == B == C:
	print("Equal Sides")
	pass
elif A == B or B == C or C == A:
	print("Isocles")
	pass
else:
	print ("Scalene")
	pass

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


