""""
1、selenium里面如何处理frame:
    多个frame识别
    多个frame之间切换
2、frame介绍
在web自动化中，如果一个元素定位不到，那么很大可能是在iframe中。
什么是frame?
    frame是html中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页面。
    基于html的框架，又分为垂直框架和水平框架（cols,rows）
3、frame分类
    frame标签包含frameset、frame、iframe三种。
    frameset和普通的标签一样，不会影响正常的定位，可以使用index、id、name、webelement任意方式定位frame.
    而frame与iframe定位而言是一样的。selenium有一组方法对frame进行操作。
演示：https://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols
4、多frame切换：
    frame存在两种：
        一种是嵌套的，一种是未嵌套的
    切换frame：
    driver.switch_to.frame()   # 根据元素id或者index切换frame
    driver.switch_to.default_content()    # 切换到默认frame
    driver.switch_to.parent_frame()       # 切换到父级frame
5、frame未嵌套
    处理未嵌套的iframe
        driver.switch_to_frame("frame的id")
        driver.switch_to_frame("frame-index") frame无ID的时候依据索引来处理，索引从0开始driver.switch_to_frame(0)
6、frame嵌套
    处理嵌套的iframe
    对于嵌套的先进入到iframe的父节点，再进入到子节点，然后可以对子节点里面的对象进行处理和操作。
    driver.switch_to.frame("父节点")
    driver.switch_to.frame("子节点")
7、多frame切换案例
    打开包含frame的web页面：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    打印‘请拖拽我’元素的文本
    打印‘点击运行’元素的文本

"""
from time import sleep

from selenium_execise.base import Base
from selenium import webdriver


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_xpath('//*[@id="draggable"]').text)
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)

