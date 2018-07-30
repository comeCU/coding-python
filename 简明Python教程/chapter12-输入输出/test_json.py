#!/src/bin/env python
# filename: test_json.py
# JSON序列化 反序列化
# 参考：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000

import json
d = dict(name='Bob', age=20, score=88)  # dict字典
json.dumps(d)   # dumps方法返回一个字符串

print(d)


json_str = '{"age":20, "score":88, "name":"Bob"}'
json.loads(json_str) # loads方法将json字符串反序列化

print(json_str)
