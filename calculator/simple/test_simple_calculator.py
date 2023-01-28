from .simple_calculator import SimpleCalculator


def test_add():
    assert SimpleCalculator.add(1, 2) == 3.0

def test_subtract():
    assert SimpleCalculator.subtract(1, 2) == -1.0
