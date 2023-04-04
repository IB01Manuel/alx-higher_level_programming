#!/usr/bin/python3
"""
This module has one function that adds 2 integers
"""


def add_integer(a, b=98):
    """Return the addition of two integers or floats as integers
    Args:
        a: first argument case
        b: second argument case
    Returns:
        addition of the two arguments
    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
