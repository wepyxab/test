import pytest
from bank import greet_message

def test_bank():
    assert greet_message('heLLo') == '$0'
    assert greet_message('hI herry') == '$20'
    assert greet_message('lalSLSLL') == '$10'