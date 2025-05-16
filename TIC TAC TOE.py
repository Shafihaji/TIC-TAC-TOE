import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), height=2, width=5, command=lambda i=i: self.cell_clicked(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def cell_clicked(self, index):
        if not self.board[index] and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == ""]
        if empty_cells and not self.check_winner():
            index = random.choice(empty_cells)
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "X"

    def check_winner(self):
        winning_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                return True
        return False

    def reset_board(self):
        for button in self.buttons:
            button.config(text="")
        self.board = [""] * 9
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
