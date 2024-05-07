import unittest
import time

from Dz63 import factorial


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
        self.start = time.time()

    def test1_factorial(self):
        self.assertEqual(factorial(3), 6)

    def test2_factorial(self):
        self.assertRaises(ValueError, factorial, -1)

    def test3_factorial(self):
        self.assertRaises(ValueError, factorial, 100)

    def test4_factorial(self):
        self.assertEqual(factorial(1), 1)

    def test5_factorial(self):
        self.assertEqual(factorial(0), 1)

    def test6_factorial(self):
        self.assertEqual(factorial(15), 1307674368000)

    def tearDown(self) -> None:
        t = time.time() - self.start
        i = 1
        print(__name__, "-", t)
        print("tearDown")
