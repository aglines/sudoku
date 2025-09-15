import pytest
from sudoku.game import SudokuGame
from sudoku.grid import SudokuGrid


class TestSudokuGame:
    def test_game_init(self):
        game = SudokuGame()

        assert game.cursor_row == 0
        assert game.cursor_col == 0
        assert game.user_values == {}
        assert game.show_solution_mode is False
        assert isinstance(game.puzzle, SudokuGrid)
        assert isinstance(game.solution, SudokuGrid)

    def test_move_cursor_up(self):
        game = SudokuGame()
        game.cursor_row = 5
        game.move_cursor('up')
        assert game.cursor_row == 4

    def test_move_cursor_up_boundary(self):
        game = SudokuGame()
        game.cursor_row = 0
        game.move_cursor('up')
        assert game.cursor_row == 0  # Should not go below 0

    def test_move_cursor_down(self):
        game = SudokuGame()
        game.cursor_row = 3
        game.move_cursor('down')
        assert game.cursor_row == 4

    def test_move_cursor_down_boundary(self):
        game = SudokuGame()
        game.cursor_row = 8
        game.move_cursor('down')
        assert game.cursor_row == 8  # Should not go above 8

    def test_move_cursor_left(self):
        game = SudokuGame()
        game.cursor_col = 5
        game.move_cursor('left')
        assert game.cursor_col == 4

    def test_move_cursor_left_boundary(self):
        game = SudokuGame()
        game.cursor_col = 0
        game.move_cursor('left')
        assert game.cursor_col == 0  # Should not go below 0

    def test_move_cursor_right(self):
        game = SudokuGame()
        game.cursor_col = 3
        game.move_cursor('right')
        assert game.cursor_col == 4

    def test_move_cursor_right_boundary(self):
        game = SudokuGame()
        game.cursor_col = 8
        game.move_cursor('right')
        assert game.cursor_col == 8  # Should not go above 8

    def test_move_cursor_invalid_direction(self):
        game = SudokuGame()
        initial_row, initial_col = game.cursor_row, game.cursor_col
        game.move_cursor('invalid')
        assert game.cursor_row == initial_row
        assert game.cursor_col == initial_col

    def test_set_value_valid(self):
        game = SudokuGame()
        # Find an empty cell
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0:
                    game.cursor_row, game.cursor_col = r, c
                    result = game.set_value(5)
                    assert result is True
                    assert game.user_values[(r, c)] == 5
                    return

    def test_set_value_given_cell(self):
        game = SudokuGame()
        # Find a cell with a given value
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value != 0:
                    game.cursor_row, game.cursor_col = r, c
                    result = game.set_value(5)
                    assert result is False
                    assert (r, c) not in game.user_values
                    return

    def test_set_value_in_solution_mode(self):
        game = SudokuGame()
        game.show_solution_mode = True

        # Find an empty cell in puzzle
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0:
                    game.cursor_row, game.cursor_col = r, c
                    result = game.set_value(5)
                    assert result is False
                    assert (r, c) not in game.user_values
                    return

    def test_set_value_invalid_range(self):
        game = SudokuGame()
        # Find an empty cell
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0:
                    game.cursor_row, game.cursor_col = r, c

                    # Test invalid values
                    assert game.set_value(0) is False
                    assert game.set_value(10) is False
                    assert (r, c) not in game.user_values
                    return

    def test_clear_cell_with_user_value(self):
        game = SudokuGame()
        game.user_values[(3, 4)] = 7
        game.cursor_row, game.cursor_col = 3, 4

        result = game.clear_cell()
        assert result is True
        assert (3, 4) not in game.user_values

    def test_clear_cell_no_user_value(self):
        game = SudokuGame()
        game.cursor_row, game.cursor_col = 3, 4

        result = game.clear_cell()
        assert result is False

    def test_toggle_solution(self):
        game = SudokuGame()
        initial_state = game.show_solution_mode

        game.toggle_solution()
        assert game.show_solution_mode != initial_state

        game.toggle_solution()
        assert game.show_solution_mode == initial_state

    def test_new_game(self):
        game = SudokuGame()

        # Modify game state
        game.cursor_row, game.cursor_col = 5, 6
        game.user_values[(2, 3)] = 7
        game.show_solution_mode = True
        old_puzzle = game.puzzle

        game.new_game()

        # State should be reset
        assert game.cursor_row == 0
        assert game.cursor_col == 0
        assert game.user_values == {}
        assert game.show_solution_mode is False
        assert game.puzzle != old_puzzle  # New puzzle generated

    def test_get_display_value_given(self):
        game = SudokuGame()

        # Find a cell with given value
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value != 0:
                    expected = str(game.puzzle.grid[r][c].value)
                    assert game.get_display_value(r, c) == expected
                    return

    def test_get_display_value_user(self):
        game = SudokuGame()
        # Make sure the cell is empty first
        game.puzzle.grid[3][4].value = 0
        game.user_values[(3, 4)] = 8

        assert game.get_display_value(3, 4) == "8"

    def test_get_display_value_empty(self):
        game = SudokuGame()

        # Find an empty cell
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0 and (r, c) not in game.user_values:
                    assert game.get_display_value(r, c) == " "
                    return

    def test_get_display_value_solution_mode(self):
        game = SudokuGame()
        game.show_solution_mode = True

        # Any cell should show solution value
        expected = str(game.solution.grid[0][0].value)
        assert game.get_display_value(0, 0) == expected

    def test_get_cell_type_given(self):
        game = SudokuGame()

        # Find a cell with given value, not at cursor position
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value != 0 and (r, c) != (game.cursor_row, game.cursor_col):
                    assert game.get_cell_type(r, c) == 'given'
                    return

    def test_get_cell_type_given_cursor(self):
        game = SudokuGame()

        # Find a cell with given value and set cursor there
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value != 0:
                    game.cursor_row, game.cursor_col = r, c
                    assert game.get_cell_type(r, c) == 'given_cursor'
                    return

    def test_get_cell_type_user(self):
        game = SudokuGame()
        # Make sure cell is empty and set user value
        game.puzzle.grid[3][4].value = 0
        game.user_values[(3, 4)] = 5

        assert game.get_cell_type(3, 4) == 'user'

    def test_get_cell_type_user_cursor(self):
        game = SudokuGame()
        # Make sure cell is empty and set user value
        game.puzzle.grid[3][4].value = 0
        game.user_values[(3, 4)] = 5
        game.cursor_row, game.cursor_col = 3, 4

        assert game.get_cell_type(3, 4) == 'user_cursor'

    def test_get_cell_type_empty(self):
        game = SudokuGame()

        # Find an empty cell
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0:
                    assert game.get_cell_type(r, c) == 'empty'
                    return

    def test_get_cell_type_empty_cursor(self):
        game = SudokuGame()

        # Find an empty cell and set cursor there
        for r in range(9):
            for c in range(9):
                if game.puzzle.grid[r][c].value == 0:
                    game.cursor_row, game.cursor_col = r, c
                    assert game.get_cell_type(r, c) == 'empty_cursor'
                    return

    def test_get_cell_type_solution_mode(self):
        game = SudokuGame()
        game.show_solution_mode = True
        # Move cursor away from (0,0)
        game.cursor_row, game.cursor_col = 1, 1

        assert game.get_cell_type(0, 0) == 'solution'

    def test_get_cell_type_solution_cursor(self):
        game = SudokuGame()
        game.show_solution_mode = True
        game.cursor_row, game.cursor_col = 2, 3

        assert game.get_cell_type(2, 3) == 'solution_cursor'