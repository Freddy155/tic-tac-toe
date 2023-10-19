import tkinter as tk

def display_board():
    for row in range(3):
        for col in range(3):
            cell = board[row][col]
            buttons[row][col].config(text=cell, state="disabled")

def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw():
    return all(cell != ' ' for row in board for cell in row)

def on_button_click(row, col):
    global current_player

    if board[row][col] == ' ':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_win(current_player):
            display_board()
            message_label.config(text=f"Player {current_player} wins!")
            record[current_player] += 1
            update_record_label()
            return

        if check_draw():
            display_board()
            message_label.config(text="It's a draw!")
            return

        current_player = 'O' if current_player == 'X' else 'X'
        message_label.config(text=f"Player {current_player}'s turn")

def reset_board():
    global board, current_player
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
            buttons[row][col].config(text=' ', state="active")
    current_player = 'X'
    message_label.config(text="Player X's turn")

def update_record_label():
    record_label.config(text=f"Player X: {record['X']} | Player O: {record['O']}")

app = tk.Tk()
app.title("Tic-Tac-Toe")

board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

record = {'X': 0, 'O': 0}

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(app, text=' ', width=10, height=2, command=lambda row=row, col=col: on_button_click(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

message_label = tk.Label(app, text="Player X's turn", font=("Helvetica", 14))
message_label.grid(row=3, columnspan=3)

record_label = tk.Label(app, text=f"Player X: {record['X']} | Player O: {record['O']}", font=("Helvetica", 12))
record_label.grid(row=4, columnspan=3)

reset_button = tk.Button(app, text="Reset", width=10, height=2, command=reset_board)
reset_button.grid(row=5, columnspan=3)

current_player = 'X'

app.mainloop()
