""""


"""
# 被测代码
import pytest


# 测试代码
from pytest_dir.calculator import CalculatorExercise


class TestCalc:
    def setup_class(self):
        print("类级别：setup_class")
        calc = CalculatorExercise()

    def teardown_class(self):
        print("类级别：teardown_class")

    def setup(self):
        self.calc = CalculatorExercise()
        print("方法级别：“setup”")

    @pytest.mark.parametrize("a, b, except1", [(1, 2, 3), (4, 5, 9)])
    def test_add_int(self, a, b, except1):
        assert self.calc.calc_add(a, b) == except1

    @pytest.mark.parametrize("a, b, except1", [(0.1, 0.2, 0.3), (0.4, 0.5, 0.9)])
    def test_add_float(self, a, b, except1):
        assert round(self.calc.calc_add(a, b), 3) == except1

    @pytest.mark.parametrize("a, b, except1", [(1, 2, 0.5), (40, 5, 8)])
    def test_div(self, a, b, except1):
        assert self.calc.calc_div(a, b) == except1

    @pytest.mark.parametrize("a, b, except1", [(1, 2, -1), (40, 5, 35)])
    def test_sub(self, a, b, except1):
        assert self.calc.calc_sub(a, b) == except1


