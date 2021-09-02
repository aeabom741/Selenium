import unittest

class testbdd(unittest.TestCase):
    def setUp(self):
        print("TestBDD")
    
    def test_ccc(self):
        print("test ccc")
    
    def test_aaa(self):
        print("test aaa")
    
    def tearDown(self):
        pass

class testadd(unittest.TestCase):
    def setUp(self):
        print("TestADD")
    
    def test_bbb(self):
        print("test bbb")

    def tearDown(self):
        pass

if __name__ == "__main__":

    suit = unittest.TestSuite()
    suit.addTest(testbdd("test_ccc"))
    suit.addTest(testbdd("test_aaa"))
    suit.addTest(testadd("test_bbb"))

    runner = unittest.TextTestRunner()
    runner.run(suit)
        