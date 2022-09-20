import unittest
import triangle as tri

class Test_type(unittest.TestCase):
    def test_right_triangle(self):
        self.test_triangle1 = tri.triangle(12,15,9)
        self.test_triangle2 = tri.triangle(15,12,9)
        self.test_triangle3 = tri.triangle(12,9,15)
        self.assertEqual("Right triangle", self.test_triangle1.type)
        self.assertEqual("Right triangle", self.test_triangle2.type)
        self.assertEqual("Right triangle", self.test_triangle3.type)


    def test_equalateral_triangle(self):
        self.test_triangle = tri.triangle(5,5,5)
        self.assertEqual("Equilateral triangle", self.test_triangle.type)

    def test_invalid(self):
        self.test_triangle = tri.triangle(0,0,-2)
        self.assertEqual("Invalid triangle", self.test_triangle.type)

class Test_valid(unittest.TestCase):
    def test_not_valid_if_all_zeros(self):
        self.test_triangle = tri.triangle(0,0,0)
        self.assertEqual(False, self.test_triangle.is_valid())

    def test_not_valid_if_all_negatives(self):
        self.test_triangle = tri.triangle(-1,-1,-1)
        self.assertFalse(self.test_triangle.is_valid())

    def test_not_valid_if_one_negative(self):
        self.test_triangle1 = tri.triangle(1,1,-1)
        self.test_triangle2 = tri.triangle(-1,1,1)
        self.test_triangle3 = tri.triangle(1,-1,1)
        self.assertFalse(self.test_triangle1.is_valid())
        self.assertFalse(self.test_triangle2.is_valid())
        self.assertFalse(self.test_triangle3.is_valid())

    def test_not_valid_if_two_negative(self):
        self.test_triangle1 = tri.triangle(-1,1,-1)
        self.test_triangle2 = tri.triangle(-1,-1,1)
        self.test_triangle3 = tri.triangle(1,-1,-1)
        self.assertFalse(self.test_triangle1.is_valid())
        self.assertFalse(self.test_triangle2.is_valid())
        self.assertFalse(self.test_triangle3.is_valid())

    def test_valid(self):
        self.test_triangle1 = tri.triangle(3,3,3)
        self.assertTrue(self.test_triangle1.is_valid())

class Test_area(unittest.TestCase):
    def test_area(self):
        self.test_triangle1 = tri.triangle(9,12,15)
        self.assertEqual(54, self.test_triangle1.area)
    