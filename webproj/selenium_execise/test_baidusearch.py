""""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearchBaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        pass
        # self.driver.quit()

    def test_search(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹学院")
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
