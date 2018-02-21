# coding=utf-8

""""" 载入场景测试用例 """""

import unittest
from selenium import webdriver
from src.lib.HTMLTestReportCN import DirAndFiles


class TestClass(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="./lib/chromedriver.exe")
        self.browser.get("https://www.baidu.com")
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    def test1_find_input(self):
        try:
            self.browser.find_element_by_xpath("//input[@id='kw']")
        except Exception:
            img_name = self.daf.get_screen_shot(self.browser)
            raise Exception(img_name)

    def test2_title(self):
        title = self.browser.title
        try:
            self.assertEqual(title, "百度一下，你就知道!", "Title不一致！")
        except AssertionError:
            img_name = self.daf.get_screen_shot(self.browser)
            raise AssertionError(img_name)


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
