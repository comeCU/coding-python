# -*- coding:utf-8 -*-
# 插入U盘复制盘符下的目标文件

import os
import time
from datetime import datetime
import shutil

# U盘的盘符
usb_path = "H:/test"    #必须是目录名，不带有文件
# 要复制到的路径
save_path = "C:/Users/Administrator/Desktop/"

while (True):
    if os.path.exists(usb_path):
        shutil.copytree(usb_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))    #以系统时间命名
        break
    else:
        time.sleep(10)
