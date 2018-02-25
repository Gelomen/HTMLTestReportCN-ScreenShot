# coding=utf-8

""""" 运行 “.” (当前)目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
import datetime
from src.lib import HTMLTestReportCN


class RunAllTests(object):

    def __init__(self, path="."):
        self.test_case_path = path
        self.title = "Test Report"
        self.description = "测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取最新文件夹的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir()
        new_dir = daf.get_new_dir()

        # 在最新文件夹下新建测试报告
        now = str(datetime.datetime.now().strftime("%Y-%m-%d(%H-%M-%S)"))
        file_path = new_dir + "/Test_report_" + now + ".html"

        fp = open(file_path, "wb")

        # need_screen_shot = 0，表示不是UI自动化测试，不执行截图
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, need_screen_shot=0, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()

        print("\033[36;0m--------------------- 测试结束 ---------------------\033[0m")


if __name__ == "__main__":
    RunAllTests().run()
