##回合制格斗游戏
1.一个回合制游戏,每个角色都有hp和power,hp代表血量,power代表攻击力,
hp的初始值为1000,power的初始值为200
2.定义一个fight方法:
3.my_hp = hp - enemy_power
4.enemy_final_hp = enemy_hp - my_power
5.两个hp进行对比,血量剩余多的人获胜

# ------------------------------classmethod与staticmethod区别------------------------------------------
使用Pycharm进行Python开发时，在类中定义方法时，若该方法不涉及对属性的操作，那么Pycharm会提示Method xxx may be 'static',因为Pycharm会认为该方法是一个静态方法，而不是类方法，所提提示我们在该方法前添加@staticmethod装饰器进行装饰。

简单记录一下classmethod和staticmethod的区别：

classmethod是类方法，而staticmethod是静态方法。

在python中，静态方法和类方法都是可以通过类对象和类对象实例访问。但是区别是：
@classmethod 是一个函数修饰符，它表示接下来的是一个类方法，类方法的第一个参数cls，而实例方法的第一个参数是self，表示该类的一个实例。
普通对象方法至少需要一个self参数，代表类对象实例
类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。 对于类方法，可以通过类来调用，比如说A是一个类，那么我们可以通过A.method()来调用A里面的method方法， 也可以通过类的一个实例来调用，如A().method()进行调用，首先A()方法会调用A的初始化方法进行实例化出一个A的对象，然后通过该对象调用method方法。
静态方法则没有上述方法，它基本上跟一个全局函数相同，一般来说用的很少
————————————————
版权声明：本文为CSDN博主「程序员小熊」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiongchun11/article/details/78202113