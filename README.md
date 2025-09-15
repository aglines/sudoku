# SUDOKU - code to create and solve sudoku puzzles

## Methodology
- vibe coding practice: write prompts in an IDE with no autocomplete (vscode, having unsubscribed from copilot)
- break prompts down to smaller chunks to ensure code isn't messy spaghetti  
- run prompts in Windsurf or Claude

### Methodology notes
- write the most often re-used prompt strings, bc it's best practice to not assume that a coding LLM will always or consistently follow the system prompts we attempt to give it

## DONE
- project setup using uv
- create prompt logic for seeding sudoku grid
- start saving each prompt i get along with what its result was
- visualize the grid, how easiest to show this
- find way to randomize this grid with the full solved legal sudoku
    (landed on a recursive backtracking algo with randomization)
- explore benchmarking via timeit
- create unsolved versions of the ones that get generated, at different levels (research indicates absolute hardest ones have minimum 17 cells populated of the 81 possible)

## TODO

- do not aim at frontend, just aim at some console interface / text user interface TUI that later i could embed in a webpage.  this is not a frontend project.  Use the python module rich, aimed at richtext


