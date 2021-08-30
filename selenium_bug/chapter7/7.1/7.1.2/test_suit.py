from calculator import Count
import unittest

class test_suit(unittest.TestCase):

    def setUp(slef):
        print("Test start")

    def test_add(self):
        add = Count(6,3)
        self.assertEqual(add.add(),9)

    def test_sub(self):
        sub = Count(4,2)
        self.assertEqual(sub.sub(),2)

    def tearDown(self):
        print("Test start")


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(test_suit("test_add"))
    suit.addTest(test_suit("test_sub"))

    runner = unittest.TextTestRunner()
    runner.run(suit)