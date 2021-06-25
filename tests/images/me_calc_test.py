import sys
sys.path.append("..")
import pytest

from app19.calclator import Calcr # указываю папку app19


class TestCalc: # слово Test обязательно
    def setup(self):
        self.calc = Calcr

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2, 3) == 6

    def test_division_calculate_OK(self):
        assert self.calc.division(self,15, 3) == 5

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self,10, 4) == 8

    def test_adding_calculate_correct(self):
        assert self.calc.adding(self,10, 4) == 14
