""""

"""
# from python_code.gift import have_gift     # 深拷贝：变量地址空间不同，变量名虽然一样，但是两个变量
import gift                                  # 采用”模块名.变量名“的方式引用即是一个变量


def show_gift():
    if gift.have_gift:
        print("收到礼物啦，好开心！")
    else:
        print("等待礼物中...")
