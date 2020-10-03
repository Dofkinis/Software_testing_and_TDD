from functions.calculator_class import Calculator
import pytest

# pytest constant decorator
@pytest.fixture()
def answer():
    return 2

calc1 = Calculator()


def test_add():
    assert calc1.add(1, 2) == 3


def test_subtract(answer):
    assert calc1.subtract(3, 1) == answer


def test_multiply():
    assert calc1.multiply(2, 2) == 4


def test_divide(answer):
    assert calc1.divide(4, 2) == answer


def test_power():
    assert calc1.power(2, 2) == 4

def test_divide_raise_exception():
    with pytest.raises(Exception):
        assert calc1.divide(2, 0)
