# -*- encoding=utf8 -*-

import pytest
import allure

data = [
    ("12345678900", "123456")
]


@allure.feature("测试登录模块")
class TestLogin(object):

    @pytest.mark.parametrize("username,password", data)
    def test_ddt(self, username, password):
        print("用户名:%s,密码%s" % (username, password))
