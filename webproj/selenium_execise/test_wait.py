""""
一、等待的三种方式
1、直接等待：强制等待，线程休眠一定时间
    time.sleep(3)      #等待3秒
2、显式等待：
    在代码中定义等待条件，当条件发生时才继续执行代码。
    WebDriverWait配合until()和until_not()方法，根据判断条件进行等待
    程序每隔一段时间（默认0.5秒）进行条件判断，如果条件成立，则执行下一步，否则继续等待，直到超过设置的最长时间
3、隐式等待（全局）：设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没出现就抛出异常
    self.driver.implicitly_wait(3)
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ceshiren.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)    # 隐式等待：动态等待5秒，5秒之后仍然无法找到元素（所有的元素都会有此操作）则抛出异常

    def teardown(self):
        pass
        # self.driver.quit()     # 关闭浏览器，进行资源回收

    def test_wait(self):
        # sleep(3)  # 直接等待
        self.driver.find_element(By.XPATH, '//*[@title="原创精华文章,有100元奖金"]').click()
        # sleep(3)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()
        # sleep(3)

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="default"]')) >= 1
        #
        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@href="/t/topic/13358"]')))
        self.driver.find_element(By.XPATH, '//*[@href="/t/topic/13358"]').click()
        sleep(3)
        print("hello")
