# HTMLTestReportCN-ScreenShot

带有截图功能的 `HTMLTestReportCN`, 基于 [findyou](https://github.com/findyou) 和 [boafantasy](https://github.com/boafantasy) 两位的版本修改的, 添加功能并修复bug和优化细节

- 目前同时拥有无截图和有截图报告功能, 通过参数 `need_screenshot` 开启截图功能
- 生成的报告有饼图显示, 测试结果比较直观
- [findyou](https://github.com/findyou) 版本: https://github.com/findyou/HTMLTestRunnerCN
- [boafantasy](https://github.com/boafantasy) 版本: https://github.com/boafantasy/HTMLTestRunnerCN

## 步骤

### 1. 初始化（若无需截图, 则跳过此步骤）

unittest框架, `setup()` 初始化 `ReportDirectory()`

```python
def setUp(self):
    ...
    self.report_dir = ReportDirectory()
```

### 2. 执行截图和获取截图名字（若无需截图, 则跳过此步骤）

测试用例的断言操作, 在抛出的 `Exception` 里执行截图操作, 截图名字通过 `print()` 出来跟随异常一起抛出

> 注意: 截图方法用的是 `selenium` 的, 如需用其他方法截图, 请自行到 `HTMLTestReportCN.py` 修改 `get_screenshot()` 方法

调用该方法则自动把截图附加到报告里

```python
def test1_find_input(self):
    try:
        self.browser.find_element(by=By.ID, value="kw")
    except Exception:
        self.report_dir.get_screenshot(self.browser)
        raise
```
### 3. 启动时创建文件夹

启动代码里, 调用 `create_dir()`, 会根据时间创建文件夹, 把截图和报告存入对应的文件夹

```python
if __name__ == "__main__":
    ReportDirectory().create_dir()
    unittest.main()
```

### 4. 自定义报告路径

初始化 `ReportDirectory()` 时可以传入 `path="自定义路径"` 来自定义报告生成目录

```python
def setUp(self):
    ...
    self.report_dir = ReportDirectory(path="./report/")
```

> 注意: 目录结构是相对路径, 而不是用绝对路径

### 5. 截图基本功能

目前为止, 在测试用例文件启动后, 出现异常可以实现截图功能

### 6. 生成HTML测试报告文档

新建 `RunAllTests.py`, 如何封装可以自行决定

```python
class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "./testcases"
        self.title = "自动化测试报告"
        self.description = "测试报告"
        self.report_path = "../report/"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取报告的名字
        report_dir = HTMLTestReportCN.ReportDirectory(path=self.report_path)
        report_dir.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=input("请输入你的名字: "))
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()

```

-----

## 效果预览

![效果预览](assets/report.gif)
