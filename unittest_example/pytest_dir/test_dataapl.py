""""
1、参数化使用(数据驱动基础)：
    @pytest.mark.parametrize(argnames,argvalues)
    argnames:要参数化的变量，string(逗号分隔)，list,tuple
    argvalues:参数化的值，list,list[tuple]
2、列表里面的值可以修改，tuple（元组）里面的值不可修改
3、yaml:
    数据：list、dict
    可以进行嵌套
"""
import pytest
import yaml


@pytest.mark.parametrize(('a', 'b'), [
    (11, 2),
    (22, 33)
    ])
def test_param(a, b):
    print(a+b)


class TestData:
    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./pytest_data.yml")))
    def test_func1(self, a, b):
        print(a + b)
