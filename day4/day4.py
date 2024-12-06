"""day4.py - Advent of code day 4."""

import re
import numpy as np
from pathlib import Path
from typing import List


def search_xmas(word_grid: List[str]) -> int:
    """Search for XMAS and count number of occurences.

    Args:
        word_grid (List(str)): Word grid to search.

    Returns:
        count_of_xmas (int): Number of times XMAS appears."""
    # Pattern to search.
    PATTERNS = ["XMAS", "SAMX"]

    # Remove newline.
    word_grid = [line.replace('\n', '') for line in word_grid]

    # The long way, loop through each possible combinations of
    # diagonals looking for the pattern.
    # Create a new word grid for each diagonal.
    max_index = len(word_grid)
    diagnonal_word_pos = []
    for anchor_row in range(max_index):
        this_diagnonal = ""
        col = 0
        for row in range(anchor_row, max_index):
            this_diagnonal += str(word_grid[row][col])
            col += 1
        diagnonal_word_pos.append(this_diagnonal)

    # Do the same for the other half of the grid, column-wise.
    for anchor_col in range(1, max_index):
        this_diagnonal = ""
        row = 0
        for col in range(anchor_col, max_index):
            this_diagnonal += str(word_grid[row][col])
            row += 1
        diagnonal_word_pos.append(this_diagnonal)

    # Repeat for negative diagonals.
    diagnonal_word_neg = []
    for anchor_row in range(max_index):
        this_diagnonal = ""
        col = 0
        for row in range(anchor_row, -1, -1):
            this_diagnonal += str(word_grid[row][col])
            col += 1
        diagnonal_word_neg.append(this_diagnonal)

    # Do the same for the other half of the grid, column-wise.
    for anchor_col in range(1, max_index):
        this_diagnonal = ""
        row = max_index - 1
        for col in range(anchor_col, max_index):
            this_diagnonal += str(word_grid[row][col])
            row -= 1
        diagnonal_word_neg.append(this_diagnonal)

    # Now get verticals.
    vertical_grid = []
    for col in range(max_index):
        this_vertical = ""
        for row in range(max_index):
            this_vertical += str(word_grid[row][col])
        vertical_grid.append(this_vertical)

    # Combine word grids.
    word_grid_all_combos = word_grid + diagnonal_word_pos \
        + diagnonal_word_neg + vertical_grid

    matches = 0
    for pattern in PATTERNS:
        for line in word_grid_all_combos:
            matches += len(re.findall(pattern, line))
    return matches


if __name__ == "__main__":
    # Get data.
    FILENAME = "day4.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Load data from file.
    with open(filepath, 'r') as file:
        file_text = file.readlines()

    # Count number of occurances of XMAS.
    count_of_xmas = search_xmas(file_text)
    print(f"Count of XMAS: {count_of_xmas}")
