""""
1：单元测试概述
    单元测试的时候一个大前提就是需要清楚的知道，自己要测试的程序块所预期的输入和输出，然后
    根据这个预期和逻辑来书写case。这里的预期结果一定要针对需求/设计的逻辑去写，
    而不是针对程序的实现去写，否则单测就是去了意义，照着错误的实现设计出的case也很可能是错的

2:unittest框架介绍
    unittest
        python的内置标准类库，它的API和JAVA的unit、.net的nunit很相似
        官网：https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
        python自带的单元测试框架，常用在单元测试
        在自动化测试中提供用例组织与执行
        提供丰富的断言方法-验证函数等功能
        加上HTMLTestTRunner可以生成html的报告
    pytest
        可以结合ALLURE生成一个炫酷的测试报告，现在比较主流
    nose
        对unittest的扩展，使python的测试更加简单
    mock
        unittest.mock是用来测试python的标准库（3.3之后版本出现）
3：unittest实战
------------------------------------------------------------------------------
# unittest详细介绍：
1、unittest提供了test cases、test suits、test fixtures、test runner相关的组件
2、编写规范：
    测试模块首先import unittest
    测试类必须继承unittest.TestCase
    测试方法必须以”test_“开头
3、测试框架结构：
    setUp用来为测试准备环境，tearDown用来清理环境
    如果想要在所有case(同一个类)执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用setUpClass()与tearDownClass();比如数据库连接及销毁
    setUp和tearDown每个用例前后都会执行一次，setUpClass和tearDownClass会在每个类前后执行一次
    如果想有些方法不在本次执行使用@unittest.skip
    测试方法的命名：以test开头
    各种执行-单一用例，全部
4、测试用例的执行顺序：
    测试用例执行顺序是以test后面的字母顺序执行的。例如test_a,test_b,test_c
"""
import logging
import unittest
from time import ctime

logging.basicConfig(level=logging.INFO)


class TestStringMethods(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("setUp")
    #
    # def tearDown(self) -> None:
    #     print("tearDown")

    @classmethod      # 类方法要加列方法装饰器
    def setUpClass(cls) -> None:
        print("setUp Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class")

    def test_upper(self):
        logging.info("test_upper start at " + ctime())
        print("test_upper 111")
        self.assertEqual('foo'.upper(), 'FOO')
        logging.info("test_upper end at " + ctime())

    def test_isupper(self):
        logging.info("test_isupper start at " + ctime())
        print("test_isupper 222")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        logging.info("test_isupper end at " + ctime())

    def test_split(self):
        logging.info("test_split start at " + ctime())
        print("test_split 333")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        logging.info("test_split end at " + ctime())


if __name__ == '__main__':
    unittest.main()
