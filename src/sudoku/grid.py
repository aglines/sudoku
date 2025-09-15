class Cell:
    def __init__(self, row, col, value=0):
        self.row = row          # Row: 0-8
        self.col = col          # Column: 0-8
        self.square = (row // 3) * 3 + (col // 3)  # Square: 0-8
        self.value = value

class SudokuGrid:
    def __init__(self):
        self.grid = [[Cell(row, col) for col in range(9)] for row in range(9)]
    
    def get_cell(self, row, col):
        return self.grid[row][col]
    
    def __str__(self):
        result = []
        for row in range(9):
            row_str = " ".join(str(self.grid[row][col].value) for col in range(9))
            result.append(row_str)
        return "\n".join(result)
    

if __name__ == "__main__":
    g = SudokuGrid()
    print(g)
