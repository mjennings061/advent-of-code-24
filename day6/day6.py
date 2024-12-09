"""day6.py - Advent of code challenge."""

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

    # Remove newlines.
    grid = [line.replace('\n', '') for line in grid]
    grid_size = len(grid)

    # Get current position.
    cursor = '^'
    for pos_row, row in enumerate(grid):
        if cursor in row:
            pos_col = row.index('^')
            break

    # Grids touched.
    n_movements = 0
    while is_on_grid(pos_row, pos_col, grid_size):
        # Move cursor until we are off the grid.
        delta_row, delta_col = DIRECTIONS[cursor]
        next_row = pos_row + delta_row
        next_col = pos_col + delta_col

        # Get the next symbol.
        if is_on_grid(next_row, next_col, grid_size):
            # Get the next valid symbol.
            next_symbol = grid[next_row][next_col]
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
        if grid[pos_row][pos_col] != 'x':
            # Convert to list since strings are immutable.
            row = list(grid[pos_row])
            row[pos_col] = 'x'
            grid[pos_row] = row
            n_movements += 1

        # Move forward.
        pos_row = next_row
        pos_col = next_col
    return n_movements


if __name__ == "__main__":
    # Input filepath.
    FILENAME = "day6.txt"
    this_dir = Path(__file__).parent
    filepath = Path(this_dir, FILENAME)

    # Read input file.
    with open(filepath, 'r') as file:
        input_txt = file.readlines()

    # Play the game.
    n_squares_touched = play_game(grid=input_txt)
    print(f"Number of grids touched: {n_squares_touched}")
