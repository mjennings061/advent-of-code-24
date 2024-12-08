"""day5.py - Advent of code challenge."""

import re
from pathlib import Path
from typing import List


def printer_sort(input_txt: List[str]) -> int:
    """Sort by rules and get sum of middle pages."""
    # Use regex to get all rules.
    rule_exp = r"\d+\|\d+"
    rules_txt = re.findall(rule_exp, input_txt)
    rules = []
    for rule in rules_txt:
        this_rule = rule.split('|')
        left_rule = int(this_rule[0])
        right_rule = int(this_rule[1])
        rules.append([left_rule, right_rule])

    # Split page updates.
    page_set_exp = r"^\d+,(?:\d+,)+\d+$"
    pages_txt = re.findall(page_set_exp, input_txt, re.MULTILINE)
    pages_set = []
    for set in pages_txt:
        this_set = set.split(',')
        pages = [int(page) for page in this_set]
        pages_set.append(pages)

    # For each page.
    # Determine if any rules exist for that page.
    # If the other page exists in the set, determine page order.
    # Move pages in set.

    # Find relevant rules for the page set.
    for set in pages_set:
        # Find rules pertaining to at least two elements of the pages set.
        for rule in rules:
            # Find if a rule applies.
            n_present = 0
            both_present = False
            for page in set:
                if rule == page:
                    n_present += 1
                if n_present == 2:
                    both_present = True
                    break
                    


if __name__ == "__main__":
    # Input filepath.
    FILENAME = "day5.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Read input file.
    with open(filepath, 'r') as file:
        input_txt = file.read()

    # Sort and sum middle page numbers.
    middle_page_sum = printer_sort(input_txt=input_txt)
    print(middle_page_sum)
