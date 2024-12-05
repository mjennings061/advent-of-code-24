"""day1.py - Advent of Code day 1."""

from pathlib import Path
import numpy as np


def pair_and_sort(unsorted: np.array) -> int:
    """Sort lists and calculate sum of differences.

    Args:
        unsorted (np.ndarray): Nx2 array of unsorted pairs.

    Returns:
        sum_of_diff (int): The sum of pair differences."""
    # Sort each column.
    col_0 = np.sort(unsorted[:, 0])
    col_1 = np.sort(unsorted[:, 1])

    # Difference between the two.
    diff = np.abs(col_1 - col_0)

    # Sum.
    sum_of_diff = np.sum(diff)
    return sum_of_diff


def similarity_score(unsorted: np.array) -> int:
    """Count number of times first column value
    appears in second column and sum.

    Args:
        unsorted (np.array): Array to process.

    Returns:
        sum_of_counts (int): Sum of appearences in second column."""
    # Get index and search data columns.
    index = unsorted[:, 0]
    search_data = unsorted[:, 1]

    # Search for each index in search data.
    # Count prevalence and multiply by index.
    # Return sum of prevalence.
    sum_of_counts = 0
    for value in index:
        prevalence = np.sum(search_data == value)
        sum_of_counts += value * prevalence
    return sum_of_counts


if __name__ == "__main__":
    # Input data.
    FILENAME = "day1.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Load file.
    with open(filepath, 'r') as file:
        input_array = np.loadtxt(file, dtype=int)

    # Part one: pair and sort lists.
    result = pair_and_sort(input_array)
    print(f"Sum of differences: {result}")

    # Part two: get similarity score.
    similarity = similarity_score(input_array)
    print(f"Similarity score: {similarity}")
