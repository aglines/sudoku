from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from readchar import readkey
from readchar import key as keys
from sudoku.game import SudokuGame

class ColorScheme:
    GIVEN = "bold blue"
    USER_INPUT = "green"
    SELECTED = "black on white"
    GRID_BORDER = "white"

class SudokuTUI:
    def __init__(self):
        self.console = Console()
        self.game = SudokuGame()

    def draw_grid(self):
        table = Table.grid(padding=(0, 1))

        for r in range(9):
            row_cells = []
            for c in range(9):
                display = self.game.get_display_value(r, c)
                cell_type = self.game.get_cell_type(r, c)

                # Map cell types to styles
                style_map = {
                    'given': ColorScheme.GIVEN,
                    'given_cursor': f"{ColorScheme.SELECTED} {ColorScheme.GIVEN}",
                    'user': ColorScheme.USER_INPUT,
                    'user_cursor': f"{ColorScheme.SELECTED} {ColorScheme.USER_INPUT}",
                    'empty': "white",
                    'empty_cursor': ColorScheme.SELECTED,
                    'solution': "bold yellow",
                    'solution_cursor': "bold yellow"
                }
                style = style_map[cell_type]

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

        title = "Solution" if self.game.show_solution_mode else "Sudoku Puzzle"
        return Panel(table, title=title, border_style=ColorScheme.GRID_BORDER)

    def handle_input(self, key):
        # Navigation - arrow keys and WASD
        if key == keys.UP or key.lower() == 'w':
            self.game.move_cursor('up')
        elif key == keys.DOWN or key.lower() == 's':
            self.game.move_cursor('down')
        elif key == keys.LEFT or key.lower() == 'a':
            self.game.move_cursor('left')
        elif key == keys.RIGHT or key.lower() == 'd':
            self.game.move_cursor('right')

        # Number input
        elif key.isdigit():
            self.game.set_value(int(key))

        # Clear cell
        elif key in [' ', '0']:
            self.game.clear_cell()

        # Commands
        elif key.lower() == 'x':
            self.game.toggle_solution()
        elif key.lower() == 'n':
            self.game.new_game()
        elif key.lower() == 'q':
            return False

        return True


    def run(self):
        while True:
            self.console.clear()
            self.console.print(self.draw_grid())
            self.console.print(f"\n[bold]Cursor position:[/] Row {self.game.cursor_row + 1}, Col {self.game.cursor_col + 1}")
            self.console.print("\n[bold]Controls:[/] arrows/wasd to move, 1-9 to enter number, space/0 to clear")
            self.console.print("[bold]Commands:[/] 'x' toggle solution, 'n' new game, 'q' quit")
            self.console.print("\n[bold cyan]Press any key:[/]")

            try:
                key = readkey()
                if not self.handle_input(key):
                    break
            except KeyboardInterrupt:
                break

        self.console.print("\n[bold green]Thanks for playing![/]")

if __name__ == "__main__":
    tui = SudokuTUI()
    tui.run()