from count import prime
import unittest

class test_prime(unittest.TestCase):
    
    def setUp(self):
        print("test start")

    def test_prime(self):
        a = prime(8)
        self.assertTrue(a.is_prime(),msg="The number is not prime")

    def tearDown(self):
        print("test end")

    
if __name__ == "__main__":
    unittest.main()
    