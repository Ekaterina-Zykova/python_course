import pytest

from homework9.task02.task02 import Suppressor, suppressor


def test_suppressor_as_class():
    with Suppressor(IndexError):
        assert [0][1]
    with Suppressor(ValueError):
        assert int("string")
    with Suppressor(ZeroDivisionError):
        assert 1 / 0
    with Suppressor(ArithmeticError, AttributeError):
        assert 1 / 0
    with pytest.raises(ZeroDivisionError):
        with Suppressor(IndexError):
            assert 1 / 0


def test_suppressor_as_generator():
    with suppressor(IndexError):
        assert [0][1]
    with suppressor(ValueError):
        assert int("string")
    with suppressor(ZeroDivisionError):
        assert 1 / 0
    with suppressor(ArithmeticError, AttributeError):
        assert 1 / 0
    with pytest.raises(ZeroDivisionError):
        with suppressor(IndexError):
            assert 1 / 0
