# _*_coding:utf-8 _*_
# @File　　  :basePage.py
# @Software  :PyCharm


import datetime
import logging
import time

from selenium.webdriver.common.by import By
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.all_path import picturePath
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc, doc="") -> WebElement:
        """
        查找单个元素方法
        :type doc: 定位元素界面位置：例如 首页
        :type loc: 元素定位
        """
        try:
            logging.info("{} 页面开始查找元素{}".format(doc, loc))
            WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(loc))
            ele = self.driver.find_element(*loc)
            logging.info("{} 页面查找元素{}成功！".format(doc, loc))
            return ele
        except Exception as e:
            logging.error('{} 定位元素 {}出现未知错误！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def find_elements(self, *loc, doc=''):
        """
        查找多个元素方法
        """
        try:
            logging.info("{} 页面开始查找一组元素{}".format(doc, loc))
            WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(loc))
            ele = self.driver.find_elements(*loc)
            logging.info("{} 页面查找元素{}成功！".format(doc, loc))
            return ele
        except Exception as e:
            logging.error('{} 定位元素 {}出现未知错误！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def click_element(self, *loc, doc=''):
        ele = self.find_element(*loc, doc=doc)
        try:
            logging.info("{} 页面点击元素{}".format(doc, loc))
            ele.click()
            logging.info("{} 页面点击元素{}成功！".format(doc, loc))
        except Exception as e:
            logging.error('{} 点击元素 {}失败！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def send_keys(self, *loc, value, doc=''):
        """
        send_keys方法
        """
        ele = self.find_element(*loc, doc=doc)
        try:
            logging.info("{} 页面输入框输入{}".format(doc, value))
            ele.clear()
            ele.send_keys(value)
            logging.info("{} 页面输入框输入{}成功！".format(doc, value))
        except Exception as e:
            logging.error('{} 定位元素 {}出现未知错误！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def is_toast_exist(self, text, doc=''):
        """is toast exist, return True or False
        :Agrs:
            - text   - 页面上看到的文本内容
        :Usage:
            is_toast_exist("看到的内容")
        """
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            logging.info("{} 页面开始查找 toast {}".format(doc, toast_loc))
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(toast_loc))
            logging.info("{} 页面开始查找 toast {} 成功！".format(doc, toast_loc))
            return True
        except Exception as e:
            logging.error('{} 页面toast {} 未出现！ 错误为：{}'.format(doc, text, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            return False

    def is_element_exist(self, *loc, doc=''):
        try:
            logging.info("{} 页面开始查找元素 {}".format(doc, loc))
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            logging.info("{} 页面查找元素 {}成功！".format(doc, loc))
            return True
        except Exception as e:
            logging.exception('{} 定位元素 {}出现未知错误！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            return False

    def get_text(self, *loc, doc=''):
        ele = self.find_element(*loc, doc=doc)
        try:
            logging.info("{} 页面开始获取 {} 文本".format(doc, loc))
            text = ele.text
            logging.info("{} 页面获取文本 {}成功！".format(doc, loc))
            return text
        except Exception as e:
            logging.exception('{} 定位元素 {}出现未知错误！ 错误为：{}'.format(doc, loc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            return None

    def get_size(self):
        """
        获取屏幕大小
        """
        try:
            logging.info("开始获取设备屏幕大小。")
            size = self.driver.get_window_size()
            width = size.get("width")
            height = size.get("height")
            logging.info("获取设备屏幕大小完成。{}".format((width, height)))
            return width, height
        except Exception as e:
            logging.error('获取屏幕尺寸失败 ！ 错误为：{}'.format(e))
            return None

    def swipe_to_left(self, doc=''):
        """
        左滑
        """
        width, height = self.get_size()
        try:
            logging.info("{} 页面开始进行左滑".format(doc))
            self.driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, duration=1000)
            logging.info("{} 页面开始左滑完成。".format(doc))
            time.sleep(0.5)
        except Exception as e:
            logging.error('左滑屏幕失败 ！ 错误为：{}'.format(e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_right(self, doc=''):
        """
        右滑
        """
        width, height = self.get_size()
        try:
            logging.info("{} 页面开始进行右滑".format(doc))
            self.driver.swipe(width * 0.1, height * 0.5, width * 0.9, height * 0.5, duration=1000)
            logging.info("{} 页面开始右滑完成。".format(doc))
            time.sleep(0.5)
        except Exception as e:
            logging.error('右滑屏幕失败 ！ 错误为：{}'.format(e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_up(self, doc=''):
        """
        上滑
        """
        width, height = self.get_size()
        try:
            logging.info("{} 页面开始进行上滑".format(doc))
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, duration=1000)
            logging.info("{} 页面开始上滑完成。".format(doc))
            time.sleep(0.5)
        except Exception as e:
            logging.error('上滑屏幕失败 ！ 错误为：{}'.format(e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_down(self, doc=''):
        """
        下滑、下拉刷新
        """
        width, height = self.get_size()
        try:
            logging.info("{} 页面开始进行下滑".format(doc))
            self.driver.swipe(width * 0.5, height * 0.4, width * 0.5, height * 0.9, duration=1000)
            logging.info("{} 页面开始下滑完成。".format(doc))
            time.sleep(1)
        except Exception as e:
            logging.error('下滑、下拉刷新屏幕失败 ！ 错误为：{}'.format(e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def get_screenshot(self, doc):
        """
        截图
        """
        logging.info("开始进行截图..")
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        pic_name = picturePath + r"\{}".format(doc) + now + '.png'
        self.driver.get_screenshot_as_file(pic_name)
        logging.info("截图成功！图片名称为:{}".format(pic_name))
        with open(pic_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, doc, allure.attachment_type.PNG)
        return pic_name

    def result_assert(self, res, expected, doc=''):
        try:
            assert res == expected
        except AssertionError:
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            raise
