from typing import Callable
from calculator import Count
import unittest

class test(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        add = Count(5,6)
        self.assertEqual(add.add(),11)

    def test_sub(self):
        sub = Count(7,5)
        self.assertEqual(sub.sub(),2)

    def test_mul(self):
        mul = Count(8,5)
        self.assertEqual(mul.mul(),40)

    def test_div(self):
        div = Count(6,4)
        self.assertEqual(div.div(),1.5)

    def tearDown(self):
        print("test end")
        
if __name__ == "__main__":
    unittest.main()