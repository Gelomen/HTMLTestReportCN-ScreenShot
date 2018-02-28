# HTMLTestReportCN_ScreenShot

> #### 带有截图功能的HTMLTestReportCN
> * 在大神findyou和boafantasy两人的版本基础上，添加截图功能，并修复bug和优化细节；
> * 此版本目前同时拥有无截图和有截图报告功能，通过参数 `need_screen_shot=1` 开启截图功能；
> * [findyou](https://github.com/findyou) 大神原版：https://github.com/findyou/HTMLTestRunnerCN ；
> * [boafantasy](https://github.com/boafantasy) 大神原版：https://github.com/boafantasy/HTMLTestRunnerCN ；


## 步骤
### 一、报告文档需截图
#### 1. 初始化
unittest框架，`setup()` 初始化 `DirAndFiles()`
```python
def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.get("https://www.baidu.com")
    self.daf = DirAndFiles()
```
#### 2. 执行截图和获取截图名字
测试用例的断言操作，在抛出的Exception里执行截图操作，截图名字通过 `print()` 出来跟随异常一起抛出，**注意：截图方法用的是selenium的，如需用其他方法截图，请自行到 `HTMLTestReportCN.py` 修改 `get_screenshot()` 方法**
```python
def test1_find_input(self):
    try:
        self.browser.find_element_by_xpath("//input[@id='kw']")
    except Exception:
        self.daf.get_screenshot(self.browser)
        raise
```
#### 3. 启动时创建文件夹
启动代码里，调用 `create_dir()`，会根据时间创建文件夹，把截图和报告存入对应的文件夹
```python
if __name__ == "__main__":
    DirAndFiles().create_dir()
    unittest.main()
```
#### 4. 报告路径
到 **HTMLTestReportCN.py**，找到 `class DirAndFiles(object)`，修改初始化的 `self.path = "../../result/"` 报告路径为你自己的，**注意：目录结构需要先创建好！且最好是以测试用例为相对路径，而不是用绝对路径**

#### 5. 截图基本功能
目前为止，在测试用例文件启动后，出现异常可以实现截图功能

#### 6. 生成HTML测试报告文档
新建 `RunAllTests.py`，如何封装可以自行决定，**主要需要注意的是：`HTMLTestReportCN.HTMLTestRunner()` 需加入参数 `need_screenshot=1` 以启用将error截图嵌入HTML功能，同时 `RunAllTests.py` 存放的路径需要跟普通用例文件具有相同目录结构，以保证正常读取```第4点```的报告路径**
```python
class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "."
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

        # need_screenshot = 1，表示是UI自动化测试，需执行截图
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, need_screenshot=1, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()
```

-----
### 二、报告文档不用截图
#### 1. 初始化
无需初始化

#### 2. 抛出异常
直接抛出即可
```python
def test1(self):
    try:
        self.assertNotEqual(self.a, self.b, "a == b!")
    except AssertionError:
        raise
```
#### 3. 报告路径
参考 一、4

#### 4. 生成HTML测试报告文档
与 一、6相同，但 **注意：`HTMLTestReportCN.HTMLTestRunner()` 的参数 `need_screenshot=1` 需改为 `need_screenshot=0` 以关闭嵌入截图功能，其他一致**
