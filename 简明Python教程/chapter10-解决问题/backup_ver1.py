#!/usr/bin/env python
# filename: backup_ver1.py
# 备份文件并打包成zip格式
# 版本一

import os
import time

# 1.需要备份打包的文件列表
# 注意：windows下目录格式
source = [r'C:\Users\Administrator\Desktop\test_backup1', r'C:\Users\Administrator\Desktop\test_backup2']

# 2.保存目录
target_dir = r'C:\Users\Administrator\Desktop\backup/' #windows下目录写法

# 3.保存后生成文件目录，文件名为当前日期时间
# 4.生成的文件为zip格式
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5.使用命令对其打包，拼接命令
zip_command = "zip -qr %s %s" %(target, ' '.join(source))   # 注意%s 不需要引号

# 运行
if os.system(zip_command) == 0:
    print('Successful backup to', target)    
else:
    print('Backup failed!')
