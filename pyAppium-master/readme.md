# pyAppium
## 项目介绍
   pyAppium是python语言，基于PO模式的pytest、Appium二次封装的Android自动化框架，多进程方式在多台手机上同时执行测试，自动获取已连接设备信息，自动启动多个appium服务，同一套测试用例在不同手机上执行，用例执行失败自动截图、收集报错信息，allure插件生成测试报告
## 框架目录说明
```
pyAppium		# 项目根目录
├─app			# 测试APP存放目录
├─common		# 公共模块目录
├─config		# 配置文件目录
├─data			# 测试数据目录
├─outputs		# 测试输出目录
│  ├─logs		# 日志目录
│  ├─picture	# 截图存放目录
│  └─reports	# 测试报告存放目录
├─pageViwe		# PO模式页面封装模块
└─testcase		# 测试用例目录
```

## 主要功能

 1. 自动启动appium server和杀掉appium server
 2. 自动获取电脑连接设备信息，如设备版本、设备udid
 3. 自动检测端口是否可用、释放占用端口
 4. 自动获取测试APP应用相关信息，如：appPackage、launchable_activity
 5. 自动安装APP和卸载APP
 6. 测试用例无需配置，自动获取用例执行，测试人员只需编写相关case
 7. 用例执行失败自动截图、收集错误日志信息，自动加到测试报告对应case下面
 8. 启动一次APP，执行所有测试用例，缩短测试用例执行间隔，提高测试执行效率
 9. 多进程方式在多台手机上同时执行测试，大幅提高测试效率

