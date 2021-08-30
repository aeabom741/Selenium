import unittest

class tset(unittest.TestCase):

    def setUp(self):
        number = input("enter a number:")
        self.number = int(number)

    def test_equal(self):
        self.assertEqual(self.number,10,msg="The number is not equal 10")

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()