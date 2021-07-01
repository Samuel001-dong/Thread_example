""""
json由列表和字典组成
"""
import json
data = {'name': ["Samuel", "John"], 'age': 27, 'gender': "male"}
print(type(data))
data1 = json.dumps(data)          # json转化为字符串
print(data1)
print(type(data1))
data2 = json.loads(data1)         # 字符串转化为json
print(data2)
print(type(data2))
