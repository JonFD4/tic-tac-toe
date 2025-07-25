import numpy as np
# helper function that Convert numbers to symbols
def get_symbol(value):
    if value == 1:
        return 'X'
    elif value == -1:
        return 'O'
    else:
        return ' '


# print board
def print_board(board):
    for row_index, row in enumerate(board):
        row_symbol = [get_symbol(cell) for cell in row]
        print('  ' + ' | '.join(row_symbol))
        if row_index < 2:
            print("----+---+----")



# get player move
def get_player_move(player, board):
    while True:
        print(f"Player{get_symbol(player)}'s turn. ")
        try:
            row= int(input('Enter row(0,1,2): '))
            col= int(input('Enter column(0,1,2): '))
        except valueError:
            print('Please, enter numbers only.')
            continue
        
        if row not in [0,1,2] or col not in  [0,1,2]:
            print('Invalid Position, Try again')
            continue
        if board[row,col]!=0:
            print('That spot is taken. Try another')
            continue

        board[row,col]=player
        print(f"Player {get_symbol(player)} placed at ({row}, {col})")

        break
    
# check for wins row, column and diagonals

def check_winner(board):
    # check row wins
    for row in board:
        row_sum = np.sum(row)
        if row_sum == 3:
            return 1
        elif row_sum == -3:
            return -1
    # check column wins
    for col in board:
        col_sum = np.sum(col)
        if col_sum == 3:
            return 1
        elif col_sum == -3:
            return -1
    
    #check main diagonal wins
    # top-left to right-bottom
    main_diag_sum = np.trace(board)
    if main_diag_sum = 3:
        return 1
    elif main_diag_sum = -3:
        return -1

    #check main diagonal wins
    # top-left to right-bottom
    main_diag_sum = np.trace(board)
    if main_diag_sum = 3:
        return 1
    elif main_diag_sum = -3:
        return -1

    # top-right to bottom-left
    anti_diag_sum = np.trace(np.flipr(board))
    if anti_diag_sum = 3:
        return 1
    elif anti_diag_sum = -3:
        return -1


def play_game():
    board = np.zeros((3,3), dtype = int)
    current_player = 1

    while True:
        print_board(board)
        get_player_move(current_player, board)

        print_board(board)
        # check for wins
        result = check_winner(board)
    
        current_player = -current_player
        break

play_game()