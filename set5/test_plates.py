import pytest
from plates import is_valid

def test_numbers():
    assert is_valid('AAAA22') == True
    assert is_valid('AA29AV') == False
    assert is_valid('AAA22') == True
    assert is_valid('AA056') == False
    assert is_valid('AA 22') == False
    assert is_valid('AAm,34') == False