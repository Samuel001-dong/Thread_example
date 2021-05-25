""""
1、pytest是一个非常成熟的全功能的python测试框架
    测试用例的skip和xfail，自动失败重试等处理
    能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）
    pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-allure(完美html测试报告生成)、pytest-xdist(多CPU分发)等
    可以很好的和jenkins集成
2、文档：https://docs.pytest.org/en/latest/contents.html#toc
3、第三方库：https://pypi.org/search/?q=ptest
4、测试用例的识别与运行
    测试文件：
        test_*.py
        *_test.py
    用例识别：
        Test*类包含的所有test_*的方法（测试类不能带有_init_方法）
        不在class中的所有的test_*方法
    pytest也可以执行unittest框架写的用例和方法
5、
"""
import pytest


def func(x):
    return x + 1


# 测试用例的参数化
@pytest.mark.parametrize('a, b', [
    (1, 2),
    (10, 11),
    (55, 56)
])
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    username = 'Jerry'
    return username


class TestDemo:
    def test_a(self, login):
        print(f"a  username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c   username = {login}")


if __name__ == '__main__':
    pytest.main(['test_frame.py::TestDemo', '-v'])
