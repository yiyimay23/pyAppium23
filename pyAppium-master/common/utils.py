# _*_coding:utf-8 _*_
# @File　　  :utils.py
# @Software  :PyCharm
import re
import logging


def re_extract(data, rePath):
    try:
        return re.findall(rePath, data)
    except Exception as e:
        logging.exception("提取执行失败！{}".format(e))
    return None
