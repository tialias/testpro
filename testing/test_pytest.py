import pytest

from testing.python import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(1, 2)
        assert result == 3

    def test_sub(self):
        result = self.calc.sub(2, 1)
        assert result == 1

    def test_mult(self):
        result = self.calc.mult(1, 2)
        assert result == 2

    def test_div(self):
        result = self.calc.div(2, 1)
        assert result == 2


pytest.main(['-vs', 'test_pytest.py::TestCalc'])
