""""
1、执行javascript脚本
    使用selenium直接在当前页面中进行js交互
    常用的几种操作使用js实现
2、js的处理
   selenium能够执行js，这使得selenium拥有更为强大的能力。既然能执行js,那么js能做的事情，selenium应该大部分也能做。
   直接使用js操作页面，能够解决很多click()不生效的问题。
   页面滚动到底部，顶部
   处理富文本，时间空间的输入
3、selenium中如何调用js
    execute_script:执行js
    return:可以返回js的返回结果
    execute_script: arguments传参
4、js处理-案例1-滑动
    场景：页面显示的数据比较多，需要点击底部的对象，我们就需要把鼠标移动到底部，才可以点击对象
    案例一：滑动到浏览器底部或者顶部
        打开百度首页
        输入搜索关键字
        点击搜索后，跳转到搜索结果也
        滑动到底部点击‘下一页’
5、js处理-案例3-时间控件
    大部分时间控件都是readonly属性，需要手动去选择对应的时间，手动测试中很容易座到，自动化中对空间的操作可以使用js来操作。
    处理时间控件思路：
        要取消日期的readonly属性
        给value赋值
        写js代码来实现如上的1，2点，再webdriver对js进行处理
    测试案例3：
        打开网址https://www.12306.cn/index/
        修改出发日期为2020-12-30
        打印出发日期
        关闭网址
"""
from time import sleep

import pytest

from selenium_execise.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.execute_script("document.getElementById('su').click()")
        # self.driver.find_element_by_id("su").click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(7)
        self.driver.find_element_by_css_selector(".n").click()
        sleep(3)

    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        # self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # # self.driver.execute_script("data.removeAttribute('readonly')")
        # self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(5)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        # print(self.driver.execute_script("return document.getElementById('train_data').value"))
