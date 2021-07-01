""""
实现发礼物，之后展示礼物
1、默认值（have_gift = False）没有礼物
2、定义一个发礼物的方法
3、定义一个显摆礼物的方法
4、实现发完礼物之后，能展示礼物
# print(__name__)     # 此模块被别的模块调用时，__name__的值为python_code.send_gift,只有在运行模块中的__name__值为__main__
"""
# from python_code.gift import have_gift    # 深拷贝：变量地址空间不同，变量名虽然一样，但是两个变量
import gift                                 # 采用”模块名.变量名“的方式引用即是一个变量


def send_gift():
    gift.have_gift = True
    print("发礼物啦！")

