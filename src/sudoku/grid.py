from typing import List

class Cell:
    def __init__(self, row: int, col: int, value: int = 0) -> None:
        self.row: int = row          # Row: 0-8
        self.col: int = col          # Column: 0-8
        self.square: int = (row // 3) * 3 + (col // 3)  # Square: 0-8
        self.value: int = value

class SudokuGrid:
    def __init__(self) -> None:
        self.grid: List[List[Cell]] = [[Cell(row, col) for col in range(9)] for row in range(9)]

    def get_cell(self, row: int, col: int) -> Cell:
        return self.grid[row][col]

    def __str__(self) -> str:
        result: List[str] = []
        for row in range(9):
            row_str: str = " ".join(str(self.grid[row][col].value) for col in range(9))
            result.append(row_str)
        return "\n".join(result)
    

if __name__ == "__main__":
    g = SudokuGrid()
    print(g)
