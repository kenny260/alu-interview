# alu-interview
# Rain Water Retention

## Description
This project solves the rain water retention problem: given a list of non-negative integers representing the heights of walls, calculate how many square units of water will be retained after it rains.

## Problem
Given a cross-section view of walls with unit width 1, determine the total volume of water that can be trapped between the walls after rainfall.

## Algorithm
The solution uses a dynamic programming approach:

1. **Left Max Array**: For each position, calculate the maximum wall height to its left
2. **Right Max Array**: For each position, calculate the maximum wall height to its right
3. **Water Calculation**: For each position, the water level is `min(left_max, right_max) - wall_height`

### Time Complexity
- O(n) where n is the number of walls

### Space Complexity
- O(n) for storing left_max and right_max arrays

## Requirements
- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)
- No external module imports allowed

## Files
- `0-rain.py`: Main solution file containing the `rain()` function
- `README.md`: This file

## Usage
```python
#!/usr/bin/python3
rain = __import__('0-rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
```

## Examples

### Example 1: `[0, 1, 0, 2, 0, 3, 0, 4]`
```
    █
  █ █
█ █ █
█ █ █ █
---------
```
Water retained: 6 square units

### Example 2: `[2, 0, 0, 4, 0, 0, 1, 0]`
```
    █
█   █
█   █   █
█   █   █
---------
```
Water retained: 6 square units

## Author
ALU Interview Project
