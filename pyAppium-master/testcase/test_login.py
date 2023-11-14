# _*_coding:utf-8 _*_
# @Time　　:2021/6/18 21:22
# @Author　 : king
# @File　　  :test_login.py
# @Software  :PyCharm
# import random

import allure


@allure.feature("登录")
class TestLogin:

    @allure.story("首页上滑")
    @allure.description("首页上滑")  # 用例的描述
    @allure.severity(allure.severity_level.BLOCKER)
    def test_swipe(self, common_driver, device):
        allure.dynamic.title("首页上滑" + device["device"])
        common_driver.home_swipe()

    @allure.story("正常登录")
    @allure.description("用户正常登录")  # 用例的描述
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, common_driver, device):
        allure.dynamic.title("登录" + device["device"])
        common_driver.login('XXX', 'XXX')
        common_driver.result_assert(common_driver.get_username(), "xkw_03314932", '用户正常登录')
