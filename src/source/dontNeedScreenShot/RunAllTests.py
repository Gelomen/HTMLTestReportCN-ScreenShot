# coding=utf-8

""""" 运行 “.” (当前)目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
from src.lib import HTMLTestReportCN


class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "."
        self.title = "Test Report by Gelomen"
        self.description = "测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取对应的文件夹名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalVar.get_value("report_path")

        fp = open(report_path, "wb")

        # need_screenshot = 0，表示是非UI自动化测试，无需执行截图
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, need_screenshot=0, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()
