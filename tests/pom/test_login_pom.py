# -*- encoding=utf8 -*-

import pytest
import allure
from airtest.core.api import *
# from lib.tools import touch_image
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

"""
class PageBase(object):
    def __init__(self):
        pass
"""


@allure.feature("测试登录模块")
class TestHhCases(object):

    @classmethod
    def setup_class(cls):
        print("前置执行：登录模块开始执行:")

    @classmethod
    def teardown_class(cls):
        print("登录模块执行完毕")

    @classmethod
    def setup_method(cls):
        print("执行用例：")
        start_app("com.youdao.lingshi.aicard")
        sleep(0.5)

    @classmethod
    def teardown_method(cls):
        print("用例执行完毕，关闭程序，回到首页")
        stop_app("com.youdao.lingshi.aicard")
        keyevent("HOME")

    @pytest.mark.slow
    def test_ddt(self, username, password):
        print("用户名:%s,密码%s" % (username, password))

