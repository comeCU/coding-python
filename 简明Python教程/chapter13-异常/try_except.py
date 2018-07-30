#!/usr/bin/env python
# filename: try_except.py

import sys

try:
    s = input('Enter something -->')
except EOFError:    # 输入 Ctrl+d 文件末尾
    print('\nWhy did you doan EOF on me?')
    sys.exit()
except:
    print('\nSome error/exception occurred.')

print('Done')
