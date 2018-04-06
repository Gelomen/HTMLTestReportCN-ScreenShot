# coding=utf-8

""""" 百度首页测试用例 """""

import unittest
from selenium import webdriver
from src.lib.HTMLTestReportCN import DirAndFiles


class TestClass(unittest.TestCase):
    """ UI自动化测试 """

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.browser.get("https://www.baidu.com")
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    def test1_find_input(self):
        """ UI自动化测试1 """
        try:
            # 正确值为 //input[@id='kw']
            self.browser.find_element_by_xpath("//input[@id='kw1']")
        except Exception:
            self.daf.get_screenshot(self.browser)
            raise

    def test2_assert_equal(self):
        """ UI自动化测试2 """
        a = 1
        b = 2
        try:
            self.assertEqual(a, b, "a ≠ b!")
        except AssertionError:
            raise

    def test3_title(self):
        """ UI自动化测试3 """
        title = self.browser.title
        try:
            # 加了个感叹号 ！
            self.assertEqual(title, "百度一下，你就知道!", "Title不一致！")
        except AssertionError:
            self.daf.get_screenshot(self.browser)
            raise


if __name__ == "__main__":
    DirAndFiles().create_dir()
    unittest.main()
