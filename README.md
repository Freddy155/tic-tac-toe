# Tic-Tac-Toe Game

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to install](#how-to-install)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Game Logic](#game-logic)
- [User Interface](#user-interface)
- [Reset Button](#reset-button)
- [Player Records](#player-records)
- [Conclusion](#conclusion)

---

## Introduction

The Tic-Tac-Toe game is a classic two-player game where players take turns marking cells in a 3x3 grid to achieve a winning pattern, traditionally "three in a row." This documentation provides an overview of the game's features, rules, code structure, and user interface.

## Features

The Tic-Tac-Toe game includes the following features:

- A 3x3 game board.
- Alternate turns between two players (X and O).
- Validation of valid moves.
- Detection of game-winning conditions.
- Detection of a draw.
- A graphical user interface (GUI) using Tkinter.
- A "Reset" button to start a new game.
- Player records that keep track of the number of wins for each player.

## How to install
1. clone repo 
```bash
git clone https://github.com/Freddy155/tic-tac-toe.git
```
2. enter directory
```bash
cd tic-tac-toe
 ```



## How to Play

1. Launch the game by executing the `app.py` script.
```bash
python app.py
```
2. The game starts with Player X's turn.
3. Players take turns to click on an empty cell on the game board.
4. The first player to achieve three in a row horizontally, vertically, or diagonally wins.
5. The game ends when a player wins or when there is a draw.
6. Use the "Reset" button to start a new game at any time.

## Code Structure

The code for the Tic-Tac-Toe game is organized as follows:

- The game board is represented as a 3x3 grid.
- A `display_board` function shows the current state of the board.
- Functions `check_win` and `check_draw` verify win/draw conditions.
- `get_player_move` handles player input validation.
- A game loop in the `play_game` function manages the game.
- The GUI interface is created using Tkinter.
- Player records are updated and displayed.

## Game Logic

The game logic follows standard Tic-Tac-Toe rules:

- Players take turns to place their symbol (X or O) on an empty cell.
- The game checks for win conditions after each move.
- If a player achieves three in a row, they win.
- The game can also end in a draw if all cells are filled with no winner.

## User Interface

The game features a graphical user interface (GUI) created using Tkinter. The interface includes:

- A 3x3 grid of buttons representing the game board.
- A message label indicating whose turn it is.
- A "Reset" button for starting a new game.
- A player record section to track wins for Player X and Player O.

## Reset Button

The "Reset" button allows you to reset the game board and start a new game at any time. It clears the game board and sets Player X as the starting player.

## Player Records

Player records are displayed at the bottom of the game interface. These records show the number of wins for each player (Player X and Player O). Whenever a player wins a game, their win count is incremented, and the player record is updated.

## Conclusion

The Tic-Tac-Toe game provides a classic and enjoyable gaming experience. It features a user-friendly GUI, win detection, a draw condition, and player records to keep track of victories. Enjoy playing the game and have fun!

For more details on the code and its implementation, please refer to the source code in the `app.py` file.
