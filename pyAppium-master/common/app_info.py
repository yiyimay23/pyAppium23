# _*_coding:utf-8 _*_
# @File　　  :app_info.py
# @Software  :PyCharm
import logging
import os
from common.all_path import appPath


def exec_cmd(cmd) -> str:
    result = os.popen(cmd).read()
    logging.info(str(result))
    return result


def get_app_name(file_dir) -> str:
    for root, dirs, files in os.walk(file_dir):
        files = [file for file in files if file.endswith(".apk")]
        if len(files) == 1:
            return files[0]
        else:
            raise FileNotFoundError("{}目录下没有测试包或者存在多个测试包。。".format(file_dir))


def get_app_package_name() -> str:
    cmd = "aapt dump badging {} | findstr package".format(os.path.join(appPath, get_app_name(appPath)))
    result = exec_cmd(cmd)
    if "package" in result:
        package_name = result.strip().split(" ")[1].split('=')[1]
        # print(package_name)
        return package_name
    else:
        raise NameError("未获取到package name。")


def get_app_launchable_activity() -> str:
    cmd = "aapt dump badging {} | findstr launchable".format(os.path.join(appPath, get_app_name(appPath)))
    result = exec_cmd(cmd)
    # logging.info(result)  # 不同的设备结果不同
    # launchable-activity: name='com.zxxk.page.main.LauncherActivity'  label='' icon=''
    if "launchable" in result:
        # launchable_parts = result.strip().split(" ")[2].split('=')
        launchable_parts = result.strip().split(" ")[1].split('=')  # 上面指令运行时，获取不到activity,把[2]改为[1]后可运行
        # logging.info(launchable_parts)
        # ['name', "'com.zxxk.page.main.LauncherActivity'"]
        if len(launchable_parts) > 1:
            launchable_activity = launchable_parts[1].replace("label", '')
            # logging.info(launchable_activity)
            return launchable_activity
        else:
            raise NameError("未获取到launchable activity。")
            # print("无法获取可启动活动")
            # return ""
    else:
        raise NameError("未找到可启动活动")
        # print("未找到可启动活动")
        # return ""
    # if "launchable" in result:
    #     launchable_activity = result.strip().split(" ")[2].split('=')[1].replace("label", '')
    #     return launchable_activity
    # else:
    #     raise NameError("未获取到launchable activity。")


def get_devices_version(device: str) -> str:
    if not isinstance(device, str):
        raise Exception("device type is should str..")
    result = exec_cmd("adb -s {} shell getprop ro.build.version.release".format(device))
    result = result.strip()
    if "error" not in result:
        return result
    else:
        raise Exception("获取设备系统版本失败，无法进行正常测试。。")


def get_all_devices() -> list:
    result = exec_cmd('adb devices')
    result = result.strip().split(" ")[3].replace("\n", '').replace("\t", ''). \
        replace("attached", '').split('device')
    result.remove('')
    if len(result) == 0:
        raise Exception("电脑未连接设备信息，无法进行正常测试。。")

    return result


def get_device_infos():  # 将所有的devices整合成字典
    device_infos = []
    devices = get_all_devices()
    for i in range(len(devices)):
        device_dict = {"platform_version": get_devices_version(devices[i]), "server_port": 4723 + i * 2,
                       "system_port": 8200 + i * 1, "device": devices[i]}
        device_infos.append(device_dict)

    if len(device_infos) < 1:
        raise Exception("当前电脑未连接设备信息。。。")

    return device_infos


def uninstall_app(device_list: list) -> None:
    if not isinstance(device_list, list):
        raise Exception("device_list is should list!")

    for device_info in device_list:
        cmd = 'adb -s 127.0.0.1:{} uninstall "{}"'.format(device_info.get("device").split(':')[-1],
                                                          str(get_app_package_name())).replace("'", '')
        logging.info("开始卸载设备上应用：{}".format(cmd))
        exec_cmd(cmd)


app_path = os.path.join(appPath, get_app_name(appPath))  # apk的绝对路径
