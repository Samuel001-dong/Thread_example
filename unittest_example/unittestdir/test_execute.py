""""
unittest执行测试用例
1、多个测试用例的集合就是测试套件，通过测试套件来管理多个测试用例
2、执行方法：
    1、执行方法一、unittest.main()
    2、执行方法二(创建测试套件，批量执行测试用例)、
        suite = unittest.TestSuite()
        suite.addTest(TestMethod("test_01"))
        suite.addTest(TestMethod("test_02"))
        unittest.TextTestRunner().run(suite)
    3、方法三：同时执行多个类
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
        suite = unittest.TestSuite([suite1, suite2])
        unittest.TextTestRunner(verbosity = 2).run(suite)
    4、方法四：
        匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
        test_dir = "./test_case"
        discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
        unittest.TextTestRunner().run(discover)
            discover可以一次调用多个脚本
            test_dir被测试脚本的路径
            pattern脚本名称匹配规则
3、pycharm软件存在bug,如果想要执行套件中的测试用例，需要在命令行中输入“python 文件名”
4、测试用例执行过程
    首先是要写好TestCase
    然后由TestLoader加载TestCase到TestSuite
    然后由TextTestRunner来运行TestSuite
    运行的结果保存在TextTestResult中
    整个过程继承在unittest.main模块中
5、unittest结合htmltestrunner生成带日志的测试报告
    版本（python2）: http://tungwaiyip.info/software/HTMLTestTunner.html
    版本（python3）: https://github.com/huilansame/HTMLTestRunner_PY3

"""
import unittest


class Search:
    def search_fun(self):
        print("search_fun")
        return True


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class-方法级别")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class-方法级别")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        self.assertTrue(self.search.search_fun())

    def test_search2(self):
        print("test_search2")
        # search = Search()
        self.assertTrue(self.search.search_fun())

    def test_search3(self):
        print("test_search3")
        # search = Search()
        self.assertTrue(self.search.search_fun())


class TestSearch1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class1-方法级别")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class1-方法级别")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        self.assertTrue(self.search.search_fun())

    def test_search2(self):
        print("test_search2")
        # search = Search()
        self.assertTrue(self.search.search_fun())

    def test_search3(self):
        print("test_search3")
        # search = Search()
        self.assertTrue(self.search.search_fun())

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1, 1, "判断1 == 1")

    def test_notequal(self):
        print("断言不相等！")
        self.assertNotEqual(1, 2, "1 != 2")


# if __name__ == '__main__':
    # unittest.main()           # 方法一：执行当前文件所有的测试用例
    # 创建一个测试套件，testsuite()      # 方法二：执行指定的测试用例，将要执行的用例添加到测试套件里，批量执行
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch1("test_search1"))
    # suite.addTest(TestSearch1("test_search2"))
    # unittest.TextTestRunner().run(suite)
    # 方法三：执行某个/多个测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
