""""
创建一个Person类：
    属性：姓名、性别、年龄、存款金额
    方法（行为）：吃、睡、跑、赚钱
"""


class Person:
    # pass(类中可以只写pass进行展位)
    # 静态属性
    name = None
    gender = "男"
    age = 0
    # 私有属性:变量名前加'__',该变量不能直接方位，可以采用方法返回该值
    __money = 1000

    def __init__(self, name, gender, age):        # 构造方法，实例化时就会执行
        print("__init__")
        self.name = name
        self.gender = gender
        self.age = age

    # 动态方法
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def running(self):
        print(f"{self.name} is running")

    def have_money(self):    # 私有属性可以采用此种方法进行访问
        return self.__money

    def __get_money(self):   # 私有方法
        return self.__money + 1000
