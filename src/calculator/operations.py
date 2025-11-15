from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Adds two Decimal numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtracts the second Decimal number from the first.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference between a and b.
    """
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiplies two Decimal numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divides the first Decimal number by the second.

    Args:
        a: The first number (dividend).
        b: The second number (divisor).

    Returns:
        The quotient of a and b.

    Raises:
        ZeroDivisionError: If the divisor b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
