# coding=utf-8

""""" 百度首页测试用例 """""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib import HTMLTestReportCN


class TestClass(unittest.TestCase):
    """ UI自动化测试 """

    def setUp(self):
        self.browser = webdriver.Edge()
        self.browser.get("https://www.baidu.com")

    def tearDown(self):
        self.browser.quit()

    @HTMLTestReportCN.screenshot
    def test1_find_input(self):
        """ UI自动化测试1 """
        try:
            # 正确值为 "kw"
            self.browser.find_element(by=By.ID, value="#kw")
        except Exception:
            raise

    def test2_assert_equal(self):
        """ UI自动化测试2 """
        a = 1
        b = 2
        try:
            self.assertEqual(a, b, "a ≠ b!")
        except AssertionError:
            raise

    @HTMLTestReportCN.screenshot
    def test3_title(self):
        """ UI自动化测试3 """
        title = self.browser.title
        try:
            # 加了个感叹号 ！
            self.assertEqual(title, "百度一下，你就知道!", "Title不一致！")
        except AssertionError:
            raise


if __name__ == "__main__":
    unittest.main()
