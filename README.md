# HTMLTestReportCN-ScreenShot

> #### 带有截图功能的HTMLTestReportCN
> * 在大神 [findyou](https://github.com/findyou) 和 [boafantasy](https://github.com/boafantasy) 两人的版本基础上，添加功能，并修复bug和优化细节
> * 目前同时拥有无截图和有截图报告功能，通过参数 `need_screenshot` 开启截图功能
> * 生成的报告有饼图显示，测试结果比较直观
> * [findyou](https://github.com/findyou) 大神版本：https://github.com/findyou/HTMLTestRunnerCN
> * [boafantasy](https://github.com/boafantasy) 大神版本：https://github.com/boafantasy/HTMLTestRunnerCN

## 版本
Version 1.1.0 -- Gelomen
* 优化报告截图写入方式

Version 1.0.2 -- Gelomen
* 新增测试结果统计饼图
* 优化筛选时只显示预览

Version 1.0.1 -- Gelomen
* 修复报告存入文件夹的bug
* 优化报告的命名方式

Version 1.0.0 -- Gelomen
* 修改测试报告文件夹路径的获取方式
* 修改截图获取文件夹路径的获取方式

Version 0.9.9 -- Gelomen
* 优化报告文件夹命名
* 优化截图存放的目录
* 增加图片阴影边框以突出图片
* 优化 失败用例合集 和 错误用例合集 显示的颜色

Version 0.9.8 -- Gelomen
* 优化回到顶部按钮的显示方式

Version 0.9.7 -- Gelomen
* 优化截图显示，滚动页面会固定居中

Version 0.9.6 -- Gelomen
* 新增打开图片的特效，可以直接在当前页面看截图

Version 0.9.5 -- Gelomen
* heading新增 失败 和 错误 测试用例合集

Version 0.9.4 -- Gelomen
* 修复失败和错误用例里对应按钮的颜色

Version 0.9.3 -- Gelomen
* 修复点击失败或错误按钮后，浏览器版本和截图的列不会隐藏的bug

Version 0.9.2 -- Gelomen
* 美化 浏览器版本 和 截图 的显示

Version 0.9.1 -- Gelomen
* 使用UI自动化测试时，增加 错误、失败 详细信息的 浏览器类型和版本

Version 0.9.0 -- Gelomen
* 可通过 `need_screenshot=1` 作为开关，将报告开启截图功能
* 增加 失败 和 错误 详细信息的 截图链接

Version 0.8.4 -- Gelomen
* 删除 失败模块 的显示

Version 0.8.3 -- Gelomen
* 修复 测试结果 的筛选
* 优化 失败、错误 小图标的颜色
* 增加表格 最后一列 的显示，以美化表格

Version 0.8.2.1 -Findyou
* 改为支持python3

Version 0.8.2.1 -Findyou
* 支持中文，汉化
* 调整样式，美化（需要连入网络，使用的百度的Bootstrap.js）
* 增加 通过分类显示、测试人员、通过率的展示
* 优化“详细”与“收起”状态的变换
* 增加返回顶部的锚点

Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).

Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.

Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat \<script\> block as CDATA.

Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).

## 步骤
#### 1. 初始化（若无需截图，则跳过此步骤）
unittest框架，`setup()` 初始化 `DirAndFiles()`
```python
def setUp(self):
    ...
    self.daf = DirAndFiles()
```
#### 2. 执行截图和获取截图名字（若无需截图，则跳过此步骤）
测试用例的断言操作，在抛出的Exception里执行截图操作，截图名字通过 `print()` 出来跟随异常一起抛出，**注意：截图方法用的是selenium的，如需用其他方法截图，请自行到 `HTMLTestReportCN.py` 修改 `get_screenshot()` 方法**，调用该方法则自动把截图附加到报告里。
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
新建 `RunAllTests.py`，如何封装可以自行决定，**主要需要注意的是：`RunAllTests.py` 存放的路径需要跟普通用例文件具有相同目录结构，以保证正常读取```第4点```的报告路径**
```python
class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "."
        self.title = "自动化测试报告"
        self.description = "测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取报告的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()

```

-----

## 效果预览
<img width="900" src="https://github.com/Gelomen/HTMLTestReportCN-ScreenShot/raw/master/src/assets/report.gif"/>
