"""
python执行入口
"""
from python_code.gift.send_gift import send_gift
from python_code.gift.show_gift import show_gift

# print(__name__)
if __name__ == '__main__':
    send_gift()
    show_gift()
