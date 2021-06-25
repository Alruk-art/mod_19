import sys
sys.path.append("..")
import pytest

from mytestcalc.apptc import Calctor # если папка таже


class TestKalcylat: # слово Test обязательно
    def setup(self):
        self.kalc = Calctor

    def test_multiply_calculate_correctly(self):
        assert self.kalc.multiply(self,2, 3) == 6

    def test_division_calculate_OK(self):
        assert self.kalc.division(self,15, 3) == 5

    def test_subtraction_calculate_YES(self):
        assert self.kalc.subtraction(self,10, 4) == 6

    def test_adding_calculate_NO(self):
        assert self.kalc.adding(self,10, 4) == 11