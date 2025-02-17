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

    turns_taken = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] != None:
                turns_taken += 1

    return X if (turns_taken % 2) == 0 else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions_available = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == None:
                actions_available.add((row, col))

    return actions_available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    current_player = player(board)
    actions_available = actions(board)
    result_board = copy.deepcopy(board) 

    if action not in actions_available:
        raise Exception("Action not valid")
    else:
        result_board[action[0]][action[1]] = current_player
    
    return result_board 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and cols
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]        
        if board[0][i] == board[1][i] == board[2][i] and board[i][0] != EMPTY:
            return board[0][i]

    # Check diagonals     
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if not actions(board) or winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    alpha = -float('inf')
    beta = float('inf')

    if terminal(board):
        return None

    def maxValue(board, alpha, beta):
        v = -float('inf')
        if terminal(board):
            return utility(board)  
        for action in actions(board):
            v = max(v, minValue(result(board,action), alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v

    def minValue(board, alpha, beta):
        v = float('inf')
        if terminal(board):
            return utility(board)  
        for action in actions(board):
            v = min(v, maxValue(result(board,action), alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v
    
    if player(board) == X:
        max_val = -float('inf')
        for action in actions(board):
            current_val = minValue(result(board, action), alpha, beta)
            if current_val > max_val:
                max_val = current_val
                best_action = action
        return best_action

    else:
        min_val = float('inf')
        for action in actions(board):
            current_val = maxValue(result(board, action), alpha, beta)
            if current_val < min_val:
                min_val = current_val
                best_action = action
        return best_action