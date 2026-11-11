"""
sudoku solver
solves any valid 9x9 sudoku with backtracking

the board is a list of 9 rows, each row is a list of 9 numbers
empty cells are 0
"""

import sys


def read_puzzle(text):
    """takes 81 characters (digits, 0 or . for blanks) and turns them into a 9x9 grid"""
    chars = [c for c in text if c.isdigit() or c == "."]
    if len(chars) != 81:
        raise ValueError(f"Puzzle must have 81 cells, got {len(chars)}")
    numbers = [0 if c == "." else int(c) for c in chars]
    return [numbers[row * 9:(row + 1) * 9] for row in range(9)]


def is_valid_move(grid, row, col, num):
    """checks if num can go at (row, col) without breaking any rules"""
    # can't already be in the same row
    if num in grid[row]:
        return False

    # can't already be in the same column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # can't already be in the same 3x3 box
    box_row = (row // 3) * 3   # top left corner of the box
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False

    return True


def find_empty_cell(grid):
    """gives back (row, col) of the first empty cell, or None if the board is full"""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid_puzzle(grid):
    """makes sure the starting puzzle doesn't already break the rules"""
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num != 0:
                grid[row][col] = 0          # take it out for a sec
                ok = is_valid_move(grid, row, col, num)
                grid[row][col] = num        # put it back
                if not ok:
                    return False
    return True


def solve(grid):
    """
    solves the board in place with backtracking
    returns True if it worked, False if there's no solution

    how it works:
      1. find an empty cell
      2. try 1 to 9 in it
      3. if a number is allowed, put it in and try to solve the rest
      4. if that hits a dead end, erase it (backtrack) and try the next number
      5. if nothing works, go back to the cell before
    """
    empty = find_empty_cell(grid)
    if empty is None:
        return True  # no empty cells left so we're done

    row, col = empty
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0  # dead end, undo and try the next one

    return False


def print_grid(grid):
    """prints the board with lines between the 3x3 boxes"""
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("------+-------+------")
        line = ""
        for col in range(9):
            if col % 3 == 0 and col != 0:
                line += "| "
            line += (str(grid[row][col]) if grid[row][col] != 0 else ".") + " "
        print(line.rstrip())


def main():
    if len(sys.argv) != 2:
        print("Usage: python sudoku.py <puzzle_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        grid = read_puzzle(f.read())

    print("Puzzle:")
    print_grid(grid)
    print()

    if not is_valid_puzzle(grid):
        print("This puzzle breaks Sudoku rules, so it can't be solved.")
    elif solve(grid):
        print("Solved:")
        print_grid(grid)
    else:
        print("No solution exists for this puzzle.")


if __name__ == "__main__":
    main()
