from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import random
import tkinter.messagebox as messagebox
from idlelib.tooltip import Hovertip

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
        self.root.resizable(False, False)

        # Initialize statistics
        self.player_x_wins = 0          # Number of wins for player X
        self.player_o_wins = 0          # Number of wins for player O
        self.ties = 0                   # Number of ties
        self.current_player = None      # Current player (X or O)
        self.winner = None              # Stores the winner (X, O, or "Cat's Game")
        self.buttons = [[None for _ in range(3)] for _ in range(3)] # 2D list to hold buttons

        self.winner_label = tk.Label(self.root, text=f"Who wins?", font=('Arial', 14))
        self.winner_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.create_widgets()    # Create the game board buttons
        self.player1_choice, self.player1_color = self.choose_symbol_color(1)  # Player 1 chooses symbol and color
        self.player2_choice, self.player2_color = self.choose_symbol_color(2)  # Player 2 chooses symbol and color (with limitations)
        
        if "X" in self.player1_choice and "O" in self.player2_choice:
            self.player_colors = {"X": self.player1_color, "O": self.player2_color}         # Player colors

        elif "O" in self.player1_choice and "X" in self.player2_choice:
            self.player_colors = {"X": self.player2_color, "O": self.player1_color}         # Player colors
        
        self.default_button_color = "lightblue"                                             # Default button color
        
        self.start_game()        # Start a new game
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind protocol for close button
        self.root.mainloop()

    def on_closing(self):
        """Confirms if the user wants to quit the game."""
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

    def choose_symbol_color(self, player):
        """Vytvoří dialogové okno pro výběr X nebo O a barvu z palety s vizuální odezvou."""
        choice = tk.StringVar(value=None)
        color = tk.StringVar(value=None)

        def set_choice(symbol):
            if player == 2:
                if symbol in self.player1_choice:  # Check if symbol already chosen
                    return  # Do nothing if already chosen
            choice.set(symbol)
            x_button.config(relief=tk.RAISED if symbol != "X" else tk.SUNKEN)
            o_button.config(relief=tk.RAISED if symbol != "O" else tk.SUNKEN)

        def set_color(event=None, button=None):
            if button:
                chosen_color = button.cget("bg")
                color.set(chosen_color)

                for btn in color_buttons:
                    btn.config(relief=tk.RAISED)
                button.config(relief=tk.SUNKEN)

        def finalize_choice():
            if choice.get() and color.get():
                top.destroy()
            else:
                if not choice.get():
                    messagebox.showwarning("Warning", "Choose symbol, please.")
                if not color.get():
                    messagebox.showwarning("Warning", "Choose color, please.")

        top = tk.Toplevel(self.root)
        top.title("Symbol and color")
        top.resizable(False, False)
        top.transient(self.root)
        # Inactivate the close button ("X") of the top-level window
        top.protocol("WM_DELETE_WINDOW", lambda: None)

        symbol_frame = tk.Frame(top)
        symbol_frame.pack(pady=(10, 0))

        x_button = tk.Button(symbol_frame, text="X", command=lambda: set_choice("X"), font=('Arial', 20), width=5, height=2, relief=tk.RAISED)
        o_button = tk.Button(symbol_frame, text="O", command=lambda: set_choice("O"), font=('Arial', 20), width=5, height=2, relief=tk.RAISED)

        if player == 2:
            if "X" in self.player1_choice:  # Check if symbol already chosen
                x_button.config(state=tk.DISABLED)
                Hovertip(x_button, "This symbol has already been chosen by Player 1")
            if "O" in self.player1_choice:  # Check if symbol already chosen
                o_button.config(state=tk.DISABLED)
                Hovertip(o_button, "This symbol has already been chosen by Player 1")

        x_button.pack(side=tk.LEFT, padx=10)
        o_button.pack(side=tk.LEFT, padx=10)

        color_frame = tk.Frame(top)
        color_frame.pack(pady=(10, 10))

        colors = ["lightgreen", "lightcoral", "lightblue", "yellow", "pink", "lightgray"]
        color_buttons = []
        for c in colors:
            color_button = tk.Button(color_frame, bg=c, width=3, relief=tk.RAISED)
            color_button.bind("<Button-1>", set_color)
            color_button.pack(side=tk.LEFT, padx=5)
            color_buttons.append(color_button)
        
        for btn in color_buttons:
            btn.config(command=lambda btn=btn: set_color(button=btn))

        if player == 2 and self.player1_color:
            for btn in color_buttons:
                if btn.cget("bg") == self.player1_color:
                    btn.config(state=tk.DISABLED)
                    Hovertip(btn, "This color has already been chosen by Player 1")

        confirm_button = tk.Button(top, text="Choose for Player 1", command=finalize_choice)
        confirm_button.pack(pady=(0, 10))
        if player == 2:
            confirm_button.config(text="Choose for Player 2")

        top.wait_window()
        return choice.get(), color.get()

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

    def create_widgets(self):
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

        # Check rows and columns
        for i in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)):
                return True
            if all(self.buttons[j][i]['text'] == self.current_player for j in range(3)):
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
        self.root.after(3500, self.reset_game)


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