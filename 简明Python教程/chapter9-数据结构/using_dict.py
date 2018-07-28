#!/usr/bin/env python
# filename : using_dict.py
# 字典  键值对

'''
ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }
'''
# printAll方法打印字典所有
def printAll():
    global ab #全局
    
    for name, address in ab.items():
        print('Contact %s at %s'%(name, address))


ab = {
        'aaa'   :   '111@qq.com',
        'bbb'   :   '222@qq.oom',
        'ccc'   :   '333@qq.com',
        'ddd'   :   '444@qq.com'
    }

print("aaa's address is %s"%ab['aaa'])

# Adding a key/value pair
ab['eee'] = '555@qq.com'
print('\nThere are %d contacts in the address-book\n'%len(ab))
#printAll()


# Deleting a key/value pair
del ab['ddd']
printAll()


if 'eee' in ab:
    print("\neee's address is %s"%ab['eee'])
