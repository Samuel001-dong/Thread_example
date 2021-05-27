""""
pytest fixture练习
1、fixture是在测试函数运行前后，有pytest执行的外壳函数，代码可以定制，满足多变的测试需求，功能包括
    定义传入测试中的数据集
    配置测试前系统的初始状态
    为批量测试提供数据源等
2、fixture是pytest用于将测试前后进行预备，清理工作的代码分离出核心测试逻辑的一种机制
3、用法：
    为了测试用例的执行，初始化一些数据和方法
        类似setUp,tearDown功能，但比setUp，tearDown更灵活
        直接通过函数名字调用或使用装饰器@pytest.mark.usefixtures('test1')
        允许使用多个Fixture
        使用autouse自动化应用（@pytest.fixture(autouse=True)表示所有的用例都要执行这个动作），如果要返回值，需要传fixture函数名
        作用域（session>package>module>class>function）
    --setup-show 回溯fixture的执行过程
4、yield后面的语句将会在自动激活fixture的teardown功能，并在teardown中执行
5、前端自动化中的应用-conftest
    场景：你与其他测试工程师合作一起开发时，公共的模块要在不同的文件中，要在大家都访问到的地方。
    解决：使用conftest这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用。
    前提：
        conftest这个文件名不能换的，放在项目下是全局的数据共享的地方，全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方。
    执行：系统执行到参数login时先从本文件中查找是否有这个名字的fixture方法，之后在conftest.py中找是否有。
    步骤：将登录模块带@pytest.fixture写在conftest.py
6、pytest常用的插件
pip install pytest-ordering 控制用例的执行顺序
pip install pytest-dependency 控制用例的依赖关系
pip install pytest-xdist 分布式并发执行测试用例
pip install pytest-rerunfailures 失败重跑
pip install pytest-assume  多重校验
pip install pytest-random-order 用例随机执行
pip install pytest-html 测试报告
"""


def test_search():
    print("搜索")


def test_cart(login):   # 为测试用例添加Login前置条件，如果login有返回值，还可以作为参数传入
    print("添加购物")


def test_order(login, connect_db):      # 多个fixture时放在前面的先执行
    url = f"http://www.baidu.com/token={login}"
    print("下单")
    print(url)


def provider():
    for i in range(0, 10):
        yield i    # 相当于return,并记录上一次的执行位置，下一次继续执行


p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))


