# -*- encoding=utf8 -*-

import time

import allure
from airtest.core.api import touch, sleep, exists, text, log
from airtest.core.assertions import assert_exists
from airtest.core.cv import Template

from lib.launch import init_config

case_images_path = 'D:/Workspace/airtest-uitesting-template/selectors/login-selector/'


class TemplateDemo(Template):

    def __init__(self, filename, **kwargs):
        self.filename = case_images_path + filename
        super(TemplateDemo, self).__init__(self.filename)


Template = TemplateDemo


@allure.feature("测试模块：登录模块")
class TestLogin(object):

    @allure.story('用户故事：登录')
    @allure.step('测试步骤')
    def test_lingshi_login(self):
        init_config()
        sleep(1.0)
        # 登录有道领世APP
        touch(Template("tpl1670395937592.png"))
        touch(Template(r"tpl1670396180931.png", record_pos=(-0.237, -0.825), resolution=(1170, 2532)))
        sleep(1.0)

        touch(Template(r"tpl1670398367631.png", record_pos=(0.355, -0.144), resolution=(1170, 2532)))
        sleep(1.0)

        # 同意协议的icon容易被键盘挡住，所以先把他给点了
        touch(Template(r"tpl1670398795122.png", record_pos=(-0.418, 0.149), resolution=(1170, 2532)))

        # 这里需要注意，需要激活光标的输入框截图才能定位到
        if exists(Template(r"tpl1670398249886.png", record_pos=(-0.274, -0.437), resolution=(1170, 2532))):
            touch(Template(r"tpl1673508234063.png", record_pos=(-0.276, -0.44), resolution=(1170, 2532)))
            text("12345678900")
            sleep(1)
            touch(Template(r"tpl1670398529482.png", record_pos=(-0.288, -0.283), resolution=(1170, 2532)))
            text("123456")
        else:
            touch(Template(r"tpl1670398529482.png", record_pos=(-0.288, -0.283), resolution=(1170, 2532)))
            text("123456")

        touch(Template(r"tpl1670398714193.png", record_pos=(-0.01, 0.015), resolution=(1170, 2532)))

        sleep(5)
        assert_exists(Template(r"tpl1670399834697.png", record_pos=(-0.347, -0.55), resolution=(1170, 2532)),
                      "判断登录成功了")
        log("登录成功", timestamp=time.time(), desc="登录成功了")
