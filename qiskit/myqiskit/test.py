import unittest
from math import pi, e, sqrt

from numpy import complex

from visualize import complex_pretty

class ComplexPrettyStrig(unittest.TestCase):

    def test_zero(self):
        n = complex(0,0)
        self.assertEqual(complex_pretty(n), '0')

    def test_real_int(self):
        n = complex(4,0)
        self.assertEqual(complex_pretty(n), '4')

    def test_real_dec(self):
        n = complex(pi,0)
        self.assertEqual(complex_pretty(n), '3.14')

    def test_real_neg(self):
        n = complex(-3,0)
        self.assertEqual(complex_pretty(n), '-3')

    def test_imag_int(self):
        n = complex(0,4)
        self.assertEqual(complex_pretty(n), '4j')

    def test_imag_dec(self):
        n = complex(0,e)
        self.assertEqual(complex_pretty(n), '2.72j')

    def test_imag_neg(self):
        n = complex(0,-6)
        self.assertEqual(complex_pretty(n), '-6j')

    def test_complex_int(self):
        n = complex(4,3)
        self.assertEqual(complex_pretty(n), '4 + 3j')

    def test_complex_dec(self):
        n = complex(1/sqrt(2), 1/sqrt(2))
        self.assertEqual(complex_pretty(n), '0.71 + 0.71j')

    def test_complex_neg(self):
        n = complex(-0.5, -sqrt(3)/2)
        self.assertEqual(complex_pretty(n), '-0.50 - 0.87j')

    def test_real_near_zero(self):
        n = complex(0.0000000001, 0)
        self.assertEqual(complex_pretty(n), '0')

    def test_imag_near_zero(self):
        n = complex(0, -0.00001)
        self.assertEqual(complex_pretty(n), '0')

    def test_complex_near_zero(self):
        n = complex(-0.000001, 0.0000001)
        self.assertEqual(complex_pretty(n), '0')



if __name__ == '__main__':
    unittest.main()
