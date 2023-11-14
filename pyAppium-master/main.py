# _*_coding:utf-8 _*_
# @File　　  :main.py
# @Software  :PyCharm
from multiprocessing import Pool

import os
import pytest
from common.app_info import get_device_infos
from common.app_info import uninstall_app
from common.appium_auto_server import close_appium


def run_parallel(device_info):
    pytest.main([f"--cmdopt={device_info}",
                 "--alluredir", "outputs/reports/data"])
    os.system("allure generate outputs/reports/data -o outputs/reports/html --clean")


if __name__ == "__main__":
    device_lists = get_device_infos()
    # uninstall_app(device_lists)  # 不是经常更新的版本，可以不需要卸载
    with Pool(len(device_lists)) as pool:
        pool.map(run_parallel, device_lists)
        pool.close()
        pool.join()

    close_appium()

