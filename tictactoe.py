"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Counts the number of occupied cells
    occupied_cells = sum(1 for row in board for cell in row if cell != EMPTY)

    # If the number of occupied cells is even, it's player X's turn, otherwise it's player O's turn
    return X if occupied_cells % 2 == 0 else O

# Needs improvement
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Make X (Computer) place in the middle if the board is empty
    """
    TO DO
    """
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Creating a copied board / consider deep copy

    cboard =  copy.deepcopy(board)
    (row, col) = action
                
    # Check if cell is empty and then make the move
    if cboard[row][col] == EMPTY:
        cboard[row][col] = player(board)
    else:
        raise ValueError("Invalid action: Cell is occupied")
    
    return cboard
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        elif all(board[row][col] == O for row in range(3)):
            return O
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # If no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    elif terminal(board):
        return 0
    else:
        return ValueError("Game isn't over") 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    # Get all possible actions for the current player
    possible_actions = actions(board)
    if player(board) == X:
        # If the current player is X, maximize the value
        return max(possible_actions, key=lambda action: min_value(result(board, action)))
    else:
        # If the current player is O, minimize the value
        return min(possible_actions, key=lambda action: max_value(result(board, action)))