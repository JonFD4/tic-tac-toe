import numpy as np




# helper function that Convert numbers to symbols
def get_symbol(cell):
    if cell == 1:
        return 'X'
    elif cell == -1:
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
    


def play_game():
    board = np.zeros((3,3), dtype = int)
    current_player = 1

    while True:
        print_board(board)
        get_player_move(current_player, board)

        print_board(board)
        current_player = -current_player
        break

play_game()