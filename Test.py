# coding=utf-8

""""" 载入场景测试用例 """""

import unittest
from time import sleep
from selenium import webdriver
from src.source.common.Common import Common
from src.lib.HTMLTestReportCN import DirAndFiles


class TestLoadingView(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="../../lib/chromedriver.exe")
        self.common = Common(self.browser)
        self.common.start()
        self.daf = DirAndFiles()

    def tearDown(self):
        self.browser.quit()

    # 验证是否进入载入场景
    def test1_loading_view_showing(self):
        sleep(1)
        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "没有进入载入场景！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

    # 验证载入场景进度条
    def test2_loading_bar(self):
        sleep(1)
        tip = self.common.loading_bar()
        try:
            self.assertEqual(tip, "100%", "进度条走满后，百分比不是100%！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

    # 验证载入场景进度条100%后是否消失
    def test3_loading_view_dispear(self):
        sleep(1)
        self.common.loading_bar()
        sleep(1)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

    # 验证竖屏进入载入画面，是否显示载入场景、进度条以及进度条走满后是否消失
    def test4_loading_on_vertical_screen(self):
        # 切换竖屏
        self.common.set_window_to_vertical_screen()

        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "竖屏没有进入载入场景！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

        tip = self.common.loading_bar()
        try:
            self.assertEqual(tip, "100%", "竖屏进度条走满后，百分比不是100%！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

        sleep(1)
        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "竖屏载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

    # 验证载入场景来回切换横竖屏显示正常
    def test5_loading_switch_screen(self):
        # 切换竖屏
        self.common.set_window_to_vertical_screen()

        sleep(1)

        # 切换横屏
        self.common.set_window_to_horizontal_screen()

        showing = self.common.loading_view_showing()
        try:
            self.assertEqual(showing, True, "来回切换横竖屏没有进入载入场景！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

        # 切换竖屏
        self.common.set_window_to_vertical_screen()

        tip = self.common.loading_bar()
        try:
            self.assertEqual(tip, "100%", "竖屏进度条走满后，百分比不是100%！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)

        # 切换横屏
        self.common.set_window_to_horizontal_screen()

        sleep(2)

        showing = self.common.loading_view_dispear()
        try:
            self.assertEqual(showing, None, "来回切换横竖屏，载入完成后载入场景不会消失！")
        except AssertionError:
            self.daf.get_screen_shot(self.browser)
            file_name = self.daf.get_new_file()
            raise AssertionError(file_name)


if __name__ == "__main__":
    # 启动测试时创建文件夹
    DirAndFiles().create_dir()
    unittest.main()
