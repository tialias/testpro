import pytest

from python.python import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()

    @pytest.mark.usefixtures("myfixture")
    def test_add(self):
        # print("执行test_add")
        result = self.calc.add(1, 2)
        assert result == 3

    def test_sub(self, myfixture):
        # print("执行test_add")
        result = self.calc.sub(2, 1)
        assert result == 1

    def test_mult(self, myfixture):
        # print("执行test_mult")
        result = self.calc.mult(1, 2)
        assert result == 2

    def test_div(self, myfixture):
        # print("执行test_div")
        result = self.calc.div(2, 1)
        assert result == 2


pytest.main(['-rvsq', 'test_pytest.py::TestCalc'])
