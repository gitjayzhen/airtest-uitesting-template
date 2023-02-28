# -*- encoding=utf8 -*-

import base64
import json
import re
import sys

import requests
from faker import Faker
from airtest.core.api import *
from config import emulator_dict


def gen_result_dir():
    """生成报告数据目录路径"""
    report_path = './result/data/' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    return report_path


def touch_image(i_name, record_pos, resolution=(1440, 2560)):
    """重构touch函数"""
    images_path = r'D:\Workspace\lingshi-ui-testing\images'
    return touch(
        Template(images_path + '\\' + i_name, record_pos=record_pos,
                 resolution=resolution))


def adb_connect_emulator():
    """adb连接模拟器函数"""
    for i, v in emulator_dict.items():
        print("正在连接模拟器：{}".format(i), v)
        os.system(v)
        sleep(1)


def get_device_id():
    """获取已连接设备id，并输出"""
    str_init = ""
    all_info = os.popen("adb devices").readlines()
    print("adb devices 输出的内容是:", all_info)

    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)
    try:
        return devices_name[0]
    except IndexError:
        print("没有找到已连接的设备")
        sys.exit()
    except:
        print("未知异常")


# 生成测试数据
def faker_data(num):
    faker = Faker('zh_CN')
    list_data = []
    for i in range(num):
        list_data.append((faker.name(), faker.ssn(), faker.phone_number()))
    return list_data


def base64_api(img, uname="name", pwd="pwd"):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""
