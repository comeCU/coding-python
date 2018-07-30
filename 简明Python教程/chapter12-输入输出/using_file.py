#!/usr/bin/env python
# filename : using_file.py
# 读文件，python3.5 需要改为open方法。
# 参考回答：https://stackoverflow.com/questions/16736833/python-nameerror-name-file-is-not-defined
# https://docs.python.org/release/3.0/library/functions.html#open

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = open('poem.txt', 'w')   # open for writing
f.write(poem)   # write text to file
f.close()   # close the file

f = open('poem.txt')    #未指定，默认read模式
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end="")

f.close()
