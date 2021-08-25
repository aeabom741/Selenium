from count import calculator
import unittest

class testsub(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_sub1(self):
        sub = calculator(7,2)
        self.assertEqual(sub.sub(),5)

    def test_sub2(self):
        sub = calculator(9,1)
        self.assertEqual(sub.sub(),8)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()