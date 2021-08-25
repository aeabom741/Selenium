import unittest
from caculate import Count

class Testcouny(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_count(self):
        a = Count(1,5)
        self.assertEqual(a.add(),6)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()    