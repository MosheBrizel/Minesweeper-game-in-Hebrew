# Minesweeper-game-in-Hebrew
This code is a Minesweeper game implemented in Python with Tkinter. It offers different levels and a custom option to set grid size and bomb count. Players reveal buttons, avoiding bombs. Adjacent buttons show the number of nearby bombs. Right-clicking marks potential bombs. The code manages game logic, GUI, and random bomb placement. 
# Minesweeper Game

This is a single player Minesweeper game implemented in Python with Tkinter.

## Game Description

- Classic Minesweeper game where the player clicks on cells to reveal numbers and avoid hidden mines. 

- Two initial difficulty levels - beginner (5x6 grid, 3 mines) and expert (10x25 grid, 20 mines).

- Option to choose custom grid size and number of mines.

- Numbers indicate how many mines are in the 8 surrounding cells.

- Right-click to place flag on suspected mine locations.

- Game ends when player clicks on a mine or reveals all non-mine cells.

## Requirements

- Python 3
- Tkinter

## Usage

Run `שולה מוקשים.py` to start the game:

`python שולה מוקשים.py`


Select desired difficulty level or custom options. 

Left-click on cells to reveal. Right-click to place flags.

## Code Overview

- `minesweeper.py` - Main game file handling UI and game logic
- `cell.py` - Cell class representing each cell on the grid
- `board.py` - Game board class managing the grid of cells
- `game.py` - Overall game class with game loop and win/lose logic

Key functions:

- `generate_board()` - Creates grid of cells and places mines randomly
- `check_cell()` - Handles left-click on cell to reveal  
- `flag_cell()` - Toggles right-click to place/remove flag
- `get_adjacent_cells()` - Returns list of cells surrounding a cell
- `check_win()` - Checks if all non-mine cells revealed for win condition
