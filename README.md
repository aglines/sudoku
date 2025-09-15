# Sudoku

A modern terminal-based Sudoku game built with Python, featuring an interactive UI, multiple difficulty levels, and comprehensive puzzle generation.

## Features

🎯 **Interactive Terminal UI** - Rich console interface with colored grid display and cursor navigation
🎲 **Three Difficulty Levels** - Easy (30 blanks), Medium (40 blanks), Hard (50 blanks)
⚡ **Fast Puzzle Generation** - Backtracking algorithm creates valid puzzles instantly
🧩 **Complete Game Logic** - Full sudoku validation with proper game state management
🎮 **Intuitive Controls** - Arrow keys or WASD navigation, number input, solution toggle
🏗️ **Clean Architecture** - Separation of game logic from UI, fully type-hinted codebase
✅ **Comprehensive Testing** - 51 unit tests covering all core functionality

## Quick Start

Install and run:
```bash
pip install -e .
sudoku
```

## Controls

- **Arrow Keys** or **WASD** - Move cursor
- **1-9** - Enter numbers
- **Space** or **0** - Clear cell
- **X** - Toggle solution view
- **N** - New game (with difficulty selection)
- **Q** - Quit

## Installation

1. Clone the repository and navigate to the directory
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the package:
   ```bash
   pip install -e .
   ```
4. Run the game:
   ```bash
   sudoku
   ```

## Development

Run tests:
```bash
pytest -v
```

The project uses modern Python practices including type hints, comprehensive testing, and clean separation of concerns.

## Technical Highlights

- **Backtracking Algorithm**: Efficient puzzle generation using recursive backtracking with randomization
- **Clean Architecture**: Separation of game logic, UI, and data models
- **Type Safety**: Full type hints throughout the codebase for better maintainability
- **Comprehensive Testing**: 51 unit tests covering all core functionality
- **Modern Python**: Uses latest Python features and best practices

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

This project follows standard Python development practices:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass with `pytest -v`
5. Submit a pull request
