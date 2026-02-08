#!/usr/bin/python3
"""
Module for calculating rainwater retention between walls.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Given a list of non-negative integers representing wall heights,
    this function calculates the total amount of rainwater that can be
    trapped between the walls.

    Args:
        walls (list): A list of non-negative integers representing wall heights

    Returns:
        int: Total amount of rainwater retained in square units

    Algorithm:
        For each position, water can be retained up to the minimum of:
        - The maximum wall height to its left
        - The maximum wall height to its right
        The actual water at that position is this minimum minus the wall height.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    total_water = 0

    # Calculate maximum height to the left of each position
    left_max = [0] * n
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate maximum height to the right of each position
    right_max = [0] * n
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water at each position
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        total_water += max(0, water_level - walls[i])

    return total_water
