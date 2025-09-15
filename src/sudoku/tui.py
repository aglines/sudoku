from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from getch import getch
from sudoku.seeder import SudokuSeeder

class ColorScheme:
    GIVEN = "bold blue"
    USER_INPUT = "green"
    SELECTED = "black on white"
    GRID_BORDER = "white"

class SudokuTUI:
    def __init__(self):
        self.console = Console()
        self.seeder = SudokuSeeder()
        self.puzzle, self.solution = self.seeder.create_puzzle()
        self.cursor_row, self.cursor_col = 0, 0
        self.user_values = {}  # Track user inputs
        self.show_solution_mode = False

    def draw_grid(self):
        table = Table.grid(padding=(0, 1))

        for r in range(9):
            row_cells = []
            for c in range(9):
                if self.show_solution_mode:
                    display = str(self.solution.grid[r][c].value)
                    style = "bold yellow"
                else:
                    value = self.puzzle.grid[r][c].value

                    if (r, c) == (self.cursor_row, self.cursor_col):
                        if value != 0:  # Given number at cursor
                            display = str(value)
                            style = f"{ColorScheme.SELECTED} {ColorScheme.GIVEN}"
                        elif (r, c) in self.user_values:  # User input at cursor
                            display = str(self.user_values[(r, c)])
                            style = f"{ColorScheme.SELECTED} {ColorScheme.USER_INPUT}"
                        else:  # Empty cell at cursor
                            display = " "
                            style = ColorScheme.SELECTED
                    elif value != 0:  # Given number
                        display = str(value)
                        style = ColorScheme.GIVEN
                    elif (r, c) in self.user_values:  # User input
                        display = str(self.user_values[(r, c)])
                        style = ColorScheme.USER_INPUT
                    else:  # Empty cell
                        display = " "
                        style = "white"

                # Add borders for 3x3 boxes
                if c in [2, 5]:
                    display += " │"

                row_cells.append(f"[{style}]{display}[/]")

            table.add_row(*row_cells)

            # Add horizontal separator for 3x3 boxes
            if r in [2, 5]:
                separator_cells = ["─" * 3 if c not in [2, 5] else "─" * 3 + " ┼" for c in range(9)]
                separator_cells[-1] = separator_cells[-1].replace(" ┼", "")
                table.add_row(*[f"[{ColorScheme.GRID_BORDER}]{cell}[/]" for cell in separator_cells])

        title = "Solution" if self.show_solution_mode else "Sudoku Puzzle"
        return Panel(table, title=title, border_style=ColorScheme.GRID_BORDER)

    def handle_input(self, key):
        # Navigation
        if key.lower() == 'w':
            if self.cursor_row > 0:
                self.cursor_row -= 1
        elif key.lower() == 's':
            if self.cursor_row < 8:
                self.cursor_row += 1
        elif key.lower() == 'a':
            if self.cursor_col > 0:
                self.cursor_col -= 1
        elif key.lower() == 'd':
            if self.cursor_col < 8:
                self.cursor_col += 1

        # Number input (only if not a given cell and not in solution mode)
        elif key.isdigit() and not self.show_solution_mode:
            num = int(key)
            if 1 <= num <= 9:
                # Only allow input in empty cells (not given numbers)
                if self.puzzle.grid[self.cursor_row][self.cursor_col].value == 0:
                    self.user_values[(self.cursor_row, self.cursor_col)] = num

        # Clear cell
        elif key in [' ', '0']:
            if (self.cursor_row, self.cursor_col) in self.user_values:
                del self.user_values[(self.cursor_row, self.cursor_col)]

        # Commands
        elif key.lower() == 'x':
            self.show_solution_mode = not self.show_solution_mode
        elif key.lower() == 'n':
            self.new_game()
        elif key.lower() == 'q':
            return False

        return True

    def new_game(self):
        self.puzzle, self.solution = self.seeder.create_puzzle()
        self.user_values = {}
        self.show_solution_mode = False
        self.cursor_row, self.cursor_col = 0, 0

    def run(self):
        while True:
            self.console.clear()
            self.console.print(self.draw_grid())
            self.console.print(f"\n[bold]Cursor position:[/] Row {self.cursor_row + 1}, Col {self.cursor_col + 1}")
            self.console.print("\n[bold]Controls:[/] w/s/a/d to move, 1-9 to enter number, space/0 to clear")
            self.console.print("[bold]Commands:[/] 'x' toggle solution, 'n' new game, 'q' quit")
            self.console.print("\n[bold cyan]Press any key:[/]")

            try:
                key = getch()
                if not self.handle_input(key):
                    break
            except KeyboardInterrupt:
                break

        self.console.print("\n[bold green]Thanks for playing![/]")

if __name__ == "__main__":
    tui = SudokuTUI()
    tui.run()