""""
1.一个回合制游戏,每个角色都有hp和power,hp代表血量,power代表攻击力,
hp的初始值为1000,power的初始值为200
2.定义一个fight方法:
3.my_hp = hp - enemy_power
4.enemy_final_hp = enemy_hp - my_power
5.两个hp进行对比,血量剩余多的人获胜
"""


def fight():
    # 变量初始化
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200
    # 血量计算公式
    my_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power
    # 三目表达式
    # print("我赢了!") if my_hp > enemy_final_hp else print("对方胜利!")
    if my_hp > enemy_final_hp:
        print("我赢了!")
    else:
        print("对方胜利!")


fight()
