# coding=utf-8

""""" 运行 `./testcases` 目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
from lib import HTMLTestReportCN

report_dir = "./report"
title = "自动化测试报告"
description = "测试报告"
test_case_path = "./testcases"


@HTMLTestReportCN.init(report_dir=report_dir, title=title)
def run():
    test_suite = unittest.TestLoader().discover(test_case_path)

    fp = open(HTMLTestReportCN.get_report_path(), "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp, title=title, description=description, tester=input("请输入你的名字: ")
    )
    runner.run(test_suite)
    fp.close()


if __name__ == "__main__":
    run()
