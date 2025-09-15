from typing import Dict, Tuple, Literal
from sudoku.seeder import SudokuSeeder

CellType = Literal['given', 'given_cursor', 'user', 'user_cursor', 'empty', 'empty_cursor', 'solution', 'solution_cursor']
Direction = Literal['up', 'down', 'left', 'right']

class SudokuGame:
    def __init__(self) -> None:
        self.seeder = SudokuSeeder()
        self.puzzle, self.solution = self.seeder.create_puzzle()
        self.cursor_row: int = 0
        self.cursor_col: int = 0
        self.user_values: Dict[Tuple[int, int], int] = {}  # Track user inputs
        self.show_solution_mode: bool = False

    def move_cursor(self, direction: Direction) -> None:
        """Move cursor in given direction: 'up', 'down', 'left', 'right'"""
        if direction == 'up' and self.cursor_row > 0:
            self.cursor_row -= 1
        elif direction == 'down' and self.cursor_row < 8:
            self.cursor_row += 1
        elif direction == 'left' and self.cursor_col > 0:
            self.cursor_col -= 1
        elif direction == 'right' and self.cursor_col < 8:
            self.cursor_col += 1

    def set_value(self, value: int) -> bool:
        """Set value at current cursor position if valid"""
        if 1 <= value <= 9 and not self.show_solution_mode:
            if self.puzzle.grid[self.cursor_row][self.cursor_col].value == 0:
                self.user_values[(self.cursor_row, self.cursor_col)] = value
                return True
        return False

    def clear_cell(self) -> bool:
        """Clear value at current cursor position"""
        if (self.cursor_row, self.cursor_col) in self.user_values:
            del self.user_values[(self.cursor_row, self.cursor_col)]
            return True
        return False

    def toggle_solution(self) -> None:
        """Toggle solution display mode"""
        self.show_solution_mode = not self.show_solution_mode

    def new_game(self) -> None:
        """Start a new game"""
        self.puzzle, self.solution = self.seeder.create_puzzle()
        self.user_values = {}
        self.show_solution_mode = False
        self.cursor_row, self.cursor_col = 0, 0

    def get_display_value(self, row: int, col: int) -> str:
        """Get the value to display at given position"""
        if self.show_solution_mode:
            return str(self.solution.grid[row][col].value)

        value = self.puzzle.grid[row][col].value
        if value != 0:
            return str(value)
        elif (row, col) in self.user_values:
            return str(self.user_values[(row, col)])
        else:
            return " "

    def get_cell_type(self, row: int, col: int) -> CellType:
        """Get cell type: 'given', 'user', 'empty', 'cursor'"""
        is_cursor = (row, col) == (self.cursor_row, self.cursor_col)

        if self.show_solution_mode:
            return 'solution_cursor' if is_cursor else 'solution'

        value = self.puzzle.grid[row][col].value
        if value != 0:
            return 'given_cursor' if is_cursor else 'given'
        elif (row, col) in self.user_values:
            return 'user_cursor' if is_cursor else 'user'
        else:
            return 'empty_cursor' if is_cursor else 'empty'