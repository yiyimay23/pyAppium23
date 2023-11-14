# _*_coding:utf-8 _*_
# @File　　  :conftest.py
# @Software  :PyCharm

from common.base_driver import BaseDriver
import pytest
import random

from pageViwe.loginPage import LoginPage

driver = None


def pytest_addoption(parser):
    # 注册自定义参数cmdopt到配置对象
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    # 两种写法
    # 从配置对象获取cmdopt的值
    return pytestconfig.getoption("--cmdopt")
    # return pytestconfig.option.cmdopt


# 定义公共的fixture
@pytest.fixture(scope='session')
def common_driver(cmdopt):
    global driver
    base_driver = BaseDriver(eval(cmdopt))
    driver = base_driver.base_driver()
    lg = LoginPage(driver)
    yield lg
    driver.close_app()
    driver.quit()


@pytest.fixture
def device(cmdopt):
    yield eval(cmdopt)


def pytest_itemcollected(item):
    item._nodeid = str(random.randint(1, 1000)) + '_' + item . _nodeid
