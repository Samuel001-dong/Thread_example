"""
setup&teardown方法



"""
import os

from selenium import webdriver


class Base:
    def setup(self):
        # brower = os.getenv("brower")       # 多浏览器兼容性测试
        # if brower == 'firefox':
        #     self.driver = webdriver.Firefox()
        # elif brower == 'chrome':
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        # pass
        self.driver.quit()
