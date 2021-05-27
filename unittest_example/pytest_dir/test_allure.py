""""
1、allure介绍：
    allure是一个轻量级，灵活的，支持多语言的测试报告工具
    多平台的，奢华的report框架：
    可以为dev/qa提供详尽的测试报告、测试步骤、log;
    也可以为管理层提供high level统计报告；
    Java语言开发的，支持pytest,JavaScript,PHP,ruby等
    可以集成到Jenkins
2、官网：https://demo.qameta.io/allure/#
3、allure安装：
    windows/mac通用安装方法：
        https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
        下载allure2.7zip包
        解压->进入bin目录->运行allure.bat
        把bin目录加入PATH环境变量
4、使用allure2生成精美报告
    安装allure-pytest插件
        pip install allure-pytest
    运行：
        在测试执行期间收集结果：
            pytest [测试文件] -s -q --alluredir=./result/(--alluredir这个选项用于指定存储测试结果的路径)
        查看测试报告：
            方式一：测试完成后查看实际报告，在线看报告，会直接打开默认浏览器显示当前报告
                allure serve ./result/(注意这里serve书写)
            方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告、打开报告
                生成报告：
                    allure generate ./result/ -o ./report/ --clean(注意：覆盖路径加--clean)
                打开报告：
                    allure open -h 127.0.0.1 -p 8883 ./report
5、Allure常用的特性：
    场景：
        希望在报告中看到测试功能，子功能或场景，测试步骤，包括测试附加信息
    解决：
        @Feature,@story,@step,@attach
    步骤：
        import allure
        功能上加@allure.feature('功能名称')
        子功能上加@allure.story('子功能名称')
        步骤上加@allure.step('步骤细节')
        @allure.attach('具体文本信息')，需要附加的信息，可以是数据，文本，图片，视频，网页
        如果只测试登录功能的时候可以加限制过滤：
            pytest 文本名 --allure-features "购物车功能" --allure-stories "加入购物车"（注意这里--allure-features中间是-中线）
6、allure特性-testcase
    关联测试用例（可以直接给测试用例的地址链接）
    eg:
        TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
        @allure.testcase(TEST_CASE_LINK,'Test case title')
        def test_with_testcase_link():
            pass
7、按重要性级别进行一定范围测试
    场景：
        通常测试有P0、冒烟测试、验证上线测试。按重要性级别来分别执行的，比如上线要把主流程和重要模块 都跑一遍。
    解决：
        通过附加pytest.mark标记
        通过allure.feature,allure.story
        也可以通过allure.severity附加标记
            级别：Trivial:不重要，Minor:不太重要，Normal:正常问题，Critical：严重，Blocker:阻塞
            Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
            Critical级别：临界缺陷（功能点缺失）
            Normal级别：普通缺陷（数值计算错误）
            Minor级别：次要缺陷（界面错误与UI需求不符）
            Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
    步骤：
        在方法，函数和类上面加
            @allure.severity(allure.severity_level.TRIVIAL)
        执行时
            pytest -s -v 文件名 --allure-severities normal,critical
8、前端自动化测试-截图
    场景：
        前端自动化测试经常需要附加图片或html，在适当的地方，适当的时机截图
    解决：
        @allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果
    步骤：
        在测试报告里附加网页：
            allure.attach(body(内容)，name,attachment_type,extension):
            allure.attach('<head></head><body>首页</body>',"这是错误页的信息"，allure.attachment_type.HTML)
        在测试报告里附加图片：
            allure.attach.file(source,name,attachment_type,extension)
            allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

"""
import pytest
import allure
TEST_CASE_LINK = 'https://www.baidu.com'     # 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.feature("搜索模块")
@allure.title("搜索模块")     # 使allure报告中的behaviors是中文，方便查看
class TestSearch:
    @allure.testcase(TEST_CASE_LINK, "测试链接")
    def test_case1(self):
        print("case1")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_case2(self):
        print("case2")


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("登录模块")
@allure.title("登录模块")
class TestLogin:
    @allure.story("登录成功")
    @allure.title("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("输入用户名和密码")
        print("这里是登录： 测试用例，登录成功")
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("登录失败")
    @allure.title("登录失败")
    def test_login_fail(self):
        print("这是登录： 测试用例，登录失败")
        pass

    @allure.story("用户名缺失")
    @allure.title("用户名缺失")
    def test_login_username_miss(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    @allure.title("密码缺失")
    def test_login_key_miss(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass

    @allure.story("登录失败")
    @allure.title("登录失败")
    def test_login_failure(self):
        print("这是登录： 测试用例，登录失败")
        pass


if __name__ == '__main__':
    pytest.main()
