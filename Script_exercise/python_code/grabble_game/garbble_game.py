""""
1.一个回合制游戏,每个角色都有hp和power,hp代表血量,power代表攻击力,
hp的初始值为1000,power的初始值为200
2.定义一个fight方法:
3.my_hp = hp - enemy_power
4.enemy_final_hp = enemy_hp - my_power
5.两个hp进行对比,血量剩余多的人获胜
"""


class Game:
    def __init__(self, my_hp, enemy_hp):     # 构造函数
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 200

    def fight(self):
        while True:
            # 血量计算公式
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(f"我的血量:{self.my_hp}\n敌人的血量:{self.enemy_hp}")
            # 三目表达式
            # print("我赢了!") if my_hp > enemy_final_hp else print("对方胜利!")
            if self.my_hp > self.enemy_hp:
                print("我赢了!")
                break
            else:
                print("对方胜利!")
                break

    @staticmethod
    def back_home():
        print("回城~")


# Hero类继承Game类,多了一个防御力的参数
class Hero(Game):
    def __init__(self, my_hp, enemy_hp):  # 继承父类时父类的参数在此处输入
        super(Hero, self).__init__(my_hp, enemy_hp)  # 继承父类__init__
        self.defense = 100

    def fight(self):    # hero自身的比赛规则(因为多了一个防御力,故比赛规则与父类不同,需要制定自身的比赛规则)
        while True:
            # 血量计算公式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(f"我的血量:{self.my_hp}\n敌人的血量:{self.enemy_hp}")
            # 三目表达式
            # print("我赢了!") if my_hp > enemy_final_hp else print("对方胜利!")
            if self.my_hp > self.enemy_hp:
                print("我赢了!")
                break
            else:
                print("对方胜利!")
                break


# 调用
# 实例化类
# game1 = Game()
# game1.fight()
hero1 = Hero(1000, 200)
hero1.fight()
hero1.back_home()
