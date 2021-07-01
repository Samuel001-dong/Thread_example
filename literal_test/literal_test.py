# -----------------------------------------------------格式化输出----------------------------------------------------- #
# name = "literal_test"
# age = 3
# print("this is a case of %s ,my age is %d" % (name, age))
# -----------------------------------------------------format----------------------------------------------------- #
""""
支持字符串、列表、字典
"""
# name = "Samuel"
# age = 27
# print("my name is {},my age is {}.".format(name, age))
# print("we are the {} and {}.".format("Tom", "Jerry"))    # 其中{}是可以添加索引的，默认是从0开始,添加索引用法如下列
# # format中的元素并不一定都要用
# print("we have the same name ,my name is {0},his name is {0}.and we are both {0}".format(name, age))
# print("we have the same name ,my name is {0},his name is {0}.and our age are both {1}".format(name, age))
# 列表、字典
# 列表：*解包
# 字典：**解包
# list_literal = [0, 1, 2, 3]
# dict_literal = {"name": "Samuel", "gender": "male", "age": 27}        # 打印列表和字典的全部元素不要加*
# print("my list is {},my dic is {}".format(list_literal, dict_literal))
# print("my list is {1},my dic is {name}".format(*list_literal, **dict_literal))
# print("my list is {0},my dic is {1}".format(list_literal[1], dict_literal))
# print("my list is {3},my dic is {gender}".format(*list_literal, **dict_literal))

# ------------------------------字符串格式化机制（Python3.6以上）----------------------------------------------------- #
# 这种使用方式中列表和字典都不需要解包操作
# 大括号内可以放入变量、常量
formatted_sti = "Samuel"
formatted_age = 27
formatted_list = [1, 2, 3, 4]
formatted_dict = {'name': "Samuel", 'gender': 'male', 'age': 27}
print(f"my name is {formatted_sti},my age is {formatted_age}.")
print(f"my first list is {formatted_list[0]},my first element of dict is {formatted_dict['name']},my name is "
      f"{formatted_sti},my age is {formatted_age}")
# 大括号中可以添加表达式
print(f"my name is {formatted_sti.upper()}")
print(f"this is a expression {(lambda x: x + 2)(2)}")      # 大括号里不准有/ ：等，但是添加一个括号，然后在括号里添加这些元素是可以的

