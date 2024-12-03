"""day3.py - Day three.
https://adventofcode.com/2024/day/3"""

import re
from pathlib import Path


def multiply_string(string: str) -> int:
    """Main function.

    Args:
        string (str): String to multiply.
    Returns:
        sum_of_multiples (int): Result."""
    # Define regex pattern.
    PATTERN = r"mul\(\d+,\d+\)"

    # Preallocate output.
    sum_of_multiples = None

    # Find all matches.
    multiples = re.findall(
        pattern=PATTERN,
        string=string
    )

    # Loop through matches and multiply.
    sum_of_multiples = 0
    for multiple in multiples:
        # Find each digit.
        digits = re.findall(r"\d+", multiple)
        product = 1
        for digit in digits:
            # Convert to a digit and multiply.
            digit = int(digit)
            product *= digit
        # Get sum of products.
        sum_of_multiples += product
    return sum_of_multiples


if __name__ == "__main__":
    # Get path to input file.
    FILE_NAME = "input.txt"
    this_dir = Path(__file__).parent
    file_path = Path(this_dir, FILE_NAME)

    # Read contents.
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Sum multiples.
    result = multiply_string(file_contents)
    print(result)
