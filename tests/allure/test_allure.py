# -*- coding: utf-8 -*-

"""
@author: jay.zhen
@contact: jayzhen_testing@163.com
@version: 1.0.0
@license: Apache Licence
@file: test_allure.py
@time: 2023/2/27 14:50


@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
"""

import pytest
import allure


# allure.feature 定义功能
@allure.feature("报告购物车")
class TestAllure(object):
    # 定义用户场景
    @allure.story("加入购物车")
    def test_add_goods_cart(self):
        # 调用步骤函数
        login("crisimple", "123456")

        # 将测试用例分成几个步骤，将测试步骤打印到测试报告中，步骤二
        with allure.step("浏览商品"):
            # allure.attach--打印一些附加信息
            allure.attach("商品1", "C")
            allure.attach("商品2", "C")

        # 步骤三
        with allure.step("加入商品"):
            allure.attach("商品1", 2)
            allure.attach("商品2", 3)

        # 步骤四
        with allure.step("校验商品"):
            allure.attach("商品1加入成功", "共2个")
            allure.attach("商品2加入失败", "共0个")

    @allure.story("继续购物")
    def test_continue_shopping_cart(self):
        login("crisimple", "123456")
        allure.attach("商品3", 4)
        print("继续购物成功")

    @allure.story("减少商品失败")
    def test_edit_shopping_cart(self):
        login("crisimple", "123")
        assert 0

    @pytest.mark.skip(reason="删除购物车不执行")
    @allure.story("删除购物车")
    def test_delete_shopping_cart(self):
        login("crisimple", "123")
        print()


# 将函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名称通常时函数名，这样的函数通常称为步骤函数
@allure.step("用户登录")
def login(user, passwd):
    if user == "crisimple" and passwd == "123456":
        print(user, passwd)
        print("登录成功")
    else:
        print(user, passwd)
        print("登录失败，请重新尝试")
