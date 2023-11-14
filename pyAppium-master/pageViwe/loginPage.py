# _*_coding:utf-8 _*_
# @File　　  :loginPage.py
# @Software  :PyCharm
import time

import allure
from selenium.webdriver.common.by import By

from pageViwe.basePage import BasePage


class LoginPage(BasePage):

    # version_ask = (By.ID, "android:id/button1")
    gd_btn = (By.ID, "com.xkw.client:id/dialog_close")
    agree_btn = (By.ID, "com.xkw.client:id/agree_yes")
    mine_btn = (By.ID, "com.xkw.client:id/mine_text")
    login_btn = (By.ID, "com.xkw.client:id/mine_username")
    password_login_btn = (By.ID, "com.xkw.client:id/login_mobile_use_password")
    username_input = (By.ID, "com.xkw.client:id/login_password_username")
    password_input = (By.ID, "com.xkw.client:id/login_password_password")
    login_submit_btn = (By.ID, "com.xkw.client:id/login_password_login")

    discover_search_box = (By.ID, "com.xkw.client:id/discover_search_box")

    # def open(self):
    #     self.click_element(*self.version_ask, doc='系统已有更高版本，无法安装，直接打开')

    def gd_close(self):
        self.click_element(*self.gd_btn, doc='关闭广告')

    def agree(self):
        self.click_element(*self.agree_btn, doc='同意协议')

    def login(self, user, password):
        # with allure.step("同意协议"):
        #     self.agree()

        with allure.step("我的页面，点击切换到我的页面"):
            self.click_element(*self.mine_btn, doc='我的按钮')
        with allure.step("我的页面，点击登录"):
            self.click_element(*self.login_btn, doc='我的_登录')
        with allure.step("我的_登录页面_切换到用户密码登录"):
            self.click_element(*self.password_login_btn, doc='我的_登录_密码登录')
        with allure.step('我的_账号密码登录页面，输入账号:{}'.format(user)):
            self.send_keys(*self.username_input, value=user, doc='登录_用户名输入框')
        with allure.step('我的_账号密码登录页面，输入密码:{}'.format(password)):
            self.send_keys(*self.password_input, value=password, doc='登录_密码输入框')
        with allure.step('我的_账号密码登录页面_点击提交登录'):
            self.click_element(*self.login_submit_btn, doc='我的_登录_提交登录')

    def home_swipe(self):
        with allure.step("同意协议"):
            self.agree()

        time.sleep(2)
        with allure.step("等待发现页面"):
            self.is_element_exist(*self.discover_search_box, doc="发现")

        with allure.step("上滑操作"):
            self.swipe_to_up("首页")

    def get_username(self):
        with allure.step("获取用户名"):
            return self.get_text(*self.login_btn, doc="我的_用户名")
