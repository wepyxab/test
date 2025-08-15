import pytest
from fule import chekxy

def test_E():
    assert chekxy(['1','100']) == True
    assert chekxy(['5','8']) == True
    assert chekxy(['7','94']) == True

def test_F():
    assert chekxy(['-1','10']) == False
    assert chekxy(['9','0']) == False
    assert chekxy(['9','-1']) == False
    assert chekxy('car') == False