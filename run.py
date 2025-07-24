import numpy as np

board = np.zeros((3,3), dtype = int)


# Convert to symbol
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
        row_symbols = [get_symbol(cell) for cell in row]
