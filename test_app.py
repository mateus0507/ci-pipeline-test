from app import soma

def test_soma_basica():
    assert soma(1, 2) == 3

def test_soma_negativos():
    assert soma(-1, -2) == -3