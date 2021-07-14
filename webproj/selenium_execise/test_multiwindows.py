"""
1、selenium里面如何处理多窗口场景
    多个窗口识别
    多个窗口之间切换
2、多窗口处理
    点击某些连接，会重新打开一个窗口，对于这种情况，想在新页面上操作，就得切换窗口了。
    获取窗口得唯一标识用句柄表示，所以只需要切换句柄，就可以在多个页面灵活操作了。
3、多窗口处理流程
    先获取到当前得窗口句柄（driver.current_window_handle）
    再获取到所有得窗口句柄（driver.window_handles）
    判断是否是想要操作得窗口，如果是，就可以对窗口进行操作，如果不是，跳转到另外一个窗口，对另一个窗口进行操作（driver.switch_to_window）
4、多窗口切换案例
    打开百度页面
    点击登录
    弹框中点击‘立即注册’，输入用户名和账号
    返回刚才得登录页，点击登录
    输入用户名和密码
    点击登录
"""
from time import sleep

from selenium_execise.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[3]/a').click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])    # 句柄以列表得形式存储
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("telphonenumber")
        sleep(3)
        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        sleep(2)
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("17826829606")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("120811dongjian")
        sleep(1)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(5)
