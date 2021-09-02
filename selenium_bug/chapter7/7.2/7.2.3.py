import unittest
class Mytest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("直接跳過測試")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3>2,"當條件為true時跳過")
    def test_skipis(self):
        print("當條件為true時跳過")

    @unittest.skipUnless(3>2,"當條件為true時執行測試")
    def test_skipunless(self):
        print("當條件為true時執行測試")

    @unittest.expectedFailure
    def test_false(self):
        print("test false")

if __name__ == "__main__":
    unittest.main()