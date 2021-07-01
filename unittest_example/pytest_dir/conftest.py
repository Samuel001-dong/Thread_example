""""
1、前端自动化中的应用-conftest
    场景：你与其他测试工程师合作一起开发时，公共的模块要在不同的文件中，要在大家都访问到的地方。
    解决：使用conftest这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用。
    前提：
        conftest这个文件名不能换的，放在项目下是全局的数据共享的地方，全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方。
    执行：系统执行到参数login时先从本文件中查找是否有这个名字的fixture方法，之后在conftest.py中找是否有。
    步骤：将登录模块带@pytest.fixture写在conftest.py
    注意：conftest.py文件就近生效（如果在不同的文件夹下都有conftest.py）
2、@pytest.fixture中scope解释：
    session：当执行本文件下所有的文件（包括该文件目录下的子目录）之前执行该fixture(setup部分)，并在所有用例结束后执行teardown部分

"""
import pytest


@pytest.fixture    # (scope="session", autouse=True)   # 默认是方法级别，设置参数为scope
def login():
    token = "dsjfasdlkalskdflasdjlkasdlkkfjd"
    print("登录操作")   # setup部分
    yield token     # login返回值
    print("登出操作")   # teardown部分


@pytest.fixture
def connect_db():
    print("连接数据库")
    yield     # 相当于激活fixture的teardown功能
    print("断开数据库")
