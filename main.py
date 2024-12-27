import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Initialize statistics
        self.player_x_wins = 0
        self.player_o_wins = 0
        self.ties = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

        self.winner_label = tk.Label(self.root, text=f"Who wins?", font=('Arial', 15))
        self.winner_label.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
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
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            if self.check_win():
                self.show_winner()
            else:
                self.switch_player()

    def check_win(self):
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
        self.current_player = "O" if self.current_player == "X" else "X"

    def show_winner(self):

        if self.current_player == "X":
            self.player_x_wins += 1
        elif self.current_player == "O":
            self.player_o_wins += 1
        elif self.current_player == "Cat's Game":
            self.ties += 1
        self.winner_label.configure(text=f"{self.current_player} wins!")


        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'

        # Deaktivace tlačítek a krátká pauza před automatickou obnovou
        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'
        self.root.after(5000, self.reset_game)


    def reset_game(self):
        # Vyprázdnění herního pole, reset proměnných a aktivace tlačítek
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j]['state'] = 'normal'
        self.current_player = "X"
        self.winner = None
        self.winner_label.configure(text="Who wins?")

        # Update statistics label
        self.statistics_label.configure(text=f"X: {self.player_x_wins} | O: {self.player_o_wins} | Ties: {self.ties}")

if __name__ == "__main__":
    game = TicTacToe()
