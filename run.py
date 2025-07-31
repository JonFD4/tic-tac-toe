import numpy as np
import random
# helper function that Convert numbers to symbols
def get_symbol(value):
    if value == 1:
        return ' X '
    elif value == -1:
        return ' O '
    else:
        return '   '


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
        except ValueError:
            print('Please, enter numbers only.')
            continue
        
        if row not in [0,1,2] or col not in  [0,1,2]:
            print('Invalid Position, Try again')
            continue
        if board[row,col]!=0:
            print('That spot is taken. Try another')
            continue
        print(f"Player {get_symbol(player)} placed at ({row}, {col})")
        board[row,col]=player
        

        break

 # Evaluate empty cells   
def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row,col]== 0:
                empty_cells.append((row,col))
    return empty_cells

def get_computer_moves(board,difficulty):
    empty_cells = get_empty_cells(board)
    if difficulty == 'easy':
        row,col = random.choice(empty_cells)
        board[row,col]= -1
        return

    elif difficulty == 'medium':
        # Try to win
        for row,col in empty_cells:
            dp_board = board.copy() 
            dp_board[row,col] = -1
            if check_winner(dp_board) == -1:
                board[row,col] = -1
                return 
        #Try to block
        for row,col in empty_cells:
                dp_board = board.copy() 
                dp_board[row,col] = 1
                if check_winner(dp_board) == 1:
                    board[row,col] = -1
                    return 
       
        #Fall back
        row, col = random.choice(empty_cells)
        board[row,col]= -1
        return



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
    if main_diag_sum == 3:
        return 1
    elif main_diag_sum == -3:
        return -1

    # top-right to bottom-left
    anti_diag_sum = np.trace(np.fliplr(board))
    if anti_diag_sum == 3:
        return 1
    elif anti_diag_sum == -3:
        return -1

    # check for draws
    if 0 not in board:
        return 'draw'

    return None


def setup_game():
    mode = input('Who would you like to play against?\n1. Human\n2. Computer\n>')
    if mode == '1':
        opponent_type = 'human'
        difficulty = None
    elif mode =='2':
        opponent_type = 'computer'
        difficulty_choice =input('Choose the level of computer difficulty:\n1. Easy\n2. Medium\n3. Hard\n>')
        if difficulty_choice == '1':
            difficulty = 'easy'
        elif difficulty_choice == '2':
            difficulty = 'medium'
        elif difficulty_choice == '3':
            difficulty = 'hard'
        else:
            print("Invalid input. Defaulting to easy.")
            difficulty = 'easy'
    else:
        print("Invalid input. Defaulting to human.")
        opponent_type = 'human'
        difficulty = None

    return opponent_type, difficulty, 


def play_game(opponent_type,difficulty):
    board = np.zeros((3,3), dtype = int)
    current_player = 1

    while True:
        print_board(board)
        if opponent_type == 'computer' and current_player == -1:
            get_computer_moves(board, difficulty)
        else:
            get_player_move(current_player, board)
    
        # check for wins
        result = check_winner(board)
        if result == 1:
            print('Player X has won this game')
            break
        elif result == -1:
            print('Player O has won this game')
            break
        elif result == 'draw':
            print('It is a draw')
            break
        current_player = -current_player

opponent_type, difficulty = setup_game()
play_game(opponent_type, difficulty)