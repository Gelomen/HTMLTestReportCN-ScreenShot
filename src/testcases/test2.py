# coding=utf-8

""""" 数据验证测试用例 """""

import unittest


class TestClass(unittest.TestCase):
    """ 数据自动化测试 """

    def setUp(self):
        self.a = 1
        self.b = 2

    def tearDown(self):
        pass

    def test1(self):
        """ 数据验证1 """
        try:
            self.assertNotEqual(self.a, self.b, "a == b!")
        except AssertionError:
            raise

    def test2(self):
        """ 数据验证2 """
        try:
            self.assertEqual(self.a, self.b, "a ≠ b!")
        except AssertionError:
            raise


if __name__ == "__main__":
    unittest.main()
