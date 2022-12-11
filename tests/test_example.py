import src.functions


def test_func():
    x,y = functions.generatexy()
    assert x[0]==1
