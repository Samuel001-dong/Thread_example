# # --------------------------------------------------列表(list)------------------------------------------------------ #
# list_var = [1, 2, 3, 4]
# print(type(list_var))
# print(list_var)
# list_var.append(1)
# list_var.append(2)
# list_var.append(3)
# print(list_var)
# list_var.insert(4, 99)
# print(list_var)
# list_var.remove(3)    # 参数为列表中的值，删除列表中第一个吻合的值
# print(list_var)
# y = list_var.pop(0)   # 参数为索引，并返回删除的值
# print(y)
# print(list_var)
# list_var.sort()       # 列表中的数据增量排序
# print(list_var)
# list_var.sort(reverse=True)  # 列表中的数据降序进行排序
# print(list_var)
# list_var.reverse()           # 相较于之前的列表，进行反向排序
# print(list_var)
# list_var.clear()             # 清空列表中的所有数据
# print(list_var)
# # 列表推导式:方法1：while循环
# var = 1
# var_list = []
# while var < 100:
#     var_2 = var*var
#     var = var+1
#     var_list.append(var_2)
# else:
#     print(var_list)
# # 列表推导式:方法2：for循环、直接使用range(n)就可以产生0~（n-1）的序组
# var_square = []
# for i in range(1, 4):
#     var_square.append(i**2)
# print(var_square)
# # 列表推导式:方法3：for循环->列表推导式
# # var_square2 = []
# var_square2 = [i**2 for i in range(1, 4)]
# print(var_square2)
# # 列表推导式:方法4:for循环加入if判断->列表推导式
# # var_square3 = []
# var_square3 = [i**2 for i in range(4) if i != 0]
# print(var_square3)
# # 列表推导式:方法5：嵌套循环
# var_square4 = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         var_square4.append(i*j)
# print(var_square4)
# # 列表推导式:方法5：嵌套循环->列表推导式
# var_square5 = [i*j for i in range(1, 4) for j in range(1, 4)]
# print(var_square5)
# ---------------------------------元组（tuple）-------------------------------------------------------------------- #
# # 元组的定义
# var_tuple1 = (1, 2, 3, 4)
# var_tuple2 = 1, 2, 3, 4
# print("var_tuple1's type:", type(var_tuple1))
# print("var_tuple2's type:", type(var_tuple2))
# print("var_tuple1:", var_tuple1)
# print("var_tuple2:", var_tuple2)

# # 元组的不可变性:变量指针（地址）
# a = [1, 2, 3]
# var_tuple3 = (1, 2, 2, a)       # 元组中可以嵌套列表
# print(id(var_tuple3[2]))
# print(var_tuple3)
# print(var_tuple3[0])            # 元组内的数据可以进行索引
# # var_tuple3[0] = "a"           # 不可执行：元组不可变
# var_tuple3[3][0] = "a"        # 可以执行：元组内置的列表中的数据可以改变
# print(id(var_tuple3[2]))
# print(var_tuple3)
# print(var_tuple3.count(1))     # 元组中1的个数
# print(var_tuple3.index(2))     # 元组中第一个2的索引

# -----------------------------------------集合（set）--------------------------------------------------------------- #
# 定义(集合本身具有去重功能)
# a = {1, 2, 3}             # 不能为空，若空则类型是字典
# b = {1, 4, 5}
# c = set()                 # 可以为空集合
# # print(len(c))             # 通过查询集合b的长度，可以判断其是否为空集合
# # print(type(a))
#
# # 函数
# print(a.union(b))                # union:并集（两者的集合，两者都有的元素只能保存一个）
# print(a.intersection(b))         # intersection:交集（两者共有的元素）
# print(a.difference(b))           # difference:差集（a有而b没有的元素）
# a.add("a")                       # add:向集合中添加元素
# print(a)
# print({i for i in "sladkjfkasdkkskfkasdklf"})       # 采用推导式的方式创建集合

# -----------------------------------------字典（dict）--------------------------------------------------------------- #
# 定义:key值不可变，若用字母的话需要用字符串
a = {}
var_dict = {"a": 1, "b": 2}
var_dict1 = dict(a=1, b=2)
print("var_dict's type:", type(var_dict))
print("var_dict1's type:", type(var_dict1))
print("var_dict's value:", var_dict)
print("var_dict1's value:", var_dict1)

# 内置函数：
# print(var_dict.keys())               # 所有的key（不可变）
# print(var_dict.values())             # 所有的值
# print(var_dict.pop("a"))             # 删除a（key）,打印返回值（a的值）
# print(var_dict)                      # 打印新的字典（pop操作之后）
# print(var_dict.popitem())            # 随机删除一对键值对,打印返回值（被删除的键值对）
# print(var_dict)                      # 打印新的字典（popitem操作之后）
# b = a.fromkeys((1, 2, 3), "a")         # 建立键值（key）或键值对
# print(a)
# print(b)

# 字典推导式
c = {i: i**2 for i in range(1, 5)}
print("c's type", type(c))
print(c)
