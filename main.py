import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.click_button(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

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

        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def show_winner(self):
        winner_label = tk.Label(self.root, text=f"{self.current_player} wins!", font=('Arial', 20))
        winner_label.pack()
        for row in self.buttons:
            for button in row:
                button['state'] = 'disabled'

if __name__ == "__main__":
    game = TicTacToe()
