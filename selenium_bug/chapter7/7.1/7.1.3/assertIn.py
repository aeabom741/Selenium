import unittest

class test(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_in(self):
        a = 'hallo'
        b = 'hallo world'
        self.assertIn(a,b,msg="It's not in b")

    def tearDown(self):
        print("Test end")

if __name__ == "__main__":
    unittest.main()