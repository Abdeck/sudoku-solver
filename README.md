# sudoku solver

Solves any valid 9x9 sudoku using backtracking. It also checks if the starting puzzle already breaks the rules, and tells you if a puzzle just can't be solved.

## example

```
$ python sudoku.py puzzles/easy.txt
Puzzle:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
...

Solved:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
...
```

## how it works

Basically it brute forces it, but smart about it:

1. find the first empty cell
2. try 1 to 9 in it
3. if a number doesn't break the row, column or 3x3 box rule, put it in and move to the next empty cell
4. if it gets stuck later, erase the last number and try the next one (that's the backtracking part)
5. keep going until the board's full or every option's been tried

The one people call the "world's hardest sudoku" is in `puzzles/hard.txt`. Takes way under a second.

## running it

You just need Python 3.

```
python sudoku.py puzzles/easy.txt
```

Puzzle files are 81 digits, with `0` or `.` for blanks. Spaces and line breaks don't matter.

## tests

There's 9 tests with pytest. They cover reading the puzzle, each sudoku rule, actually solving it, making sure the original numbers don't get changed, and what happens with invalid or unsolvable puzzles.

```
pip install pytest
pytest
```

## what i learned

- how recursion and backtracking work together to search through options
- splitting stuff into small functions makes it way easier to test
- writing tests for the edge cases too, not just the easy puzzle

## built with

Python 3, pytest
