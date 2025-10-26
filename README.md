# Welcome to Tic Tac Toe

![Stars](https://img.shields.io/github/stars/hrosicka/TicTacToe)
![Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Game](https://img.shields.io/badge/Game-TicTacToe-red?logo=python)
[![GitHub last commit](https://img.shields.io/github/last-commit/hrosicka/TicTacToeWeb)](https://github.com/hrosicka/TicTacToe/commits/main)

This is a simple and interactive Tic Tac Toe game implemented using Python and the Tkinter library for the graphical user interface (GUI).

Get ready to dominate the grid and emerge victorious in this epic Tic Tac Toe battle! This isn't your childhood game anymore. It's a fast-paced, strategic showdown where only one player can claim the title of Tic Tac Toe Champion.

---

## 🎮 Features

* **Intuitive Graphical Interface:** A clean and user-friendly 3x3 grid for playing.
* **Two Players:** Supports two players taking turns to place their marks.
* **Symbol and Color Choice:** Players can choose their preferred symbol ('X' or 'O') and a color for their moves at the beginning of the game. The second player's choices are limited to ensure distinct symbols and colors.
* **Automatic Win Detection:** The game automatically detects a winner (three in a row, column, or diagonal).
* **"Cat's Game" Detection:** Detects when all squares are filled without a winner, resulting in a tie.
* **Clear Winner Display:** Announces the winner or a tie at the end of each game.
* **Game Statistics:** Tracks and displays the number of wins for each player and the number of ties.
* **Automatic Game Reset:** After announcing the winner or a tie, the game board resets automatically after a short delay, ready for a new round.
* **First Player Randomization:** The first player for each new game is chosen randomly.
* **Tooltip Hints:** Provides helpful tooltips, especially when the second player is choosing their symbol and color, indicating if a choice has already been made by the first player.
* **Confirmation on Exit:** Asks for confirmation before closing the game window to prevent accidental closure.
* **DPI Awareness:** Includes code to improve the application's appearance on high-DPI displays on Windows.
  
---
  
## 🛠️ How to Run

1.  **Prerequisites:** Ensure you have Python installed on your system. Tkinter is usually included with standard Python installations.
2.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `main.py`).
3.  **Run from Terminal:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the command:
    ```bash
    python main.py
    ```
    This will launch the Tic Tac Toe game window.

---

## Conquer the Board

The game takes place on a familiar 3x3 grid. You'll take turns placing your mark (X or O) on the empty squares. But here's the catch: think strategically! A true champion anticipates their opponent's moves, blocking their attempts at victory while maneuvering their own Xs or Os to form a winning line.

---

## Claim Your Glory

The first player to score a line of three Xs or Os horizontally, vertically, or diagonally reigns supreme! But wait, there's more! If all the squares fill up without a winner, it's not a boring tie. It's a  Cat's Game – a hilarious twist where the feline overlord claims the board as its territory!

---

## Game Instructions

1.  **Symbol and Color Selection:**
    * When the game starts, a dialog window will appear for Player 1 to choose their symbol ('X' or 'O') and a color for their moves by clicking on the respective buttons.
    * Another dialog will then appear for Player 2 to make their symbol and color choices. Player 2 cannot choose the same symbol or color as Player 1. Tooltips will indicate if a symbol or color is already taken.
    * Click the "Choose for Player 1" or "Choose for Player 2" button to confirm your selections.

    ![](https://github.com/hrosicka/TicTacToe/blob/master/doc/symbol_color.png)

2.  **Playing the Game:**
    * The game will randomly determine which player goes first and display a message box indicating the starting player.
    * Players take turns clicking on an empty square on the game board to place their chosen symbol.
    * The color of the symbol placed on the board will correspond to the color chosen by the player.
  
    ![](https://github.com/hrosicka/TicTacToe/blob/master/doc/who_starts.png)
    
3.  **Game End:**
    * The game ends when one player gets three of their symbols in a row (horizontally, vertically, or diagonally), or when all nine squares are filled (a tie, also known as "Cat's Game").
    * The winner (or "Cat's Game") will be announced above the game board.
    * The game board will automatically reset after a short delay, and a new game will begin with a randomly chosen starting player.
    * The statistics for wins and ties are displayed below the game board and are updated after each game.

    ![](https://github.com/hrosicka/TicTacToe/blob/master/doc/tic_tac_toe.png)
      
4.  **Quitting the Game:**
    * You can close the game window by clicking the close button (usually an "X" in the corner of the window). A confirmation dialog will appear to ensure you want to quit.

---

## 🌟 Code Explanation

The code is structured as a class `TicTacToe` which encapsulates the game logic and GUI elements. Here's a brief overview of the key parts:

* **`__init__(self)`:** Initializes the main window, sets the title, initializes game statistics, creates the winner label, creates the game board buttons using `create_widgets()`, allows players to choose their symbols and colors using `choose_symbol_color()`, starts the first game with `start_game()`, and sets up the window closing protocol.
* **`on_closing(self)`:** Handles the window closing event by asking the user for confirmation.
* **`choose_symbol_color(self, player)`:** Creates a top-level dialog window where each player can choose their symbol ('X' or 'O') and a color from a predefined palette. It includes logic to prevent the second player from choosing the same symbol or color as the first player and provides visual feedback for selections.
* **`determine_first_player(self)`:** Randomly selects either "X" or "O" as the starting player for a new game.
* **`start_game(self)`:** Resets the game board, determines the first player, and displays an information message about who starts.
* **`create_widgets(self)`:** Creates the 3x3 grid of buttons for the game board and configures their click command to `click_button()`. It also creates the label to display game statistics.
* **`click_button(self, row, col)`:** Handles the event when a player clicks on a button. It places the current player's symbol on the button, checks for a win, and switches to the other player if the game hasn't ended.
* **`check_win(self)`:** Checks all possible winning conditions (rows, columns, diagonals) and also checks for a "Cat's Game".
* **`switch_player(self)`:** Changes the `current_player` variable to the other player.
* **`show_winner(self)`:** Updates the winner label, disables all buttons, updates the game statistics, and schedules the `reset_game()` function to be called after a delay.
* **`reset_game(self)`:** Clears the game board, resets the winner status, starts a new game, and updates the statistics label.
* **`if __name__ == "__main__":`:** Ensures that the `TicTacToe` class is instantiated and the game starts only when the script is executed directly.

So, are you ready to claim your glory on the Tic Tac Toe board? Download, run, and let the strategic battles begin! May your Xs and Os always land in the right place.


---

## 👩‍💻 Author

Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka) 👩‍🔬

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.
