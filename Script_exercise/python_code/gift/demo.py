""""
脚本编写实战1
"""
# a = 1
#
#
# def demo1():
#     global a       # 告诉解释器此处的a为全局变量中的a
#     a = 2
#     print(a)
#     print(id(a))
#     # return None    # 方法中都是默认返回None
#
#
# print(a)
# print(id(a))
# demo1()
# print(a)          # 方法demo1中已经把a的值改变了
#
#
# # python支持嵌套函数、闭包函数
# def outer():
#     def inner():
#         print("inner")
#     return inner
#
#
# outer()()   # 调用inner方法


# -------------------浅拷贝与深拷贝的区别----------------------------------- #
# 浅拷贝：只拷贝第一层（第一层的空间地址不一样）
import copy

word1 = ['hello', 'samuel', 'Hogwarts', ['name', 'mine']]
word2 = word1.copy()
word1[0] = "你好"
print(word1)
print(word2)
word1[3][0] = "郝敏"
print(word1)
print(word2)
# 深拷贝：完全拷贝出一个新的内容（地址完全不同）
# word3 = copy.deepcopy(word1)
# word1[0] = "你好"
# print(word1)
# print(word3)
# word1[3][0] = "郝敏"
# print(word1)
# print(word3)
