""""
面向对象编程示例
"""


# 创建一个人类:通过class关键字进行定义
class Person:
    name = "default"                # 属性
    age = 0
    gender = "male"
    weight = 0

    # 方法
    def __init__(self, name1, age1, gender1, weight1):                    # 类中的构造方法：初始化方法--->类实例化就会自动执行
        # self.变量名的方式，访问的变量叫做实例变量
        self.name = name1
        self.age = age1
        self.gender = gender1
        self.weight = weight1
        print("def_init")

    def set_para_name(self, name1):
        self.name = name1                        # self.name为类中的属性name,name1为输入的参数

    def set_para_age(self, age1):
        self.age = age1

    @classmethod     # 使得类访问方法可行
    def eat(self):
        print(f"{self.name} eating")

    def play(self):
        print(f"{self.name} play")

    def jump(self):
        print(f"{self.name} jump")

    def print_info(self):
        print(f"姓名:{self.name}\n年龄:{self.age}\n性别:{self.gender}\n体重:{self.weight}")


# 类的实例化
samuel = Person('samuel', 20, '男', 130)
# 类变量和实例变量的区别：都可以被修改
# 类变量是需要被类来访问的，实例变量是需要被实例访问的
print(Person.name)     # 类变量
print(samuel.name)     # 实例变量
# samuel.set_para_name("samuel")
# samuel.set_para_age(20)
samuel.print_info()
# 类方法和实例方法的区别：类方法是不可以访问的（访问时需要添加一个装饰器@calssmethod），实例方法是可以访问的
# 类方法在编写框架的时候会用
Person.eat()
