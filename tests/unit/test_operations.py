from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(Decimal('10'), Decimal('5')) == Decimal('15')
    assert add(Decimal('-1'), Decimal('1')) == Decimal('0')
    assert add(Decimal('-1'), Decimal('-1')) == Decimal('-2')

def test_subtract():
    assert subtract(Decimal('10'), Decimal('5')) == Decimal('5')
    assert subtract(Decimal('5'), Decimal('10')) == Decimal('-5')
    assert subtract(Decimal('-1'), Decimal('-1')) == Decimal('0')
    assert subtract(Decimal('0'), Decimal('5')) == Decimal('-5')

def test_multiply():
    assert multiply(Decimal('10'), Decimal('5')) == Decimal('50')
    assert multiply(Decimal('-1'), Decimal('5')) == Decimal('-5')
    assert multiply(Decimal('-1'), Decimal('-1')) == Decimal('1')
    assert multiply(Decimal('0'), Decimal('5')) == Decimal('0')

def test_divide():
    assert divide(Decimal('10'), Decimal('5')) == Decimal('2')
    assert divide(Decimal('-10'), Decimal('5')) == Decimal('-2')
    assert divide(Decimal('10'), Decimal('-5')) == Decimal('-2')
    assert divide(Decimal('-10'), Decimal('-5')) == Decimal('2')
    assert divide(Decimal('0'), Decimal('5')) == Decimal('0')

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(Decimal('10'), Decimal('0'))

