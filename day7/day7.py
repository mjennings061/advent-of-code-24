"""day7.py - Advent of code challenge."""

import re
import itertools as it
from pathlib import Path
from typing import List


def generate_operator_combos(n_ops: int) -> List[str]:
    """Generate a list of all possible combinations.

    Args:
        n_ops (int): Number of operators.

    Returns:
        all_combos (List[str]): All combinations of operators."""
    operators = ['+', '*']
    all_combos = [
        combo for combo in it.product(operators, repeat=n_ops)
    ]
    return all_combos


def perform_operation(terms_in: List[int], ops: List[str]) -> int:
    """Perform calculation of terms based on operations.

    Args:
        terms_in (List[int]): List of terms to be operated.
        ops (List[str]): List of operations.

    Returns:
        result (int): Result."""
    # For each operator pair.
    terms = terms_in.copy()
    result = 0
    for op in ops:
        # Check for two terms.
        if len(terms) < 2:
            break

        # Calculate result.
        if op == '+':
            this_op = terms[0] + terms[1]
        else:
            this_op = terms[0] * terms[1]

        # Make the first element of terms the result.
        terms[0] = this_op

        # Remove the second term, since its no longer needed.
        terms.pop(1)
        result += this_op
    return result


def is_valid_test(test: int, terms_in: List[int]) -> bool:
    """Check if test is valid.

    Args:
        test (int): The expected output value.

    Returns:
        terms_in (List[int]): A list of terms to add or multiply."""
    # Count number of operators.
    n_ops = len(terms_in) - 1
    operator_combos = generate_operator_combos(n_ops=n_ops)

    for operators in operator_combos:
        # Calculate result of operations.
        result = perform_operation(terms_in=terms_in, ops=operators)
        if result == test:
            return True

    # Default.
    return False


def sum_of_valid_tests(test_list: List[str]) -> int:
    """Get the sum of all valid instructions.

    Args:
        test_list (List[str]): List of instructions.

    Returns:
        sum_of_tests (int): Sum of valid instructions."""
    # Get tests and terms.
    tests_str = re.findall(r"^\d+", test_list, re.MULTILINE)
    terms_str = re.findall(r": (\d+(?: \d+)*)", test_list, re.MULTILINE)

    sum_of_tests = 0
    for test_str, term_str in zip(tests_str, terms_str):
        # Extract test and terms.
        test = int(test_str)
        terms = [int(term) for term in term_str.split(" ")]

        # Check if terms can be multiplied or added to get test value.
        valid = is_valid_test(test=test, terms_in=terms)

        # Sum valid test.
        if valid:
            sum_of_tests += test
    return sum_of_tests


if __name__ == "__main__":
    # Get data path.
    FILENAME = "day7.txt"
    this_dir = Path(__file__).parent
    data_path = Path(this_dir, FILENAME)

    # Load data.
    with open(data_path, 'r') as file:
        data = file.read()

    # Get sum of valid tests.
    sum = sum_of_valid_tests(test_list=data)
    print(f"Sum of valid tests: {sum}")
