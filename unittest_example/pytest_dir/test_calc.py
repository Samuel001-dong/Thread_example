""""


"""
import pytest
# 导入被测代码
import yaml

from calculator import CalculatorExercise


# 测试代码
class TestCalc:
    with open("./calc_data.yml") as f:
        DATA = yaml.safe_load(f)

    def setup_class(self):
        print("类级别：setup_class")
        calc = CalculatorExercise()

    def teardown_class(self):
        print("类级别：teardown_class")

    def setup(self):
        self.calc = CalculatorExercise()
        print("方法级别：“setup”")

    @pytest.mark.parametrize("a, b, except1", DATA["add_int"]["data"])
    def test_add_int(self, a, b, except1):
        assert self.calc.calc_add(a, b) == except1

    @pytest.mark.parametrize("a, b, except1", DATA["add_float"]["data"], ids=DATA["add_float"]["ids"])   # 数据驱动示例
    def test_add_float(self, a, b, except1):
        assert round(self.calc.calc_add(a, b), 3) == except1

    @pytest.mark.parametrize("a, b, except1", [(1, 2, 0.5), (40, 5, 8)])
    def test_div(self, a, b, except1):
        assert self.calc.calc_div(a, b) == except1

    @pytest.mark.parametrize("a, b, except1", [(1, 0, 0.5)])
    def test_div_zero(self, a, b, except1):
        with pytest.raises(ZeroDivisionError):      # 抛出异常，认为此异常为正常现象
            assert self.calc.calc_div(a, b) == except1

    @pytest.mark.parametrize("a, b, except1", [(1, 2, -1), (40, 5, 35)])
    def test_sub(self, a, b, except1):
        assert self.calc.calc_sub(a, b) == except1


