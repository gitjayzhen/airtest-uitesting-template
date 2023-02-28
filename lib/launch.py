# -*- encoding=utf8 -*-

from airtest.cli.parser import cli_setup
from airtest.core.api import auto_setup, start_app
from airtest.core.settings import Settings as ST

from lib.tools import adb_connect_emulator, get_device_id


def init_config():
    # adb连接安卓模拟器函数
    # adb_connect_emulator()
    # 获取已连接设备id，并输出
    # device_id = get_device_id()

    if not cli_setup():
        # 用来初始化环境的接口auto_setup
        auto_setup(__file__, devices=["iOS:///http://127.0.0.1:8100"])
    start_app("package.activity")

    ST.FIND_TIMEOUT = 10
    ST.FIND_TIMEOUT_TMP = 10
    ST.SAVE_IMAGE = False
    ST.THRESHOLD = 0.8
