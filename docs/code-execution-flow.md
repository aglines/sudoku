● Code Execution Flow

  Startup Path:
  1. sudoku CLI command → sudoku.tui:main()
  2. main() → SudokuTUI.__init__()
  3. SudokuTUI.__init__() → select_difficulty() (prompts user for 1/2/3)
  4. select_difficulty() → SudokuGame(difficulty)
  5. SudokuGame.__init__() → SudokuSeeder.create_puzzle(blanks)
  6. create_puzzle() → generate() (backtracking algorithm fills grid)
  7. Returns puzzle + solution grids to game instance
  8. main() → tui.run() starts main game loop

  Game Loop Path:
  1. run() → console.clear() + draw_grid() + display info
  2. draw_grid() → calls game.get_display_value() and game.get_cell_type() for each cell
  3. readkey() waits for user input
  4. handle_input(key) → routes to appropriate game.*() methods:
    - Arrow/WASD → game.move_cursor(direction)
    - Numbers → game.set_value(int)
    - Space/0 → game.clear_cell()
    - 'x' → game.toggle_solution()
    - 'n' → select_difficulty() → game.new_game(difficulty)
    - 'q' → breaks loop

  Shutdown Path:
  1. 'q' key → handle_input() returns False
  2. run() loop breaks → prints "Thanks for playing!"
  3. main() exits → process ends

  Key Classes:
  - SudokuTUI: UI layer (Rich console, input handling)
  - SudokuGame: Game state and logic
  - SudokuSeeder: Puzzle generation algorithms
  - SudokuGrid/Cell: Data structures
