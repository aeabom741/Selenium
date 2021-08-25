import unittest
import testadd
import testsub

suit =unittest.TestSuite()
suit.addTest(testadd.testadd("test_add1"))
suit.addTest(testadd.testadd("test_add2"))
suit.addTest(testsub.testsub("test_sub1"))
suit.addTest(testsub.testsub("test_sub2"))

runner = unittest.TextTestRunner()
runner.run(suit)