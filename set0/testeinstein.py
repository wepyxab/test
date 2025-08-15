from einstein import einstein
import pytest

def test_positive():
    assert einstein(1) == 'E: 90000000000000000'
    assert einstein(14) == 'E: 1260000000000000000'
    assert einstein(50) == 'E: 4500000000000000000'


