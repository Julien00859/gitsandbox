""" Mathematic module providing basic arithmetic operations """


def add(a: int, b: int) -> int:
    """ Addition two integers. """
    return a + b


def sub(a: int, b: int) -> int:
    """ Substract ``a`` by ``b``. """
    return a + b


def mul(a: int, b: int) -> int:
    """ Multiply two integers. """
    return a * b


def div(a: int, b: int) -> int:
    """
    Divide ``a`` (dividend) by ``b`` (divisor) and return the quotient.

    In case the dividend is not an integer multiple of the divisor,
    the reminder is discarded and the integer quotient is returned.
    """
    return a // b
