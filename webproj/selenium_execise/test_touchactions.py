""""
TouchActions:执行PC端和移动端的点击，滑动，拖拽，多点触控等多种手势操作
类似于ActionChains,ActionChains只是针对PC端程序鼠标模拟的一系列操作，对H5页面操作时无效的，TouchAction可以对h5页面操作，通过TouchAction
可以实现点击、滑动、拖拽、多点触控，以及模拟手势的各种操作
手势控制：
    tap:在指定元素上敲击
    double-tap:在指定元素上双敲击
    tap_and_hold:在指定元素上点击但不释放
    move:手势移动指定偏移（未释放）
    release:释放手势
    scroll:手势点击并滚动
    scroll_from_element:从某个元素位置开始手势点击并滚动（向下滑动为负数，向上滑动为证书）
    long_press:长按元素
    flick:手势滑动
    flick_element:从某个元素位置开始手势滑动（向上滑动为负数，向下滑动为正数）
    perform：执行
TouchAction实例：
打开Chrome
打开URL:http://www.baidu.com
向搜索框中输入‘selenium测试’
通过TouchAction点击搜索框
滑动到底部，点击下一页
关闭Chrome

"""
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)   # 隐式等待（针对所有的操作）
        self.driver.maximize_window()

    def teardown(self):
        pass
        # self.driver.quit()

    def test_touchaction_scrolltobottom(self):
        self.driver.get("http://www.baidu.com")
        search_element = self.driver.find_element_by_id("kw")
        search_element.send_keys("selenium测试")
        baidu_element = self.driver.find_element_by_id("su")
        # baidu_element.click()
        next_page = self.driver.find_element_by_class_name("n")
        action = TouchActions(self.driver)
        action.tap(baidu_element)
        action.scroll_from_element(search_element, 0, 1000)
        action.tap(next_page)
        action.perform()

