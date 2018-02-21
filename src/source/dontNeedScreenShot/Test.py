# coding=utf-8

""""" 载入场景测试用例 """""

import unittest


class TestClass(unittest.TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2

    def tearDown(self):
        pass

    def test1(self):
        try:
            self.assertNotEqual(self.a, self.b, "a == b!")
        except AssertionError:
            raise

    def test2(self):
        try:
            self.assertEqual(self.a, self.b, "a ≠ b!")
        except AssertionError:
            raise


if __name__ == "__main__":
    unittest.main()
