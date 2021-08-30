from calculator import Count
import unittest

class Testadd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add1(self):
        add = Count(6,5)
        self.assertEqual(add.add(),11)

    def test_add2(self):
        add = Count(7,2)
        self.assertEqual(add.add(),9)

    def tearDown(self):
        print("test end")


class Testsub(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_sub1(self):
        sub = Count(7,2)
        self.assertEqual(sub.sub(),5)

    def test_sub2(self):
        sub = Count(11,2)
        self.assertEqual(sub.sub(),10)

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Testadd('test_add1'))
    suite.addTest(Testadd('test_add2'))
    suite.addTest(Testsub('test_sub1'))
    suite.addTest(Testsub('test_sub2'))

    runner = unittest.TextTestRunner()
    runner.run(suite)