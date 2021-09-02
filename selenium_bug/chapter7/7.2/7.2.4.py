import unittest

def setUpModule():
    print("test module start>>>>>>>>>")

def tearDownModule():
    print("test module end>>>>>>>>>>>")

class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("test class start ======>")
    
    @classmethod
    def tearDownClass(cls):
        print("test class end =====>")

    def setUp(self):
        print("test setup")

    def tearDown(self):
        print("test teardown")

    def test_case(self):
        print("test case")

if __name__ == "__main__":
    unittest.main()