# PROMPTS

## 04 (out of WS credits apparently) Measure performance, using timeit


## 03   mk seeder.py

## 02   dataviz
Answer concisely.  What is the easiest data visualization we can use to show the grid? Don't write any code yet, just describe some options.

Let's go with the simplest graphic table possible. We will eventually want to plan for user interaction, but keep this as close to text-based as we can, while planning for graphics later.  Write the minimum code necessary to do this.Use very short variable names, keep comments and docstrings to a minimum.

## 01   mk grid.py
In a codefile in src/sudoku, create a simple 9x9 grid. each cell in the grid has a row, col, and 3x3 square grid coordinate.  rows, cols, and 3x3-squares must all have their own separate naming system.  make this simple, intuitive.  Fill each cell with a zero.  Write the minimum code necessary to do this.

### testing
python3 -c "
import sys
sys.path.append('/home/aglines/code/sudoku/src')
from sudoku.grid import SudokuGrid

# Create and display the grid
grid = SudokuGrid()
print('9x9 Grid (all zeros):')
print(grid)
print()

# Show some cell coordinates
print('Sample cell coordinates:')
for row, col in [(0,0), (0,8), (4,4), (8,8)]:
    cell = grid.get_cell(row, col)
    print(f'Cell ({row},{col}): row={cell.row}, col={cell.col}, square={cell.square}, value={cell.value}')
"


# MOST OFTEN USED PROMPT STRINGS

Answer concisely. 

Think this through, but answer concisely. 

Write the minimum code necessary to do this.
Use very short variable names, keep comments and docstrings to a minimum.

Don't write any code yet, just describe some options.


Review the entire codebase.  What code is now obsolete or unneeded, now that we made the previous change?


