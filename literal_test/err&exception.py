""""
错误&异常学习示例
"""
# 除零异常


# def div(x, y):      # 此时y是不能为0的
#     return x/y


# 首先执行try,如果有异常则会执行except(此时try后面的代码不再执行)，没有异常则不会执行except，但无论如何最后都会执行finally
# list1 = [1, 2, 3]
# try:
#     print("try:----------------------")
#     print(div(2, 1))
#     print(list1[0])
# except Exception as e:
#     print("except--------------------")
#     print(e)
# else:
#     print("无异常发生------------------")
# finally:
#     print("finally:------------------")
#     a = 1
def set_age(num):
    if num <= 0 or num > 200:
        raise ValueError(f"值错误：{num}")       # 自己抛出一个异常
    else:
        print(f"设置年龄为：{num}")


set_age(-1)
