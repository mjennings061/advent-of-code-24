"""day6.py - Advent of code challenge."""

import copy
import multiprocessing
from pathlib import Path
from typing import List


def is_on_grid(row: int, col: int, size: int) -> bool:
    """Determine if the cursor is on grid."""
    # Preallocate output.
    is_on_grid = True

    # Check if we are above or left of the grid.
    if row < 0 or col < 0:
        is_on_grid = False

    # Check if we are right or below the grid.
    if row >= size or col >= size:
        is_on_grid = False
    return is_on_grid


def play_game(grid: List[str]) -> int:
    """Count the number of squares touched."""
    # Constants.
    DIRECTIONS = {
        '^': (-1, 0),   # Move up a row (row-1, col)
        '>': (0, 1),    # Move right (row, col+1)
        'v': (1, 0),    # Move down a row (row+1, col)
        '<': (0, -1),   # Move left (row, col-1)
    }
    MAX_MOVEMENTS = 1e6

    # Get current position.
    cursor = '^'
    for pos_row, row in enumerate(grid):
        if not isinstance(row, str):
            row = "".join(row)
            grid[pos_row] = row
        if cursor in row:
            pos_col = row.index('^')
            break

    # Grids touched.
    grid_size = len(grid)
    n_movements = n_grids = 0
    game_grid = grid
    while is_on_grid(pos_row, pos_col, grid_size):
        # Move cursor until we are off the grid.
        delta_row, delta_col = DIRECTIONS[cursor]
        next_row = pos_row + delta_row
        next_col = pos_col + delta_col

        # Get the next symbol.
        if is_on_grid(next_row, next_col, grid_size):
            # Get the next valid symbol.
            next_symbol = game_grid[next_row][next_col]
        else:
            # Next symbol is off grid, so mark it as '.' for now.
            next_symbol = '.'

        # Check for an obstacle.
        if next_symbol == '#':
            # Rotate 90 degrees.
            cursor_idx = list(DIRECTIONS.keys()).index(cursor) + 1
            if cursor_idx >= len(DIRECTIONS):
                cursor_idx = 0
            cursor = list(DIRECTIONS.keys())[cursor_idx]
            continue

        # Mark current position.
        if game_grid[pos_row][pos_col] != 'x':
            # Convert to list since strings are immutable.
            row = list(game_grid[pos_row])
            row[pos_col] = 'x'
            game_grid[pos_row] = row
            n_grids += 1

        # Move forward.
        pos_row = next_row
        pos_col = next_col
        n_movements += 1

        if n_movements > MAX_MOVEMENTS:
            raise ZeroDivisionError("Infinite loop found")
    return n_grids


def check_for_loop(updated_grid: List[str]) -> int:
    """Helper function to check for infinite loop."""
    try:
        play_game(updated_grid.copy())
        return 0
    except ZeroDivisionError:
        return 1


def find_infinite_loops(grid_to_search: List[str]) -> int:
    """Find how many infinite loops are possible using multiprocessing."""
    # This is going to be a brute-force option, soz.
    # Move the obstacle position and run.
    n_infinite_loops = 0
    tasks = []
    for i_row, row in enumerate(grid_to_search):
        # Check an obstacle is not already there.
        for i_col, object in enumerate(row):
            # Do not run for an existing obstacle.
            if object != '.':
                continue
            else:
                # Update the grid.
                updated_grid = grid_to_search.copy()
                new_row = list(row)
                new_row[i_col] = '#'
                updated_grid[i_row] = "".join(new_row)
                tasks.append(updated_grid)

    # Use multiprocessing to check for loops.
    with multiprocessing.Pool() as pool:
        results = pool.map(check_for_loop, tasks)
        n_infinite_loops = sum(results)

    return n_infinite_loops


if __name__ == "__main__":
    # Input filepath.
    FILENAME = "day6.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Read input file.
    with open(filepath, 'r') as file:
        input_txt = file.readlines()

    # Remove newlines.
    input_grid = [line.replace('\n', '') for line in input_txt]

    # Play the game.
    n_squares_touched = play_game(copy.deepcopy(input_grid))
    print(f"Number of grids touched: {n_squares_touched}")

    # Find number of infinite loops possible.
    n_loops = find_infinite_loops(copy.deepcopy(input_grid))
    print(f"Number of infinite loops: {n_loops}")
