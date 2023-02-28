# airtest-uitesting-template

[TOC]
<!-- TOC -->
* [airtest-uitesting-template](#airtest-uitesting-template)
  * [模版能力](#)
  * [1.开发环境](#1)
  * [2.模版工程计划](#2)
  * [3.项目结构](#3)
  * [5.命令行执行](#5)
  * [6.关注的 pytest 能给测试带来的便利](#6-pytest-)
  * [资料](#)
<!-- TOC -->

## 模版能力

1. 期望能力：快速构建移动端 UI 自动化用例，同时能够兼容小程序，能够组织用例执行和完整的测试报告
2. airtest 框架底层为 python 语言实现，使用 airTest + pytest + allure 来设计。
   - airtest：对公众号、小程序的元素控件进行抓取，可使用 Poco 定位或 Airtest 图像识别进行
   - pytest：对整体用例集、用例进行管理；可单条，批量执行，分类执行等等
   - allure：输出报告，显示各用例执行结果，执行时间等
3. 可以使用 tidevice 来连接 ios 手机

## 1.开发环境

1. 安装 JDK8 并配置环境变量
2. conda 创建 Python3 环境，并安装依赖包 `pip install -r requestments.txt`
3. 安装 [allure](https://github.com/allure-framework/allure2/releases) [查看](https://docs.qameta.io/allure-report/#_installing_a_commandline)
    ```text
    1. Linux
    For debian-based repositories a PPA is provided:
    
    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update 
    sudo apt-get install allure
    
    2 Mac OS X
    For Mas OS, automated installation is available via Homebrew
    
    brew install allure
    
    2 Windows
    For Windows, Allure is available from the Scoop commandline-installer.
    To install Allure, download and install Scoop and then execute in the Powershell:
    
    scoop install allure
    ```
4. [安装Android_SDK(adb套件)并配置环境变量: platform-tools 目录](https://www.cnblogs.com/gufengchen/p/11038029.html)

## 2.模版工程计划

1. 针对主体功能使用Airtest脚本进行实验，测量稳定性,可行性。
2. 确定可行后，转为纯Python脚本进行测试。
3. 在Airtest框架基础上，搭配Pytest框架，Allure进行用例集，单用例的管理，测试报告的输出。
4. 切实可行后，可考虑将每一个公众号，小程序主体功能自动化，评估运用DDT，PO思想重构项目，以及Jenkins持续集成，Docker持续交付。

## 3.项目结构

```text
├── __init__.py
├── config.py                       # 配置属性类变量
├── docs
│   └── assets                     # 此文件内的图片
├── lib                                 # 工具集
│   ├── __init__.py
│   ├── launch.py               #用于初始化连接手机和启动APP
│   └── tools.py
├── pytest.ini                      #pytest的配置文件，主要用于过滤不想执行的目录
├── readme.md
├── requestments.txt
├── run.py                          #启动整体项目并输出报告
├── result-report                   #存放最新生成的HTML报告
├── result/data                     #存放报告数据，格式为：年\_月\_日\_时\_分\_秒
├── selectors
│   └── login-selector          # 存放图片文件
│       ├── tpl1670395937592.png
└── tests                           #重要py文件-用例集及模块用例
    ├── __init__.py
    └── pom
        ├── __init__.py
        ├── __pycache__
        └── test_login_pom.py
```

## 4.命令行执行

- python -m run.py
- 相关命令介绍
  ```shell
  # 执行指定的用例
  python -m pytest -v tests/login/test_login.py::TestLogin --alluredir ./reports/1
  # 将 ./report/1 路径下的json格式报告输出到 ./reports 路径下生成html格式报告，并清空 reports 文件夹下原来的报告
  allure generate ./report/1 -o ./reports --clean
  # 启动allure服务，打开allure报告
  allure open -h 127.0.0.1 -p 8089 ./reports
  
  os.system('allure serve %s' % report_path)
  os.system('allure open ./result-report')
  ```

## 6.关注的 pytest 能给测试带来的便利

- 用例的管理
  - 用例集 TestClass、 test_module
  - 用例组织
- 优秀的断言
  - builtin
  - 支持用户自定义
- 完整的报告
  - pytest 日志
  - 依赖 allure-pytest 美化报告
  - 自定义 hook-plugin 进行数据上报
- 用例按要求执行
  - python -m pytest -qq --tb=short
  - mock 使用不方便的数据接口
  - 失败重试
  - 按设定顺序执行 pytest-ordering
  - 按设定依赖关系执行 pytest-depends
  - 按指定的分类执行用例 pytest.mark.P0
- 定制参数（项目、运行时）
  - pytest.ini 启动进行实例化的相关配置
  - pytest 全局参数
  - pytest.fixture 定义全局的方法；实现 setup/teardown
  - pytest.mark.parametrize  运行时参数
  - hook/plugin  开发自己的工具

## 资料

- https://buildmedia.readthedocs.org%2Fmedia%2Fpdf%2Fpytest%2Flatest%2Fpytest.pdf
- <https://hackmd.io/@jenc/SJYmGcKsK>
- <https://python012.github.io/2018/05/08/pytest%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6%E4%B8%AD%E7%9A%84setup%E5%92%8CtearDown/>