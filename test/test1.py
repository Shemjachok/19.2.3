import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3