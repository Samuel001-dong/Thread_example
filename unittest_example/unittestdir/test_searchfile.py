""""

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
#     unittest.main()
