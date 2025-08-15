import pytest
from twttr import shorten

def test_up():
    assert shorten('AEZA') == 'Z'
    assert shorten('VPN') == 'VPN'
    assert shorten('TWITTER') == 'TWTTR'

def test_down():
    assert shorten('werenax') == 'wrnx'
    assert shorten('noba') == 'nb'

def test_special_simbols():
    assert shorten('568') == '568'
    assert shorten('/.,?!') == '/.,?!'

