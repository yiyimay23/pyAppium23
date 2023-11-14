# _*_coding:utf-8 _*_
# @File　　  :base_driver.py
# @Software  :PyCharm
import logging

from appium import webdriver
from common.all_path import configPath
import yaml
# import os


from common.app_info import get_devices_version, get_app_launchable_activity, get_app_package_name
# from common.app_info import app_path

from common.appium_auto_server import open_appium


class BaseDriver:

    def __init__(self, device_info):
        self.device_info = device_info
        cmd = "start /b appium -a 127.0.0.1 -p {0} -bp {1}".format(self.device_info["server_port"],
                                                                   self.device_info["server_port"] + 1)
        open_appium(cmd, self.device_info["server_port"])

    def base_driver(self, automationName="appium"):  # automationName="appium"
        fp = open(f"{configPath}//caps.yml", encoding='utf-8')
        # 平台名称、超时时间、是否重置、server_ip、
        desired_caps = yaml.load(fp, Loader=yaml.FullLoader)

        # 设备名称
        desired_caps["deviceName"] = self.device_info['device']

        # 版本信息
        desired_caps["platform_version"] = get_devices_version(desired_caps["deviceName"])

        # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        # desired_caps['app'] = PATH(app_path)

        desired_caps['appPackage'] = get_app_package_name()
        desired_caps['appActivity'] = get_app_launchable_activity()

        # desired_caps['appPackage'] = 'com.xkw.client'

        # desired_caps['appActivity'] = 'com.zxxk.page.main.MainActivity'
        # desired_caps['appActivity'] = 'com.zxxk.page.main.LauncherActivity'

        # udid
        desired_caps["udid"] = self.device_info['device']
        # 系统端口号
        desired_caps["systemPort"] = self.device_info["system_port"]

        if automationName != "appium":
            desired_caps["automationName"] = automationName

        logging.info(desired_caps)
        # {'platformName': 'Android', 'newCommonTimeout': 500, 'skipServerInstallation': True, 'noReset': True,
        # 'deviceName': 'D5F0218710007612', 'platform_version': '10',
        # 'appPackage': "'com.xkw.client'", 'appActivity': "'com.zxxk.page.main.LauncherActivity'",
        # 'udid': 'D5F0218710007612', 'systemPort': 8200}

        driver = webdriver.Remote(f"http://127.0.0.1:{self.device_info['server_port']}/wd/hub", desired_caps)
        return driver
