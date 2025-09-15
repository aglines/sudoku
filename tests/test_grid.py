import pytest
from sudoku.grid import SudokuGrid, Cell


class TestCell:
    def test_cell_init_default(self):
        cell = Cell(2, 3)
        assert cell.row == 2
        assert cell.col == 3
        assert cell.value == 0

    def test_cell_init_with_value(self):
        cell = Cell(1, 5, 7)
        assert cell.row == 1
        assert cell.col == 5
        assert cell.value == 7

    def test_cell_value_access(self):
        cell = Cell(0, 0, 5)
        assert cell.value == 5

    def test_cell_empty_value(self):
        cell = Cell(0, 0)
        assert cell.value == 0


class TestSudokuGrid:
    def test_grid_init(self):
        grid = SudokuGrid()
        assert len(grid.grid) == 9
        assert len(grid.grid[0]) == 9

        # Check all cells initialized correctly
        for r in range(9):
            for c in range(9):
                assert grid.grid[r][c].row == r
                assert grid.grid[r][c].col == c
                assert grid.grid[r][c].value == 0

    def test_str_empty_grid(self):
        grid = SudokuGrid()
        result = str(grid)

        # Should contain mostly zeros
        assert result.count("0") == 81

    def test_str_with_values(self):
        grid = SudokuGrid()
        grid.grid[0][0].value = 5
        grid.grid[4][4].value = 9

        result = str(grid)
        assert "5" in result
        assert "9" in result

    def test_set_and_get_values(self):
        grid = SudokuGrid()

        # Set some values
        grid.grid[0][0].value = 1
        grid.grid[8][8].value = 9
        grid.grid[4][5].value = 7

        # Verify they're set correctly
        assert grid.grid[0][0].value == 1
        assert grid.grid[8][8].value == 9
        assert grid.grid[4][5].value == 7

        # Verify other cells remain empty
        assert grid.grid[0][1].value == 0
        assert grid.grid[1][0].value == 0