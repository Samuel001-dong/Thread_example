""""
ActionChains:执行PC端的鼠标点击、双击、右键、拖拽等事件
1、执行原理：
    调用ActionChains的方法时，不会立即执行，而是将所有的操作，按顺序存放在一个队列里，当你调用perform()方法时，队列中的事件会依次执行
2、基本用法：
    生成一个动作action=ActionChains(driver)
    动作添加方法1 action.方法1
    动作添加方法2 action.方法2
    调用perform()方法执行（action.perform()）
3、具体写法
    链式写法：
        ActionChains(driver).move_to_element(element).click(element).perform
    分布写法：
        actions = ActonChains(driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

"""
测试案例一(用法1：点击、双击、右击操作)：
打开页面（http://sahitest.com/demo/clicks.htm）
分别对按钮 'click me','dbl click me','right click me',执行点击，双击，右击操作
打印上面展示框中的内容
实现代码：
    action = ActionChains(self.driver)
    action.click(element)
    action.double_click(element)
    action.context_click(element)
    action.perform()
测试案例二（用法2：鼠标移动到某个元素上）
实现代码：
action = ActionChains(self.driver)
action.move_to_element(element)
action.perform()
测试案例三（用法3：拖放）
实现代码：
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element1 = self.driver.find_element_by_class_name("item")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element,drop_element1)
        action.perform()
测试案例四（用法4：模拟按键用法）
模拟按键有多种方法，能用win32api来实现，能用SendKeys来实现，也可以用selenium的WebElenment对象的send_keys()方法来实现，这里ActionChains类也提供了几种模拟按键的方法。
用法：
action = ActionChains(driver)
action.send_keys(Keys.BACK_SPACE)
或者action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
action.perform()
实现代码：
打开网址：http://sahitest.com/demo/label.htm
定位两个输入框e1,e2
像输入框e1中输入文字 'username'
使用全选，复制，粘贴到输入框e2

"""


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://sahitest.com/demo/clicks.htm")

    def teardown(self):
        pass
        # self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        action = ActionChains(self.driver)
        click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        db_click = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        right_click = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action.click(click)
        action.double_click(db_click)
        action.context_click(right_click)
        action.perform()

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_id("s-usersetting-top"))
        action.perform()

    @pytest.mark.skip
    def test_draganddrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element1 = self.driver.find_element_by_class_name("item")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element1)
        action.perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element_text1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        element_text2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        action = ActionChains(self.driver)
        action.click(element_text1)
        action.send_keys("username").pause(1)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
        action.click(element_text2)
        action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
        time.sleep(3)
        action.perform()

