import src.data_generator as data_generator


def test_func():
    x,y = data_generator.generatexy()
    assert x[0]==1
