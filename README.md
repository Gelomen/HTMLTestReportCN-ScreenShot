# HTMLTestReportCN-ScreenShot

带有截图功能的 `HTMLTestReportCN`, 基于 [findyou](https://github.com/findyou) 和 [boafantasy](https://github.com/boafantasy) 两位的版本修改的, 添加功能并修复bug和优化细节

- 目前同时拥有无截图和有截图报告功能, 通过参数 `need_screenshot` 开启截图功能
- 生成的报告有饼图显示, 测试结果比较直观
- [findyou](https://github.com/findyou) 版本: https://github.com/findyou/HTMLTestRunnerCN
- [boafantasy](https://github.com/boafantasy) 版本: https://github.com/boafantasy/HTMLTestRunnerCN

## 步骤

查看例子: [Samples](./samples)

### 1. 初始化修饰器

新建 `RunAllTests.py`, 如何封装可以自行决定

- `run()` 添加 `@HTMLTestReportCN.init()` 修饰器, 并把报告目录和报告标题传入
- 调用 `HTMLTestReportCN.get_report_path()` 获取 `HTML` 报告路径, 用于测试结果写入

```python
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

```

### 2. 截图修饰器

在需要截图的测试用例添加 `@HTMLTestReportCN.screenshot` 修饰器, 失败时会自动截图

```python
from lib import HTMLTestReportCN

...

@HTMLTestReportCN.screenshot
def test1_find_input(self):
    ...

```

-----

## 效果预览

![效果预览](assets/report.gif)
