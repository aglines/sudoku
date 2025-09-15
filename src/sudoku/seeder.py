import random
from grid import SudokuGrid

class SudokuSeeder:
    def __init__(self):
        pass
    
    def _valid(self, g, r, c, n):
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
    
    def _fill(self, g, r, c):
        if r == 9:
            return True
        nr, nc = (r, c + 1) if c < 8 else (r + 1, 0)
        nums = list(range(1, 10))
        random.shuffle(nums)
        for n in nums:
            if self._valid(g, r, c, n):
                g.grid[r][c].value = n
                if self._fill(g, nr, nc):
                    return True
                g.grid[r][c].value = 0
        return False
    
    def generate(self):
        g = SudokuGrid()
        self._fill(g, 0, 0)
        return g

if __name__ == "__main__":
    s = SudokuSeeder()
    g = s.generate()
    g.show()
