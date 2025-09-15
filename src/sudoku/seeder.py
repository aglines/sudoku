import random
from typing import Tuple, List
from sudoku.grid import SudokuGrid

class SudokuSeeder:
    def __init__(self) -> None:
        pass

    def _valid(self, g: SudokuGrid, r: int, c: int, n: int) -> bool:
        # Check row
        for i in range(9):
            if g.grid[r][i].value == n:
                return False
        # Check col
        for i in range(9):
            if g.grid[i][c].value == n:
                return False
        # Check 3x3
        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if g.grid[sr + i][sc + j].value == n:
                    return False
        return True

    def _fill(self, g: SudokuGrid, r: int, c: int) -> bool:
        if r == 9:
            return True
        nr, nc = (r, c + 1) if c < 8 else (r + 1, 0)
        nums: List[int] = list(range(1, 10))
        random.shuffle(nums)
        for n in nums:
            if self._valid(g, r, c, n):
                g.grid[r][c].value = n
                if self._fill(g, nr, nc):
                    return True
                g.grid[r][c].value = 0
        return False

    def generate(self) -> SudokuGrid:
        g = SudokuGrid()
        self._fill(g, 0, 0)
        return g

    def create_puzzle(self, blanks: int = 18) -> Tuple[SudokuGrid, SudokuGrid]:
        # Generate solved version
        solved_grid = self.generate()

        # Create puzzle copy
        puzzle_grid = SudokuGrid()
        for r in range(9):
            for c in range(9):
                puzzle_grid.grid[r][c].value = solved_grid.grid[r][c].value

        # Randomly mask cells
        positions: List[Tuple[int, int]] = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(positions)
        for r, c in positions[:blanks]:
            puzzle_grid.grid[r][c].value = 0

        return puzzle_grid, solved_grid

