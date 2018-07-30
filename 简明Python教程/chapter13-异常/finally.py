#!/usr/bin/env python
# filename: finally.py

import time

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line, end="")

except:
    print('文件不存在，无法打开')
finally:
    try:
        f.close()
    except:
        print('文件不存在，无需close')
    else: 
        print('Cleaning up ...closed the file')
