import pytest
from sudoku.seeder import SudokuSeeder
from sudoku.grid import SudokuGrid


class TestSudokuSeeder:
    def test_seeder_init(self):
        seeder = SudokuSeeder()
        assert seeder is not None

    def test_generate_creates_valid_grid(self):
        seeder = SudokuSeeder()
        grid = seeder.generate()

        assert isinstance(grid, SudokuGrid)
        assert len(grid.grid) == 9
        assert len(grid.grid[0]) == 9

    def test_generate_fills_all_cells(self):
        seeder = SudokuSeeder()
        grid = seeder.generate()

        # All cells should be filled (non-zero)
        for r in range(9):
            for c in range(9):
                assert 1 <= grid.grid[r][c].value <= 9

    def test_generate_valid_rows(self):
        seeder = SudokuSeeder()
        grid = seeder.generate()

        # Each row should contain digits 1-9 exactly once
        for r in range(9):
            row_values = [grid.grid[r][c].value for c in range(9)]
            assert sorted(row_values) == list(range(1, 10))

    def test_generate_valid_columns(self):
        seeder = SudokuSeeder()
        grid = seeder.generate()

        # Each column should contain digits 1-9 exactly once
        for c in range(9):
            col_values = [grid.grid[r][c].value for r in range(9)]
            assert sorted(col_values) == list(range(1, 10))

    def test_generate_valid_boxes(self):
        seeder = SudokuSeeder()
        grid = seeder.generate()

        # Each 3x3 box should contain digits 1-9 exactly once
        for box_row in range(3):
            for box_col in range(3):
                box_values = []
                for r in range(box_row * 3, (box_row + 1) * 3):
                    for c in range(box_col * 3, (box_col + 1) * 3):
                        box_values.append(grid.grid[r][c].value)
                assert sorted(box_values) == list(range(1, 10))

    def test_create_puzzle_returns_two_grids(self):
        seeder = SudokuSeeder()
        puzzle, solution = seeder.create_puzzle()

        assert isinstance(puzzle, SudokuGrid)
        assert isinstance(solution, SudokuGrid)

    def test_create_puzzle_default_blanks(self):
        seeder = SudokuSeeder()
        puzzle, solution = seeder.create_puzzle()

        # Count blank cells (should be 18 by default)
        blank_count = 0
        for r in range(9):
            for c in range(9):
                if puzzle.grid[r][c].value == 0:
                    blank_count += 1

        assert blank_count == 18

    def test_create_puzzle_custom_blanks(self):
        seeder = SudokuSeeder()
        puzzle, solution = seeder.create_puzzle(blanks=30)

        # Count blank cells (should be 30)
        blank_count = 0
        for r in range(9):
            for c in range(9):
                if puzzle.grid[r][c].value == 0:
                    blank_count += 1

        assert blank_count == 30

    def test_create_puzzle_solution_is_valid(self):
        seeder = SudokuSeeder()
        puzzle, solution = seeder.create_puzzle()

        # Solution should be a valid complete grid
        for r in range(9):
            for c in range(9):
                assert 1 <= solution.grid[r][c].value <= 9

        # Check solution validity (rows, columns, boxes)
        # Rows
        for r in range(9):
            row_values = [solution.grid[r][c].value for c in range(9)]
            assert sorted(row_values) == list(range(1, 10))

        # Columns
        for c in range(9):
            col_values = [solution.grid[r][c].value for r in range(9)]
            assert sorted(col_values) == list(range(1, 10))

    def test_create_puzzle_consistency(self):
        seeder = SudokuSeeder()
        puzzle, solution = seeder.create_puzzle()

        # Where puzzle has values, they should match the solution
        for r in range(9):
            for c in range(9):
                if puzzle.grid[r][c].value != 0:
                    assert puzzle.grid[r][c].value == solution.grid[r][c].value

    def test_valid_method(self):
        seeder = SudokuSeeder()
        grid = SudokuGrid()

        # Test valid placement
        grid.grid[0][0].value = 1
        assert seeder._valid(grid, 0, 1, 2) is True  # Different number, same row
        assert seeder._valid(grid, 0, 1, 1) is False  # Same number, same row

    def test_multiple_generations_different(self):
        seeder = SudokuSeeder()
        grid1 = seeder.generate()
        grid2 = seeder.generate()

        # Grids should be different (very high probability)
        different = False
        for r in range(9):
            for c in range(9):
                if grid1.grid[r][c].value != grid2.grid[r][c].value:
                    different = True
                    break
            if different:
                break

        assert different