import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from sudoku import read_puzzle, is_valid_move, is_valid_puzzle, solve

EASY = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"


def is_solved_correctly(grid):
    """every row, column and 3x3 box needs 1 to 9 exactly once"""
    full = set(range(1, 10))
    for i in range(9):
        if set(grid[i]) != full:
            return False
        if set(grid[r][i] for r in range(9)) != full:
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = {grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)}
            if box != full:
                return False
    return True


def test_read_puzzle_makes_9x9_grid():
    grid = read_puzzle(EASY)
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)
    assert grid[0][0] == 5


def test_read_puzzle_rejects_wrong_length():
    try:
        read_puzzle("123")
        assert False, "should have raised ValueError"
    except ValueError:
        pass


def test_rejects_number_already_in_row():
    grid = read_puzzle(EASY)
    assert not is_valid_move(grid, 0, 2, 5)  # 5 is already in row 0


def test_rejects_number_already_in_column():
    grid = read_puzzle(EASY)
    assert not is_valid_move(grid, 2, 0, 8)  # 8 is already in column 0


def test_rejects_number_already_in_box():
    grid = read_puzzle(EASY)
    assert not is_valid_move(grid, 1, 1, 9)  # 9 is already in the top-left box


def test_solves_easy_puzzle():
    grid = read_puzzle(EASY)
    assert solve(grid)
    assert is_solved_correctly(grid)


def test_solve_keeps_original_clues():
    original = read_puzzle(EASY)
    grid = read_puzzle(EASY)
    solve(grid)
    for r in range(9):
        for c in range(9):
            if original[r][c] != 0:
                assert grid[r][c] == original[r][c]


def test_detects_invalid_puzzle():
    bad = "55" + "0" * 79  # two 5s in the same row
    assert not is_valid_puzzle(read_puzzle(bad))


def test_unsolvable_puzzle_returns_false():
    # looks fine at first but cell (0,8) has no number that works
    text = "12345678.000000009" + "0" * 63
    grid = read_puzzle(text)
    assert is_valid_puzzle(grid)
    assert not solve(grid)
