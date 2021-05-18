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
        # print("__init__")
        self.name = name
        self.gender = gender
        self.age = age

    # 动态方法
    def eat(self):
        print(f"{self.name} is eating")

    @classmethod   # 如果类名(非实例化)调用方法则需要添加@chassmethod,搭建框架时经常用这种方法
    def sleep(self):
        print(f"{self.name} is sleeping")

    def running(self):
        print(f"{self.name} is running")

    def have_money(self):    # 私有属性可以采用此种方法进行访问
        return self.__money

    def __get_money(self):   # 私有方法
        return self.__money + 1000


class Funny(Person):
    # 继承Person类的属性和方法
    # 新增方法fun()  搞笑方法
    def fun(self):
        print(f"{self.name} is funny")


class Singer(Person):
    # 继承Person类的属性和方法
    # 新增方法make_money() 挣钱方法
    skill: str

    def __init__(self, name, gender, age, skill):   # 在父类的基础上添加新的属性skill,如果不添加新的属性则可以继承父类,不必要下列代码
        # print("__init__")
        # self.name = name
        # self.gender = gender
        # self.age = age
        # 上面几行代码因为父类中已经有了，可以用下面代码代替
        super().__init__(name, gender, age)
        self.skill = skill

    def make_money(self):
        print(f"{self.name} makes many money")
        return 1000


singer1 = Singer(name="董建龙", gender="男", age=20, skill="唱歌")
print(singer1.skill)
print(singer1.running())
print(Funny.sleep())
