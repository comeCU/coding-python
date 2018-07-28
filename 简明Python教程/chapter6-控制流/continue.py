# filename : continue.py

while True:
    s = input('Enter sonething:')
    if s == 'quit':
        break
    if len(s) < 3:
        continue #跳出内层循环
    print('Input is of sufficient length')
