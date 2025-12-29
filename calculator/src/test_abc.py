import pytest
from abcde import Abc
class TestAbc:
    @pytest.fixture
    def calc(self):
        return Calculator()
    @pytest.fixture
    def abc(self):
        return Abc()
    
    def test_p(self,abc):
        assert abc.p() == "abc"
