""""
数据驱动：
    简介：
        1、数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变
        。简单来说，就是参数化的应用。数据量小的测试用例可以使用代码的参数化来来实现
        数据驱动，数据量大的情况下建议大家使用一种结构化的文件（例如yaml，json等）
        来对数据进行存储，然后在测试用例中读取这些数据。
    应用场景：
        1、App、Web、接口自动化测试
            测试步骤的数据驱动
            测试数据的数据驱动
            配置的数据驱动

"""
import pytest
import yaml


class TestDataDrive:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./dataenv.yml")))  # 出入数据必须是列表形式
    def test_demo1(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是：", env["test"])
        if "dev" in env:
            print("这是开发环境")
            print(f"开发环境的ip是：{env['dev']}")

    def test_demo2(self):
        print(yaml.safe_load(open("./dataenv.yml")))
