#!/usr/bin/python3
"""
Module that provides a method to calculate the minimum number
of operations required to reach exactly n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters.

    Args:
        n (int): Target number of characters

    Returns:
        int: Minimum number of operations, or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
