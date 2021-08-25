from count import calculator
import unittest

class testadd(unittest.TestCase):
    def setUP(self):
        print("start test")

    def test_add1(self):
        add = calculator(6,9)
        self.assertEqual(add.add(),17)

    def test_add2(self):
        add = calculator(9,2)
        self.assertEqual(add.add(),11)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()