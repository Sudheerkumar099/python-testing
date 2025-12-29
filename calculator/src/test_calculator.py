import pytest
from calculator import Calculator
from abcde import Abc
class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    @pytest.fixture
    def abc(self):
        return Abc()
    @pytest.mark.slow
    def test_add(self,calc):
        assert calc.add(1,2)==3

    @pytest.mark.regression
    def test_divde(self,calc):
        assert calc.divide(2,2)==1

    @pytest.mark.ab
    @pytest.mark.filterwarnings("ignore:DeprecationWarning")
    def test_p(self,abc):
        assert abc.p() == "abc"

    @pytest.mark.skip
    def test_div(self,calc):
        with pytest.raises(ZeroDivisionError, match="Cannot divide with zero"):
            calc.divide(2,0)

    @pytest.mark.parametrize("a,b,expected",[(1,2,3),(5,5,10),(2,2,4),])
    def test_add_paramaterized(self,calc,a,b,expected):
        assert calc.add(a,b) == expected
    