""""
表单定义：
1、什么是表单：
    表单时一种包含表单元素的区域。
    表单元素是允许用户在表单中（比如：文本域、下拉列别、单选框、复选框等等）输入信息的元素
    表单使用表单标签（<form>）定义。例如：<form><input/></form>
2、操作表单元素步骤：
    首先要定位到表单元素。
    然后去操作元素（清空，输入或点击等）



"""
import time

from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        pass
        # self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("username")
        self.driver.find_element_by_id("user_password").send_keys("password")
        print(self.driver.find_element_by_id("user_remember_me").get_attribute("id"))   # 应该是记住密码操作，但是无法定位到
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
