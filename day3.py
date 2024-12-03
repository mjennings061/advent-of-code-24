"""day3.py - Day three.
https://adventofcode.com/2024/day/3"""

import re


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
    DEFAULT_STING = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)"
        "+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    result = multiply_string(DEFAULT_STING)
    print(result)
