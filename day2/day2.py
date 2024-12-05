"""day2.py - Day two of the advent of code challenge."""

import numpy as np
from typing import List
from pathlib import Path


def count_safe_floors(floors: List[int]) -> int:
    """Count the number of safe floors in a an array.

    Args:
        floors (np.array): Array NxM where N is the number of reports
            and M is the floor numbers.

    Returns:
        safe_floors (int): Number of safe floors.

    Examples:
    >>> count_safe_floors(np.array([1, 2, 3, 4]))
    1
    >>> count_safe_floors(np.array([[1, 2], [3, 4]]))
    2
    """
    # Constants.
    MAX_FLOOR_JUMP = 3

    safe_floors = 0
    for floor in floors:
        # Calculate the difference between each element.
        diff = np.diff(np.array(floor, dtype=int))
        # Check all are either increasing or decreasing.
        is_unidirectional = np.all(diff > 0) or np.all(diff < 0)
        # If any elements are greater than the max, floor is unsafe.
        is_safe_jump = np.all(np.abs(diff) <= MAX_FLOOR_JUMP)

        if is_unidirectional and is_safe_jump:
            # Increment safe floors.
            safe_floors += 1
    return safe_floors


if __name__ == "__main__":
    # Input data.
    FILENAME = "day2.txt"
    this_dir = Path(__file__).parent
    input_file = Path(this_dir, FILENAME)

    # Get data.
    with open(input_file, 'r') as file:
        input_data = [x.split() for x in file.readlines()]

    safe_floors = count_safe_floors(input_data)
    print(f"Number of safe floors: {safe_floors}")
