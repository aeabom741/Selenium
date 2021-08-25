import unittest
from caculate import Count

class Testcouny(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_count(self):
        a = Count(1,5)
        self.assertEqual(a.add(),6)

    def test_multiple(self):
        a = Count(2,6)
        self.assertEqual(a.multiple(),12)

    def test_division(self):
        a = Count(6,3)
        self.assertEqual(a.division(),2)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()    
    