## 框架使用
### 测试环境

 - win10 64  pycharm2019
 - python 3.7.0 及以上
 - node  v12.16.3
 - appium1.20.2
 - java version "1.8.0_181"
 - Android SDK [百度云分享地址](https://pan.baidu.com/s/1ulXhwv_g0w2qhz3OW-LCSg) 密码：6666
### 环境安装
 - pycharm2019 安装
	- 自行百度安装，或者留言联系。
	
 - python环境
 - 安装包下载：[点击去下载](https://www.python.org/downloads/release/python-373/) 自行选择相应版本
 - 下载后点击exe，根据提示安装即可，不会自行百度
 - 环境检测：在cmd命令终端输入：`python`
 ![pyth版本](https://img-blog.csdnimg.cn/20210624221337510.png#pic_center)
 - node 安装
	- 安装包下载：[点击去下载](https://npm.taobao.org/mirrors/node/v12.16.3/) 自行选择相应版本
	- 下载后点击exe，根据提示安装即可，不会自行百度
	- 环境检测：在cmd命令终端输入：`node -v`
	![node 版本检测](https://img-blog.csdnimg.cn/20210624221807165.png#pic_center)
 - jdk 安装
	- 安装包下载：[点击去下载](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)  自行选择相应版本
	- 下载后点击exe，根据提示安装即可，不会自行百度
	- 配置环境变量：
		- 新建环境变量：JAVA_HOME 如值为：D:\Java\jdk1.8.0_181\bin
		- 在系统变量 Path 的值的前面加入以下内容：%JAVA_HOME%\bin
	- 环境检测：在cmd命令终端输入：`java -version`
	![java环境检测](https://img-blog.csdnimg.cn/20210624222454995.png)
 - Android SDK 安装
	- 从上面百度云下载 Android sdk 解压到一个目录，不要包含空格、中文路径
	- 新建环境变量：ANDROID_HOME 值为:F:\Andriod_SDK
	- 在系统变量 Path 的值的前面加入以下内容：%ANDROID_HOME%\platform-tools、%ANDROID_HOME%\tools
	- 环境检测：在cmd命令终端输入：`adb version`
	![Android SDK检测](https://img-blog.csdnimg.cn/20210624222804904.png)
 - appium 安装
	- 安装 node.js，配置 node.js 的环境变量 `已完成`
	- 配置国内淘宝源 `npm config set registry https://registry.npm.taobao.org`
	![配置淘宝源](https://img-blog.csdnimg.cn/20210624223220939.png)

	- 安装指定版本appium ：`npm install -g appium@1.20.2` 等待安装完成
	- 环境检测：在cmd命令终端输入：`appium -v`
	![appium 版本查看](https://img-blog.csdnimg.cn/2021062422343182.png)
	- 安装appium-doctor: `npm install appium-doctor -g` 作用：检查appium环境是否完整
	![appium-doctor 检查](https://img-blog.csdnimg.cn/20210624223553935.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTQxMTc=,size_16,color_FFFFFF,t_70)
### 下载框架源码
1.仓库地址：`https://gitee.com/King15800/pyAppium.git`
2.下载源码：`git clone https://gitee.com/King15800/pyAppium.git`
3.使用pycharm 打开源码项目
4.安装项目依赖包：`pip install -r requirements.txt`
### 使用说明
 - 启动项目正常运行前提：
 	- 有手机正常已经连接电脑
 	- 修改 `test_login.py`文件输入账号信息，本`demo`基于`学科网APP`编写
 	- 已下载APP，放到项目目录`App`下
 - 启动项目：直接运行`main.py`文件即可。

## 关键代码说明
**启动入口说明** `main.py`
- `def run_parallel(device_info)` 定义一个pytest 启动入口，根据设备进行启动，一个设备启动一个

```python
def run_parallel(device_info):
    pytest.main([f"--cmdopt={device_info}",
                 "--alluredir", "outputs/reports/data"])
    os.system("allure generate outputs/reports/data -o outputs/reports/html --clean")
```
- 根据设备数量，使用进程池创建进程进行测试

```python
	device_lists = get_device_infos() # 获取连接设备信息
    uninstall_app(device_lists)  # 卸载APP
    with Pool(len(device_lists)) as pool:
        pool.map(run_parallel, device_lists)
        pool.close()
        pool.join()
```
- 完整代码
```python
# _*_coding:utf-8 _*_
# @Time　　:2021/6/21 22:33
# @Author　 : king
# @File　　  :main.py
# @Software  :PyCharm
from multiprocessing import Pool

import os
import pytest
from common.app_info import get_device_infos, uninstall_app
from common.appium_auto_server import close_appium


def run_parallel(device_info):
    pytest.main([f"--cmdopt={device_info}",
                 "--alluredir", "outputs/reports/data"])
    os.system("allure generate outputs/reports/data -o outputs/reports/html --clean")


if __name__ == "__main__":
    device_lists = get_device_infos()
    uninstall_app(device_lists)
    with Pool(len(device_lists)) as pool:
        pool.map(run_parallel, device_lists)
        pool.close()
        pool.join()
```
**driver实现** `base_driver.py`

```python
class BaseDriver:

    def __init__(self, device_info):
        self.device_info = device_info
        cmd = "start /b appium -a 127.0.0.1 -p {0} -bp {1}".format(self.device_info["server_port"],
                                                                   self.device_info["server_port"] + 1)
        open_appium(cmd, self.device_info["server_port"])

    def base_driver(self, automationName="appium"):
        fp = open(f"{configPath}//caps.yml", encoding='utf-8')
        # 平台名称、包名、Activity名称、超时时间、是否重置、server_ip、
        desired_caps = yaml.load(fp, Loader=yaml.FullLoader)

        # 设备名称
        desired_caps["deviceName"] = self.device_info['device']

        # 版本信息
        desired_caps["platform_version"] = get_devices_version(desired_caps["deviceName"])

        app_path = os.path.join(appPath, get_app_name(appPath))
        desired_caps['app'] = app_path

        desired_caps['appPackage'] = get_app_package_name()

        desired_caps['appActivity'] = get_app_launchable_activity()

        # udid
        desired_caps["udid"] = self.device_info['device']
        # 系统端口号
        desired_caps["systemPort"] = self.device_info["system_port"]

        if automationName != "appium":
            desired_caps["automationName"] = automationName

        driver = webdriver.Remote(f"http://127.0.0.1:{self.device_info['server_port']}/wd/hub",
                                  desired_capabilities=desired_caps)
        return driver
```
**核心conftest文件** `conftest.py`

```python
from common.base_driver import BaseDriver
import pytest
import random

from pageViwe.loginPage import LoginPage

driver = None


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


@pytest.fixture(scope='session')
def cmdopt(pytestconfig):
    # 两种写法
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

# 报告中区分多设备执行结果
def pytest_itemcollected(item):
    item._nodeid = str(random.randint(1, 1000)) + '_' + item . _nodeid
```

## 执行结果
### 执行日志

> 2021-06-24-23-10-15-basePage.py-basePage-find_element-33-INFO-同意协议 页面开始查找元素('id', 'com.xkw.client:id/agree_yes')
2021-06-24-23-10-16-basePage.py-basePage-find_element-36-INFO-同意协议 页面查找元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-16-basePage.py-basePage-click_element-61-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')
2021-06-24-23-10-16-basePage.py-basePage-click_element-63-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-17-basePage.py-basePage-find_element-36-INFO-同意协议 页面查找元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-17-basePage.py-basePage-click_element-61-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')
2021-06-24-23-10-17-basePage.py-basePage-click_element-63-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-18-basePage.py-basePage-is_element_exist-105-INFO-发现 页面开始查找元素 ('id', 'com.xkw.client:id/discover_search_box')
2021-06-24-23-10-18-basePage.py-basePage-is_element_exist-108-INFO-发现 页面查找元素 ('id', 'com.xkw.client:id/discover_search_box')成功！
2021-06-24-23-10-18-basePage.py-basePage-get_size-121-INFO-开始获取设备屏幕大小。
2021-06-24-23-10-18-basePage.py-basePage-get_size-125-INFO-获取设备屏幕大小完成。(720, 1280)
2021-06-24-23-10-18-basePage.py-basePage-swipe_to_up-167-INFO-首页 页面开始进行上滑
2021-06-24-23-10-19-basePage.py-basePage-is_element_exist-105-INFO-发现 页面开始查找元素 ('id', 'com.xkw.client:id/discover_search_box')
2021-06-24-23-10-19-basePage.py-basePage-find_element-36-INFO-同意协议 页面查找元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-19-basePage.py-basePage-click_element-61-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')
2021-06-24-23-10-19-basePage.py-basePage-click_element-63-INFO-同意协议 页面点击元素('id', 'com.xkw.client:id/agree_yes')成功！
2021-06-24-23-10-19-basePage.py-basePage-is_element_exist-108-INFO-发现 页面查找元素 ('id', 'com.xkw.client:id/discover_search_box')成功！
2021-06-24-23-10-19-basePage.py-basePage-get_size-121-INFO-开始获取设备屏幕大小。
2021-06-24-23-10-19-basePage.py-basePage-get_size-125-INFO-获取设备屏幕大小完成。(720, 1280)
2021-06-24-23-10-19-basePage.py-basePage-swipe_to_up-167-INFO-首页 页面开始进行上滑
2021-06-24-23-10-20-basePage.py-basePage-swipe_to_up-169-INFO-首页 页面开始上滑完成。
### 测试报告
- 执行时启动了3台模拟器，case 标题动态生成，可以自行修改，目前是功能名称+设备udid
![测试用例收集结果](https://img-blog.csdnimg.cn/20210624232423836.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTQxMTc=,size_16,color_FFFFFF,t_70)
![执行失败自动截图加入到报告](https://img-blog.csdnimg.cn/20210624235205639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTQxMTc=,size_16,color_FFFFFF,t_70)

**注意点**
- 由于使用`pytest`的自带日志模块，修改`pytest` 自带loging文件的写入模式，保证记录完整日志信息，文件路径`F:\appium_env\Lib\site-packages\_pytest\logging.py` 需要根据自己环境地址进入
- 将`mode='w'` 改成 `mode='a'`  在文件**505**行左右
```python
        if log_file:
            self.log_file_handler = logging.FileHandler(
                log_file, mode="a", encoding="UTF-8"
            )
```
 ## 未来规划
 - 集成到Jenkins
 - 不同机器能够采用不同数据
 - 可以对于无线连接手机进行测试
 - appium server远程分布式调用执行


## 有问题，联系方式
- QQ：772084279 备注 pyAppium
- 个人微信公众号：![微信号公众号](https://img-blog.csdnimg.cn/20210705213607967.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTQxMTc=,size_16,color_FFFFFF,t_70)

> 如果您觉得对你有帮助，可以进行留言评论
> 有任何问题，可以联系我，进行询问，不限于此框架问题
