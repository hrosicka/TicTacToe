import tkinter as tk
import random
import tkinter.messagebox as messagebox

class TicTacToe:
    """The Tic Tac Toe game class that manages the game state, handles player turns, and determines the winner."""
    
    def __init__(self):
        """Initializes the Tic Tac Toe game.

        This method creates the main Tkinter window, sets the window title to "Tic Tac Toe", initializes game
        statistics variables (wins for X, O, and ties), creates a label to display the winner, creates the game board
        with buttons, and starts the Tkinter main event loop.
        """
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Initialize statistics
        self.player_x_wins = 0
        self.player_o_wins = 0
        self.ties = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_colors = {"X": "lightgreen", "O": "lightcoral"} 
        self.default_button_color = "lightblue" 

        self.winner = None

        self.winner_label = tk.Label(self.root, text=f"Who wins?", font=('Arial', 15))
        self.winner_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.create_buttons()
        self.start_game()
        self.root.mainloop()

    def determine_first_player(self):
        """Randomly determines the first player."""
        return random.choice(["X", "O"])
    
    def start_game(self):
        """Starts a new game and displays an information message box about the starting player."""

        # Randomly determine the starting player (either 'X' or 'O')
        self.current_player = self.determine_first_player()

        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button['state'] = 'normal'
                button.config(bg=self.default_button_color)

        # Display an information message box with the starting player
        messagebox.showinfo(
            title="Starting Player",
            message=f"Player {self.current_player} starts first."
        )

    def create_buttons(self):
        """Creates the Tic Tac Toe game board with buttons.

        This method iterates through a 3x3 grid to create buttons for each cell on the game board. Each button is
        configured with an empty text label, a font size, and a width/height. When a button is clicked, it calls the
        `click_button` method, passing its row and column coordinates. The buttons are added to the game board using
        the Tkinter `grid` layout manager. Additionally, this method creates a label to display the game statistics
        (X wins, O wins, ties).
        """

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.click_button(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        # Create statistics label
        self.statistics_label = tk.Label(self.root, text=f"X: {self.player_x_wins} | O: {self.player_o_wins} | Ties: {self.ties}", font=('Arial', 12))
        self.statistics_label.grid(row=5, column=1, columnspan=2, padx=10, pady=10)

    def click_button(self, row, col):
        """Handles a button click on the Tic Tac Toe game board.

        This method checks if the clicked button's space is empty. If empty, it places the current player's mark (X or O)
        on the button and updates the game board. It then checks for a winner using the `check_win` method. If there's a
        winner, it calls the `show_winner` method to display the winner and disable all buttons. If no winner, it switches
        the current player to X or O using the `switch_player` method.
        """
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col].config(bg=self.player_colors[self.current_player])
            if self.check_win():
                self.show_winner()
            else:
                self.switch_player()

    def check_win(self):
        """Checks for a winner on the Tic Tac Toe game board.

        This method checks rows, columns, and diagonals for three matching marks (X or O) to determine a winner.
        It also checks for a "Cat's Game" scenario where all cells are filled but no winner is found.

        Returns:
            True if a winner is found or a "Cat's Game" occurs, False otherwise.
        """

        # Check rows
        for i in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)):
                return True

        # Check columns
        for j in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for i in range(3)):
                return True

        # Check diagonals
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)):
            return True
        if all(self.buttons[i][2-i]['text'] == self.current_player for i in range(3)):
            return True
        
        # Check "Cat's Game"
        if all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            self.current_player = "Cat's Game"
            return True

        return False

    def switch_player(self):
        """Switches the current player."""

        self.current_player = "O" if self.current_player == "X" else "X"

    def show_winner(self):
        """Displays the winner and disables buttons."""

        if self.current_player == "X":
            self.player_x_wins += 1
        elif self.current_player == "O":
            self.player_o_wins += 1
        elif self.current_player == "Cat's Game":
            self.ties += 1
        self.winner_label.config(text=f"{self.current_player} wins!")

        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'
        self.root.after(5000, self.reset_game)


    def reset_game(self):
        """Resets the game board and variables for a new game."""
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j]['state'] = 'normal'
        self.winner = None
        self.winner_label.config(text="Who wins?")
        self.start_game()

        # Update statistics label
        self.statistics_label.config(text=f"X: {self.player_x_wins} | O: {self.player_o_wins} | Ties: {self.ties}")

if __name__ == "__main__":
    game = TicTacToe()
