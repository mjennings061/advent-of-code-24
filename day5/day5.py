"""day5.py - Advent of code challenge."""

import re
from pathlib import Path
from typing import List
from math import floor


def out_of_order(sorted_list, rules) -> bool:
    """Check if the list is out of order."""
    # Sanity check.
    for rule in rules:
        # Get the indices where the rule appears.
        left_index = sorted_list.index(rule[0])
        right_index = sorted_list.index(rule[1])
        if left_index > right_index:
            return True
    return False


def printer_sort(input_txt: List[str], reorder: bool = False) -> int:
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

    # For each set of pages.
    # Determine if any rules exist for that page.
    # Figure if its out of order based on the rules.
    # Swap out of order indices.

    # Find relevant rules for the page set.
    reordered_sets = []
    for set in pages_set:
        # Find rules pertaining to at least two elements of the pages set.
        rules_to_apply = []
        for rule in rules:
            # Find if a rule applies.
            n_present = 0
            for page in set:
                if page in rule:
                    n_present += 1
                if n_present == 2:
                    rules_to_apply.append(rule)
                    break

        is_out_of_order = out_of_order(set, rules_to_apply)
        if reorder is False and is_out_of_order:
            # Do not process this set of page numbers.
            continue

        if reorder and not is_out_of_order:
            # Order is correct but reorder requested, skip.
            continue

        reordered_set = set
        while out_of_order(reordered_set, rules_to_apply):
            for rule in rules_to_apply:
                # Get the indices where the rule appears.
                left_index = reordered_set.index(rule[0])
                right_index = reordered_set.index(rule[1])
                if left_index > right_index:
                    # Swap page positions.
                    reordered_set[left_index] = rule[1]
                    reordered_set[right_index] = rule[0]

        # Sanity check.
        if out_of_order(reordered_set, rules_to_apply):
            raise ValueError("FFS: Something funky happening here.")
        reordered_sets.append(reordered_set)

    # Calculate sum of middle pages.
    sum_of_pages = 0
    for set in reordered_sets:
        # Get the middle page.
        i_middle = floor(len(set) / 2)
        sum_of_pages += set[i_middle]
    return sum_of_pages


if __name__ == "__main__":
    # Input filepath.
    FILENAME = "day5.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Read input file.
    with open(filepath, 'r') as file:
        input_txt = file.read()

    # Part one: Sum correctly ordered middle page numbers.
    middle_page_sum = printer_sort(input_txt=input_txt)
    print(f"Sum of correct page sets: {middle_page_sum}")

    # Part two: Sum reordered middle page numbers.
    middle_page_sum = printer_sort(input_txt=input_txt, reorder=True)
    print(f"Sum of reordered middle pages: {middle_page_sum}")
